#!/usr/bin/env python3
"""arac_suzgec.py birim testleri (Sozlesme-5: tavan kurali teste cevrildi, testi kalici)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arac_suzgec import ARACLAR, tara  # noqa: E402

KURULUM_TAM = ("| winget | Git | GitHub CLI | Python 3.12+ | Unity Hub | Unity 6000.3 LTS | "
               "Resmi Unity MCP koprusu | VS Code | FFmpeg | Google Cloud SDK |")


class TestTara(unittest.TestCase):
    def test_temiz_metin_yesil(self):
        metinler = {"docs/stages/7.md": "cihaz kosusu icin `gcloud firebase test` koşulur",
                    "docs/stages/6.md": "S1 olcumu `ffmpeg -af ebur128` ile"}
        self.assertEqual(tara(metinler, KURULUM_TAM), [])

    def test_eksik_arac_kirmizi(self):
        metinler = {"docs/stages/7.md": "cihaz kosusu icin `gcloud firebase test` koşulur"}
        kurulumsuz = "| winget | Git | GitHub CLI | Python | Unity Hub | Unity 6000.3 | MCP |"
        ihlaller = tara(metinler, kurulumsuz)
        self.assertEqual(len(ihlaller), 1)
        self.assertIn("Google Cloud SDK", ihlaller[0])

    def test_birden_cok_dosya_birden_cok_ihlal(self):
        metinler = {"a.md": "`ffmpeg -version`", "b.md": "`gcloud auth list`"}
        ihlaller = tara(metinler, "| winget | Git |")
        self.assertEqual(len(ihlaller), 2)

    def test_gercek_agac_yesil(self):
        """Canli butunlesik test: gercek repo su an kirmizi vermemeli (regresyon bekçisi)."""
        root = Path(__file__).resolve().parents[1]
        kurulum = (root / "docs/stages/kurulum.md").read_text(encoding="utf-8")
        metinler = {}
        hedefler = sorted((root / "docs").rglob("*.md")) + [root / "CLAUDE.md", root / "README.md"]
        for yol in hedefler:
            if yol.name != "kurulum.md":
                metinler[yol.name] = yol.read_text(encoding="utf-8")
        self.assertEqual(tara(metinler, kurulum), [])

    def test_oruntu_sayisi_sabit(self):
        # Oruntu listesi bilincli degisir (Sozlesme-5 kayidi); sessiz buyume korumasi.
        self.assertEqual(len(ARACLAR), 10)


if __name__ == "__main__":
    unittest.main()
