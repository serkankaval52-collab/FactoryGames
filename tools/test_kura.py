#!/usr/bin/env python3
"""kura.py karar sınırı testleri (v1.0.10 / M1). stdlib dışı yok.

Koşturma: python3 tools/test_kura.py  (CI: ci/factory-gates.yml arac-testleri)
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
KURA = os.path.join(HERE, "kura.py")

HAVUZ = {"eksenler": {
    "tur": ["alfa", "beta"],
    "kisit": ["k1", "k2", "k3"],
    "kamera": ["kam"],
    "oturum_uzunlugu": ["kisa", "uzun"],
}}


class T(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        d = self._tmp.name
        self.havuz = os.path.join(d, "havuz.json")
        with open(self.havuz, "w", encoding="utf-8") as f:
            json.dump(HAVUZ, f)
        self.yasak = os.path.join(d, "yasak.md")
        self.yaz(self.yasak, ["okuma tarihi", "", "- **bibbit** — kanıt (Play, 3.)"])
        self.defter = os.path.join(d, "defter.md")
        self.yaz(self.defter, ["# defter", "", "## Klişeler", "", "- zorp — gözlem"])
        self.out = os.path.join(d, "kura.json")

    def tearDown(self):
        self._tmp.cleanup()

    def yaz(self, yol, satirlar):
        with open(yol, "w", encoding="utf-8") as f:
            f.write("\n".join(satirlar) + "\n")

    def calistir(self, *ek):
        return subprocess.run([sys.executable, KURA, "--havuz", self.havuz,
                               "--yasak", self.yasak, "--defter", self.defter,
                               "--out", self.out, *ek],
                              capture_output=True, text=True, encoding="utf-8")

    def sonuc(self):
        with open(self.out, encoding="utf-8") as f:
            return json.load(f)

    def test_01_tam_uzay_secim_gecerli(self):
        r = self.calistir()
        self.assertEqual(r.returncode, 0, r.stderr)
        s = self.sonuc()
        self.assertEqual(s["uzay_boyutu"], 2 * 3 * 1 * 2)
        for e, v in s["secim"].items():
            self.assertIn(v, HAVUZ["eksenler"][e])
        self.assertEqual(s["filtre_sonrasi"], HAVUZ["eksenler"])
        self.assertEqual(s["elenen"], [])
        self.assertIn("sha256", s["girdiler"]["havuz"])

    def test_02_yasak_eler(self):
        self.yaz(self.yasak, ["- **beta** — kanıt"])
        r = self.calistir()
        self.assertEqual(r.returncode, 0, r.stderr)
        s = self.sonuc()
        self.assertEqual(s["filtre_sonrasi"]["tur"], ["alfa"])
        self.assertEqual(s["elenen"], [{"eksen": "tur", "deger": "beta", "sebep": "yasak"}])

    def test_03_defter_eler(self):
        self.yaz(self.defter, ["# defter", "## Klişeler", "", "- k2 — gözlem"])
        r = self.calistir()
        self.assertEqual(r.returncode, 0, r.stderr)
        s = self.sonuc()
        self.assertNotIn("k2", s["filtre_sonrasi"]["kisit"])
        self.assertEqual(s["elenen"][0]["sebep"], "defter")

    def test_04_dolu_eler(self):
        dolu = os.path.join(os.path.dirname(self.out), "dolu.txt")
        self.yaz(dolu, ["k1"])
        r = self.calistir("--dolu", dolu)
        self.assertEqual(r.returncode, 0, r.stderr)
        s = self.sonuc()
        self.assertEqual(s["filtre_sonrasi"]["kisit"], ["k2", "k3"])
        self.assertEqual(s["elenen"][0]["sebep"], "dolu")

    def test_05_uzay_bos_hat_durur(self):
        self.yaz(self.yasak, ["- **alfa** — k", "- **beta** — k"])
        r = self.calistir()
        self.assertEqual(r.returncode, 3, r.stderr)
        s = self.sonuc()
        self.assertIn("YENİDEN ÇEKİLMEZ", s["hata"])
        self.assertEqual(s["bos_eksenler"], ["tur"])
        self.assertNotIn("secim", s)

    def test_06_defter_yoksa_suzgec_bos(self):
        os.remove(self.defter)
        r = self.calistir()
        self.assertEqual(r.returncode, 0, r.stderr)
        s = self.sonuc()
        self.assertIn("bekleniyor", s["girdiler"]["defter"]["durum"])

    def test_07_yasak_eksik_girdi_hatasi(self):
        os.remove(self.yasak)
        r = self.calistir()
        self.assertEqual(r.returncode, 2)

    def test_08_yasak_bos_girdi_hatasi(self):
        self.yaz(self.yasak, ["satır ama madde yok"])
        r = self.calistir()
        self.assertEqual(r.returncode, 2)
        self.assertIn("ayrıştırılamadı", r.stderr)

    def test_09_iki_cekim_ikisi_de_gecerli(self):
        for _ in range(2):
            r = self.calistir()
            self.assertEqual(r.returncode, 0, r.stderr)
            s = self.sonuc()
            for e, v in s["secim"].items():
                self.assertIn(v, HAVUZ["eksenler"][e])


if __name__ == "__main__":
    unittest.main(verbosity=2)
