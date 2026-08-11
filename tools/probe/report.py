#!/usr/bin/env python3
"""Probe report generator — every metric derived from an artifact, never from
executor declaration (Sözleşme‑10).

Usage:
  python tools/probe/report.py [--probe-root docs/probe] [--project ../probe-project]
      [--transcript PATH] [--test-xml PATH ...]

Inputs (artifact sources):
  .markers/{kurulum,uretim,build}-{start,end}.ts    -> T_kurulum, T_uretim, T_build
  .markers/editor-acik-N / editor-kapali-N          -> declared MCP/Editor sessions
  .markers/insan-kapisi-N                           -> PRIMARY human-gate count (müdahale)
  --transcript (Claude Code .jsonl)                 -> CROSS-CHECK only (uyuşmazlık SARI)
  <project>/Temp/UnityLockfile                      -> iki-durum guard at report time
  --test-xml (repeatable; NUnit XML, batchmode)     -> tests/bot status
  <probe-root>/kaynak/**/*.unity|prefab (kopya)     -> P1 nesne sayımı (≤2)

Editor GUI dokunuşu SAYILMAZ (H2) ve sahne varsayılandan sapamadığı için elle
kurulum oyuna etki etmez; kör nokta beyanı var. T_build tabloya girmez — araç
zinciri sorusunu üretim sorusundan ayırır.

Output: <probe-root>/rapor.md (overwrites). Exit: 0 = BAŞARILI, 1 = SARI, 2 = BAŞARISIZ.
"""
import argparse
import glob
import json
import os
import sys
import time
import xml.etree.ElementTree as ET

# Thresholds — sonda v0.17+ (ilk sonda bunları da kalibre eder)
T_OK = 6 * 3600          # T_uretim ≤ 6 sa
T_FAIL = 12 * 3600       # T_uretim > 12 sa
KAPI_OK = 10
KAPI_FAIL = 20
# P1 limiti sabit DEĞİL: ilk koşunun ölçtüğü scene-baseline.json kaydıdır (K2) —
# "{pin, dosya, sha256, nesne_sayisi}". Unity/şablon değişince kural güncellenir.


def read_baseline(probe_root):
    p = os.path.join(probe_root, "scene-baseline.json")
    if not os.path.exists(p):
        return None
    try:
        d = json.loads(open(p, encoding="utf-8").read())
        if isinstance(d.get("nesne_sayisi"), int):
            return d
    except (json.JSONDecodeError, ValueError):
        pass
    return None


corrupt_markers = []  # (yol, ham_icerik) — dosya VAR ama okunamıyor; eksikten FARKLI


def read_marker(probe_root, name):
    p = os.path.join(probe_root, ".markers", f"{name}.ts")
    if not os.path.exists(p):
        return None  # dosya yok = adım atlanmış (beklenebilir)
    raw = open(p, encoding="utf-8", errors="replace").read().strip()
    try:
        return int(raw) / 1000.0  # epoch milisaniye (marker.py v1.0.2; kültür-bağımsız)
    except ValueError:
        corrupt_markers.append((p, raw))  # BOZUK = hata; sessizce yutulmaz
        return None


def read_numbered(probe_root, prefix):
    out, n = [], 1
    while True:
        v = read_marker(probe_root, f"{prefix}-{n}")
        if v is None:
            break
        out.append(v)
        n += 1
    return out


def read_editor_sessions(probe_root):
    acik, kapali = read_numbered(probe_root, "editor-acik"), read_numbered(probe_root, "editor-kapali")
    sessions = [k - a for a, k in zip(acik, kapali) if k >= a]
    unpaired = abs(len(acik) - len(kapali))
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
            content = obj.get("message", {}).get("content")
            if isinstance(content, str) and content.strip():
                n += 1
    return n


def parse_tests(xml_path):
    try:
        root = ET.parse(xml_path).getroot()
    except (ET.ParseError, OSError):
        return None
    tr = root if root.tag == "test-run" else root.find(".//test-run")
    if tr is None:
        return None
    g = lambda k: int(tr.attrib.get(k, 0))
    return {"total": g("total"), "passed": g("passed"), "failed": g("failed"), "errors": g("errors")}


def scene_object_counts(kaynak_dir):
    counts = []
    for path in glob.glob(os.path.join(kaynak_dir, "**", "*.unity"), recursive=True) + \
                glob.glob(os.path.join(kaynak_dir, "**", "*.prefab"), recursive=True):
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                n = sum(1 for ln in f if ln.startswith("GameObject:"))
        except OSError:
            n = -1
        counts.append((os.path.relpath(path, kaynak_dir), n))
    return counts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe-root", default="docs/probe")
    ap.add_argument("--project", default="../probe-project")
    ap.add_argument("--transcript", default=None)
    ap.add_argument("--test-xml", action="append", default=[])
    args = ap.parse_args()

    t0 = time.strftime("%Y-%m-%d %H:%M:%S")

    def pair(a, b):
        x, y = read_marker(args.probe_root, a), read_marker(args.probe_root, b)
        return (y - x) if (x is not None and y is not None) else None

    t_kur = pair("kurulum-start", "kurulum-end")
    t_ure = pair("uretim-start", "uretim-end")
    t_build = pair("build-start", "build-end")
    b0 = read_marker(args.probe_root, "build-start")
    b1 = read_marker(args.probe_root, "build-end")

    kapi = len(read_numbered(args.probe_root, "insan-kapisi"))
    transcript_n = count_human_messages(args.transcript)
    sessions, unpaired = read_editor_sessions(args.probe_root)
    lockfile = os.path.join(args.project, "Temp", "UnityLockfile")
    lockfile_present = os.path.exists(lockfile)

    baseline = read_baseline(args.probe_root)
    kaynak_dir = os.path.join(args.probe_root, "kaynak")
    scenes = scene_object_counts(kaynak_dir)
    p1_violations = []
    if baseline is not None:
        lim = baseline["nesne_sayisi"]
        for p, n in scenes:
            if p.endswith(".prefab"):
                # v1.0.6: varlık prefabı serbest (kod-standardi §10) ama yalnız
                # izinli kökte; sahne kuralı .unity satırında değişmeden sürer.
                if n > 0 and not p.replace("\\", "/").startswith("Assets/Prefabs/"):
                    p1_violations.append((p, n))
            elif n > lim:
                p1_violations.append((p, n))

    tests = []
    for xp in args.test_xml:
        r = parse_tests(xp)
        tests.append((xp, r))
    tests_known = [r for _, r in tests if r]
    tests_green = bool(tests) and all(r and r["failed"] == 0 and r["errors"] == 0 for _, r in tests)

    fails, warns = [], []
    if t_ure is not None and t_ure > T_FAIL:
        fails.append(f"T_uretim > {T_FAIL // 3600} sa")
    if kapi > KAPI_FAIL:
        fails.append(f"insan-kapisi > {KAPI_FAIL}")
    if tests and not tests_green:
        fails.append("test/bot yeşil değil")
    if p1_violations:
        fails.append("P1 ihlali (şablon sahnesine eklenmiş nesne)")

    if t_ure is not None and T_OK < t_ure <= T_FAIL:
        warns.append(f"T_uretim {T_OK // 3600}–{T_FAIL // 3600} sa bandında")
    if KAPI_OK < kapi <= KAPI_FAIL:
        warns.append(f"insan-kapisi {KAPI_OK}–{KAPI_FAIL} bandında")
    if lockfile_present:
        warns.append("lockfile rapor anında mevcut — iki-durum ihlali olası (Editor açık kalmış?)")
    if unpaired:
        warns.append(f"eşsiz Editor damgası: {unpaired} (açık oturum kapanmadı?)")
    if transcript_n is not None and transcript_n != kapi:
        warns.append(f"sayım tutarsız: insan-kapisi={kapi}, transkript={transcript_n}")

    missing = []
    if t_ure is None:
        missing.append("uretim marker'ları")
    if not args.test_xml:
        missing.append("test XML")
    if not os.path.isdir(kaynak_dir) or not scenes:
        missing.append("kaynak kopyası (P1 ölçülemez)")
    if baseline is None:
        missing.append("scene-baseline.json (P1 referansı ölçülemedi)")
    if b0 is None or b1 is None:
        missing.append("build damgası (T_build)")
    if corrupt_markers:
        warns.append("marker bozuk: " + "; ".join(
            f"{p}, içerik: {raw[:80]!r}" for p, raw in corrupt_markers))
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
    A(f"| T_uretim | {fmt_dur(t_ure)} | `.markers/uretim-*.ts` (kapı beklemeleri dahil) | {lim_t} | {durum_t} |")
    A(f"| T_build | {fmt_dur(t_build)} | `.markers/build-*.ts` | tabloya girmez — 0A takvimini besler | bilgi |")
    for p, raw in corrupt_markers:
        ham = raw[:80].replace("`", "'")
        A(f"| Marker bozuk | dosya var, okunamıyor | `{p}` — içerik: `{ham}` | tam sayı epoch ms | sarı |")
    dk = "yeşil" if kapi <= KAPI_OK else ("kırmızı" if kapi > KAPI_FAIL else "sarı")
    A(f"| İnsan müdahalesi (birincil) | {kapi} | `.markers/insan-kapisi-N.ts` | ≤{KAPI_OK} / >{KAPI_FAIL} | {dk} |")
    cc = "ölçülemedi (isteğe bağlı)" if transcript_n is None else str(transcript_n)
    A(f"| İnsan mesajı (çapraz kontrol) | {cc} | transkript: `{args.transcript}` | birincille uyuşmalı | {'sarı' if (transcript_n is not None and transcript_n != kapi) else 'bilgi'} |")
    mcp_val = f"{len(sessions)} oturum, toplam {fmt_dur(sum(sessions) if sessions else 0.0)}"
    if not sessions:
        mcp_val = "tetiklenmedi (bulgu)"
    A(f"| MCP/Editor oturumları | {mcp_val} | `.markers/editor-*-N.ts` | koşullu tetik | {'sarı' if unpaired else 'bilgi'} |")
    A(f"| Lockfile (rapor anı) | {'MEVCUT' if lockfile_present else 'yok'} | `{lockfile}` | yok | {'sarı' if lockfile_present else 'yeşil'} |")
    if not tests:
        A("| Testler/bot | ölçülemedi | `--test-xml` yok | yeşil | — |")
    for xp, r in tests:
        if r is None:
            A(f"| Testler/bot: {os.path.basename(xp)} | okunamadı | {xp} | yeşil | — |")
        else:
            ok = r["failed"] == 0 and r["errors"] == 0
            A(f"| Testler/bot: {os.path.basename(xp)} | {r['passed']}/{r['total']} geçti, {r['failed']} kırmızı | NUnit XML (batchmode) | fail=0 | {'yeşil' if ok else 'kırmızı'} |")
    if baseline is not None:
        A(f"| Sahne baseline | {baseline.get('nesne_sayisi')} GameObject, pin {baseline.get('pin')} | `scene-baseline.json` (dosya: `{baseline.get('dosya')}`, sha256 `{str(baseline.get('sha256'))[:12]}…`) | referans | bilgi |")
    if scenes:
        for p, n in scenes:
            if baseline is None:
                st = "—"
            elif p.endswith(".prefab"):
                izinli = p.replace("\\", "/").startswith("Assets/Prefabs/")
                st = "yeşil" if (izinli or n <= 0) else "kırmızı"
            else:
                st = "yeşil" if 0 <= n <= baseline["nesne_sayisi"] else "kırmızı"
            lim_txt = ("(izinli kök dışında: 0)" if p.endswith(".prefab")
                       else f"≤{baseline['nesne_sayisi'] if baseline else '?'}")
            A(f"| P1 nesne sayımı: {p} | {n} GameObject | `kaynak/{p}` | {lim_txt} | {st} |")
    else:
        A(f"| P1 nesne sayımı | kopya/sahne yok | `{kaynak_dir}` | baseline'a göre | — |")
    A("\n## Kör nokta beyanı (H2)\n")
    A("Editor GUI'sindeki elle dokunuş **ölçülmez** — hiçbir artefakt onu güvenilir "
      "saymıyor; üstelik sahne varsayılandan sapamadığı için elle kurulum oyuna "
      "ETKİ ETMEZ. Bu rapor o alanı ölçüyormuş gibi YAPMAZ. Sınırlayıcı disiplin: "
      "(1) P1 ikili kapısı — şablon sahnesine eklenmiş nesne varsa BAŞARISIZ; "
      "(2) iki-durum — MCP oturumları damgalı, batchmode yalnız lockfile yokken; "
      "(3) kanıt koşuları batchmode'dadır. Kalan alan kabul edilmiş kör noktadır "
      "ve bu beyanla kayıtlıdır.\n")

    out_path = os.path.join(args.probe_root, "rapor.md")
    os.makedirs(args.probe_root, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"rapor: {out_path} — {verdict}")
    return {"BAŞARILI": 0, "SARI": 1, "BAŞARISIZ": 2}[verdict]


if __name__ == "__main__":
    sys.exit(main())
