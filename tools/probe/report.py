#!/usr/bin/env python3
"""Probe report generator — every metric derived from an artifact, never from
executor declaration (Sözleşme‑10).

Usage:
  python tools/probe/report.py [--probe-root docs/probe] [--repo .]
      [--transcript PATH] [--test-xml PATH]

Inputs (artifact sources):
  .markers/{kurulum-start,kurulum-end,uretim-start,uretim-end}.ts   -> T_kurulum, T_uretim
  .markers/editor-acik-*.ts / editor-kapali-*.ts                    -> declared Editor sessions (iki-durum)
  <repo>/Temp/UnityLockfile                                         -> iki-durum guard state at report time
  --transcript (Claude Code session .jsonl)                         -> human interventions
  Unity Test results (NUnit XML, from -batchmode -runTests)         -> tests/bot status
  scene/prefab object counts                                        -> P1 (bootstrap-only) violation

Editor GUI dokunuşu sayımı YOKTUR (H2): P1 altında sahneler değişmediği için git
izine dayalı sayım kördü; ölçemediğimiz şeyi ölçüyormuş gibi yapmıyoruz. Yerine:
P1 ikili kapısı + deklare edilmiş Editor oturum damgaları + lockfile bekçisi.

Output: <probe-root>/rapor.md  (overwrites). Exit code: 0 = BAŞARILI, 1 = SARI, 2 = BAŞARISIZ.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

# Thresholds — sonda v0.15+ (ilk sonda bunları da kalibre eder)
T_OK = 6 * 3600          # T_uretim ≤ 6 sa
T_FAIL = 12 * 3600       # T_uretim > 12 sa
MUDAHALE_OK = 10
MUDAHALE_FAIL = 20
SCENE_OBJECT_LIMIT = 3   # bootstrap-only: tek sahne ≈ tek GameObject


def sh(cmd, cwd=None):
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120)
        return out.returncode, (out.stdout or "") + (out.stderr or "")
    except Exception as e:  # noqa: BLE001
        return 1, f"komut hatası: {e}"


def read_marker(probe_root, name):
    p = os.path.join(probe_root, ".markers", f"{name}.ts")
    if not os.path.exists(p):
        return None
    try:
        return float(open(p, encoding="utf-8").read().strip())
    except ValueError:
        return None


def read_editor_sessions(probe_root):
    """Deklare edilmiş Editor oturumları: editor-acik-N / editor-kapali-N eşleri."""
    mdir = os.path.join(probe_root, ".markers")

    def ts(kind, n):
        p = os.path.join(mdir, f"{kind}-{n}.ts")
        if not os.path.exists(p):
            return None
        try:
            return float(open(p, encoding="utf-8").read().strip())
        except ValueError:
            return None

    sessions, n, unpaired = [], 1, 0
    while True:
        a, k = ts("editor-acik", n), ts("editor-kapali", n)
        if a is None and k is None:
            break
        if a is None or k is None:
            unpaired += 1
        elif k >= a:
            sessions.append(k - a)
        n += 1
    return sessions, unpaired


def fmt_dur(seconds):
    if seconds is None:
        return "ölçülemedi"
    h = seconds / 3600.0
    return f"{h:.2f} sa ({int(seconds)} sn)"


def count_human_messages(transcript_path):
    if not transcript_path or not os.path.exists(transcript_path):
        return None
    n = 0
    with open(transcript_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("type") != "user":
                continue
            msg = obj.get("message", {})
            content = msg.get("content")
            # İnsan yazısı: düz metin; tool sonuçları list içinde gelir, sayılmaz.
            if isinstance(content, str) and content.strip():
                n += 1
    return n


def parse_tests(xml_path):
    if not xml_path or not os.path.exists(xml_path):
        return None
    try:
        root = ET.parse(xml_path).getroot()
    except ET.ParseError:
        return None
    # NUnit3 <test-run ... total=.. passed=.. failed=.. inconclusive=..>
    tr = root if root.tag == "test-run" else root.find(".//test-run")
    if tr is None:
        return None
    g = lambda k: int(tr.attrib.get(k, 0))
    return {"total": g("total"), "passed": g("passed"), "failed": g("failed"), "errors": g("errors")}


def scene_object_counts(repo):
    counts = []
    for path in glob.glob(os.path.join(repo, "Assets", "**", "*.unity"), recursive=True) + \
                glob.glob(os.path.join(repo, "Assets", "**", "*.prefab"), recursive=True):
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                n = sum(1 for ln in f if ln.startswith("GameObject:"))
        except OSError:
            n = -1
        counts.append((os.path.relpath(path, repo), n))
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe-root", default="docs/probe")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--transcript", default=None)
    ap.add_argument("--test-xml", default=None)
    args = ap.parse_args()

    t0 = time.strftime("%Y-%m-%d %H:%M:%S")

    k0 = read_marker(args.probe_root, "kurulum-start")
    k1 = read_marker(args.probe_root, "kurulum-end")
    u0 = read_marker(args.probe_root, "uretim-start")
    u1 = read_marker(args.probe_root, "uretim-end")
    t_kur = (k1 - k0) if (k0 is not None and k1 is not None) else None
    t_ure = (u1 - u0) if (u0 is not None and u1 is not None) else None

    mudahale = count_human_messages(args.transcript)
    tests = parse_tests(args.test_xml)
    scenes = scene_object_counts(args.repo)
    sessions, unpaired = read_editor_sessions(args.probe_root)
    lockfile = os.path.join(args.repo, "Temp", "UnityLockfile")
    lockfile_present = os.path.exists(lockfile)

    p1_violations = [(p, n) for p, n in scenes if n > SCENE_OBJECT_LIMIT]
    tests_green = bool(tests) and tests["failed"] == 0 and tests["errors"] == 0

    # --- karar (yalnız T_uretim + müdahale + P1 + testler, sonda tablosu) ---
    fails, warns = [], []
    if t_ure is not None and t_ure > T_FAIL:
        fails.append(f"T_uretim > {T_FAIL // 3600} sa")
    if mudahale is not None and mudahale > MUDAHALE_FAIL:
        fails.append(f"müdahale > {MUDAHALE_FAIL}")
    if tests and not tests_green:
        fails.append("test/bot yeşil değil")
    if p1_violations:
        fails.append("P1 ihlali (Bootstrap dışı sahne nesnesi)")

    if t_ure is not None and T_OK < t_ure <= T_FAIL:
        warns.append(f"T_uretim {T_OK // 3600}–{T_FAIL // 3600} sa bandında")
    if mudahale is not None and MUDAHALE_OK < mudahale <= MUDAHALE_FAIL:
        warns.append(f"müdahale {MUDAHALE_OK}–{MUDAHALE_FAIL} bandında")
    if lockfile_present:
        warns.append("lockfile rapor anında mevcut — iki-durum ihlali olası (Editor açık kalmış?)")
    if unpaired:
        warns.append(f"eşsiz Editor damgası: {unpaired} (açık oturum kapanmadı?)")

    missing = []
    if t_ure is None:
        missing.append("uretim marker'ları")
    if mudahale is None:
        missing.append("transkript")
    if tests is None:
        missing.append("test XML")
    if missing:
        warns.append("ölçülemeyen kaynak: " + ", ".join(missing))

    verdict = "BAŞARISIZ" if fails else ("SARI" if warns else "BAŞARILI")

    L = []
    A = L.append
    A("# SONDA RAPORU\n")
    A("_Bu rapor `tools/probe/report.py` tarafından üretilmiştir; elle düzenlenmez — Sözleşme‑10._\n")
    A(f"Üretim: {t0}\n")
    A(f"## KARAR: **{verdict}**\n")
    if fails:
        A("Kırmızılar: " + "; ".join(fails) + "\n")
    if warns:
        A("Sarılar: " + "; ".join(warns) + "\n")
    A("\n## Metrikler (her satır izden türetilmiştir)\n")
    A("| Metrik | Değer | Kaynak artefakt | Sınır | Durum |")
    A("|---|---|---|---|---|")
    A(f"| T_kurulum | {fmt_dur(t_kur)} | `.markers/kurulum-*.ts` | tabloya girmez | bilgi |")
    lim_t = f"≤{T_OK // 3600} sa / >{T_FAIL // 3600} sa"
    durum_t = "—" if t_ure is None else ("yeşil" if t_ure <= T_OK else ("kırmızı" if t_ure > T_FAIL else "sarı"))
    A(f"| T_uretim | {fmt_dur(t_ure)} | `.markers/uretim-*.ts` | {lim_t} | {durum_t} |")
    dm = "—" if mudahale is None else ("yeşil" if mudahale <= MUDAHALE_OK else ("kırmızı" if mudahale > MUDAHALE_FAIL else "sarı"))
    A(f"| İnsan müdahalesi | {mudahale if mudahale is not None else 'ölçülemedi'} | transkript: `{args.transcript}` | ≤{MUDAHALE_OK} / >{MUDAHALE_FAIL} | {dm} |")
    if tests is None:
        A(f"| Testler/bot | ölçülemedi | `--test-xml {args.test_xml}` | yeşil | — |")
    else:
        A(f"| Testler/bot | {tests['passed']}/{tests['total']} geçti, {tests['failed']} kırmızı | NUnit XML (batchmode) | fail=0 | {'yeşil' if tests_green else 'kırmızı'} |")
    if scenes:
        for p, n in scenes:
            st = "yeşil" if 0 <= n <= SCENE_OBJECT_LIMIT else "kırmızı"
            A(f"| P1 nesne sayımı: {p} | {n} GameObject | {p} | ≤{SCENE_OBJECT_LIMIT} | {st} |")
    else:
        A("| P1 nesne sayımı | sahne bulunamadı | `Assets/**/*.unity` | ≤3 | — |")
    A(f"| Editor oturumları | {len(sessions)} oturum, toplam {fmt_dur(sum(sessions) if sessions else 0.0)} | `.markers/editor-*-N.ts` | deklare edilmişse serbest | {'sarı' if unpaired else 'bilgi'} |")
    A(f"| Lockfile (rapor anı) | {'MEVCUT' if lockfile_present else 'yok'} | `{lockfile}` | yok | {'sarı' if lockfile_present else 'yeşil'} |")
    A("\n## Kör nokta beyanı (H2)\n")
    A("Editor GUI'sindeki elle dokunuş **ölçülmez** — hiçbir artefakt onu güvenilir "
      "saymıyor (P1 altında sahne dosyaları neredeyse değişmez). Bu rapor o alanı "
      "ölçüyormuş gibi YAPMAZ. Sınırlayıcı disiplin: (1) P1 ikili kapısı — sahnede "
      "Bootstrap dışı nesne varsa BAŞARISIZ; (2) iki-durum — her Editor oturumu "
      "damgalı, batchmode yalnız lockfile yokken; (3) kanıt koşuları batchmode'dadır "
      "— GUI'siz süreçte insan dokunması teknik olarak imkânsızdır. Kalan alan kabul "
      "edilmiş kör noktadır ve bu beyanla kayıtlıdır.\n")

    out_path = os.path.join(args.probe_root, "rapor.md")
    os.makedirs(args.probe_root, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"rapor: {out_path} — {verdict}")
    return {"BAŞARILI": 0, "SARI": 1, "BAŞARISIZ": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
