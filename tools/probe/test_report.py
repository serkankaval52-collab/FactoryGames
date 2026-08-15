#!/usr/bin/env python3
"""report.py + marker.py karar sınırı testleri (v1.0.9 / I.3 / Sözleşme-10).

Karar aracı (BAŞARILI/SARI/BAŞARISIZ hükmünü report.py verir) test edilmeden
yaşayamaz. Her test geçici dizinde fixture kurar, report.py'yi ALT SÜREÇ olarak
koşturur, çıkış kodu + rapor metni üzerinden hüküm verir. stdlib dışı yok.

Koşturma: python3 tools/probe/test_report.py  (CI: ci/factory-gates.yml arac-testleri)
"""
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.join(HERE, "report.py")
MARKER = os.path.join(HERE, "marker.py")
H = 3600 * 1000  # bir saat, milisaniye


def base_probe(d):
    """Tam-yeşil fixture: tüm marker'lar, baseline, 2 nesneli sahne, yeşil XML."""
    probe = os.path.join(d, "probe")
    mdir = os.path.join(probe, ".markers")
    os.makedirs(mdir)
    now = int(time.time() * 1000)
    marks = {"kurulum-start": now - 8 * H, "kurulum-end": now - 7 * H,
             "uretim-start": now - 2 * H, "uretim-end": now - 1 * H,
             "build-start": now - 45 * 60 * 1000, "build-end": now - 15 * 60 * 1000}
    for n, v in marks.items():
        with open(os.path.join(mdir, n + ".ts"), "w") as f:
            f.write(str(v) + "\n")
    with open(os.path.join(probe, "scene-baseline.json"), "w") as f:
        json.dump({"pin": "6000.3.0f1", "dosya": "SampleScene.unity",
                   "sha256": "ab" * 32, "nesne_sayisi": 2}, f)
    k = os.path.join(probe, "kaynak", "Assets")
    os.makedirs(k)
    with open(os.path.join(k, "SampleScene.unity"), "w") as f:
        f.write("GameObject:\n  m_Name: a\nGameObject:\n  m_Name: b\n")
    xml = os.path.join(d, "tests.xml")
    with open(xml, "w") as f:
        f.write('<test-run total="3" passed="3" failed="0" errors="0"/>')
    proj = os.path.join(d, "proj")
    os.makedirs(proj)  # Temp/UnityLockfile YOK
    return probe, proj, xml


def run_report(probe, proj, xml):
    return subprocess.run([sys.executable, REPORT, "--probe-root", probe,
                           "--project", proj, "--test-xml", xml],
                          capture_output=True, text=True, encoding="utf-8")


def rapor(probe):
    with open(os.path.join(probe, "rapor.md"), encoding="utf-8") as f:
        return f.read()


def set_uretim(probe, saat):
    now = int(time.time() * 1000)
    with open(os.path.join(probe, ".markers", "uretim-start.ts"), "w") as f:
        f.write(str(now - int(saat * H)) + "\n")
    with open(os.path.join(probe, ".markers", "uretim-end.ts"), "w") as f:
        f.write(str(now) + "\n")


def add_kapisi(probe, n):
    for i in range(1, n + 1):
        with open(os.path.join(probe, ".markers", f"insan-kapisi-{i}.ts"), "w") as f:
            f.write("1\n")


class TestKararSinirlari(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.probe, self.proj, self.xml = base_probe(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_01_tam_yesil_basarili(self):
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("**BAŞARILI**", rapor(self.probe))

    def test_02_uretim_sari_bant(self):  # 6 sa < t <= 12 sa
        set_uretim(self.probe, 8)
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn("**SARI**", rapor(self.probe))

    def test_03_uretim_kirmizi(self):  # t > 12 sa
        set_uretim(self.probe, 13)
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn("**BAŞARISIZ**", rapor(self.probe))

    def test_04_kapi_sari_bant(self):  # 10 < n <= 20
        add_kapisi(self.probe, 12)
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn("**SARI**", rapor(self.probe))

    def test_05_kapi_kirmizi(self):  # n > 20
        add_kapisi(self.probe, 21)
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn("**BAŞARISIZ**", rapor(self.probe))

    def test_06_bozuk_marker_eksikten_ayri(self):  # tr-TR virgülü sınıfı
        with open(os.path.join(self.probe, ".markers", "uretim-start.ts"), "w") as f:
            f.write("1,23\n")
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 1, r.stderr)  # bozuk = SARI, kırmızı değil
        m = rapor(self.probe)
        self.assertIn("Marker bozuk", m)
        self.assertIn("1,23", m)

    def test_07_eksik_marker(self):
        os.remove(os.path.join(self.probe, ".markers", "uretim-start.ts"))
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 1, r.stderr)
        m = rapor(self.probe)
        self.assertIn("ölçülemeyen kaynak", m)
        self.assertNotIn("Marker bozuk", m)

    def test_08_p1_sahne_ihlali(self):
        s = os.path.join(self.probe, "kaynak", "Assets", "SampleScene.unity")
        with open(s, "a") as f:
            f.write("GameObject:\n  m_Name: fazla\n")  # 3 > baseline 2
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 2, r.stderr)
        self.assertIn("P1 ihlali", rapor(self.probe))

    def test_09_prefab_izinsiz_kok_kirmizi(self):
        d = os.path.join(self.probe, "kaynak", "Assets", "UI")
        os.makedirs(d)
        with open(os.path.join(d, "x.prefab"), "w") as f:
            f.write("GameObject:\n")
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 2, r.stderr)
        m = rapor(self.probe)
        self.assertIn("x.prefab", m)
        self.assertIn("kırmızı", m)

    def test_10_prefab_izinli_kok_yesil(self):
        d = os.path.join(self.probe, "kaynak", "Assets", "Prefabs")
        os.makedirs(d)
        with open(os.path.join(d, "ok.prefab"), "w") as f:
            f.write("GameObject:\n")
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("ok.prefab", rapor(self.probe))

    def test_11_baseline_yoksa_sari(self):
        os.remove(os.path.join(self.probe, "scene-baseline.json"))
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 1, r.stderr)
        self.assertIn("scene-baseline", rapor(self.probe))

    def test_12_marker_py_kultur_bagimsiz_int(self):
        alt = os.path.join(self._tmp.name, "alt-probe")
        r = subprocess.run([sys.executable, MARKER, "uretim-start",
                            "--probe-root", alt],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(r.returncode, 0, r.stderr)
        with open(os.path.join(alt, ".markers", "uretim-start.ts")) as f:
            icerik = f.read().strip()
        self.assertRegex(icerik, r"^\d+$")  # nokta/virgül YOK — tr-TR güvenli

    def test_13_ham_kayit_tablosu(self):  # II.4: marker'lar yerel, kanıt raporda
        r = run_report(self.probe, self.proj, self.xml)
        self.assertEqual(r.returncode, 0, r.stderr)
        m = rapor(self.probe)
        self.assertIn("Marker ham kayıtları", m)
        with open(os.path.join(self.probe, ".markers", "uretim-start.ts")) as f:
            self.assertIn(f.read().strip(), m)

    def test_14_liste_content_ve_pencere(self):  # v1.3.8 / sonda §7.1: ölü sayaç dirildi
        tj = os.path.join(self.probe, "transcript.jsonl")
        yaz_transkript(tj, [
            {"type": "user", "timestamp": "2020-01-01T00:00:00Z",   # pencere ÖNCESİ str
             "message": {"content": "kurulum turunda insan yazisi"}},
            {"type": "user", "timestamp": "2099-01-01T00:00:00Z",   # pencere İÇİ liste+text
             "message": {"content": [{"type": "text", "text": "sonda baslasin"}]}},
            {"type": "user", "timestamp": "2099-01-01T00:00:01Z",   # tool_result → insan DEĞİL
             "message": {"content": [{"type": "tool_result", "content": "ok"}]}},
            {"type": "user",                                        # damgasız → içerde (ihtiyat)
             "message": {"content": [{"type": "text", "text": "not"}]}},
            {"type": "assistant",                                   # sayılmaz
             "message": {"content": [{"type": "text", "text": "ajan"}]}},
        ])
        r = run_report_t(self.probe, self.proj, self.xml, tj)
        m = rapor(self.probe)
        self.assertIn("çapraz kontrol", m)
        self.assertIn("| 2 |", m)           # 2 insan metni: text-liste + damgasız
        self.assertIn("sayım tutarsız", m)  # 2 > kapi(0)+1 → SARI bilgisi
        self.assertEqual(r.returncode, 1)   # SARI

    def test_15_beklenen_yapi_sari_degil(self):  # 1 başlangıç + kapı kadar cevap
        tj = os.path.join(self.probe, "transcript.jsonl")
        yaz_transkript(tj, [
            {"type": "user", "timestamp": "2099-01-01T00:00:00Z",
             "message": {"content": [{"type": "text", "text": "sonda baslasin"}]}},
        ])
        r = run_report_t(self.probe, self.proj, self.xml, tj)
        m = rapor(self.probe)
        self.assertIn("| 1 |", m)
        self.assertNotIn("sayım tutarsız", m)
        self.assertEqual(r.returncode, 0)

    def test_16_pencere_oncesi_dusulur(self):  # kapsam farkı: kurulum turu sızmasın
        tj = os.path.join(self.probe, "transcript.jsonl")
        yaz_transkript(tj, [
            {"type": "user", "timestamp": "2020-01-01T00:00:00Z",
             "message": {"content": "pencere oncesi"}},
        ])
        r = run_report_t(self.probe, self.proj, self.xml, tj)
        m = rapor(self.probe)
        self.assertIn("| 0 |", m)
        self.assertNotIn("sayım tutarsız", m)
        self.assertEqual(r.returncode, 0)


def yaz_transkript(yol, kayitlar):
    with open(yol, "w", encoding="utf-8") as f:
        for k in kayitlar:
            f.write(json.dumps(k, ensure_ascii=False) + "\n")


def run_report_t(probe, proj, xml, transcript):
    return subprocess.run([sys.executable, REPORT, "--probe-root", probe,
                           "--project", proj, "--test-xml", xml,
                           "--transcript", transcript],
                          capture_output=True, text=True, encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
