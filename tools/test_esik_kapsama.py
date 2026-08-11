#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_esik_kapsama.py — esik_kapsama.py birim testleri (4 test).

Calistirma (tools/ dizininden): python3 -m unittest test_esik_kapsama
Canli-repo testi kok yolu __file__ uzerinden cozer — herhangi bir cwd'den kosar.
"""
import unittest
from pathlib import Path

from esik_kapsama import bolum1_alanlari, eksikler

ROOT = Path(__file__).resolve().parent.parent
EKC_CANLI = ROOT / "docs/appendix/C.md"
ILK_CANLI = ROOT / "docs/standards/ilk-kosu.md"

EKC_ORNEK = """# EK C

## Bölüm 1 — Standart tavanlar ve eşikler

| Alan | Anlam |
|---|---|
| `alfa_esik` | ... |
| `beta_esik` | ... |

## Bölüm 2 — İstisna girdileri

| `istisna_butce_usd` | kapsam disi |
"""


class TestBolum1Alanlari(unittest.TestCase):
    def test_bolum1_alanlar_cikar(self):
        self.assertEqual(bolum1_alanlari(EKC_ORNEK), ["alfa_esik", "beta_esik"])

    def test_bolum2_atlanir(self):
        self.assertNotIn("istisna_butce_usd", bolum1_alanlari(EKC_ORNEK))


class TestEksikler(unittest.TestCase):
    def test_tam_kapsam_bos_liste(self):
        self.assertEqual(eksikler(["alfa_esik"], "alfa_esik burada geciyor"), [])


class TestCanliRepo(unittest.TestCase):
    def test_gercek_agacta_tam_kapsam(self):
        # kapsam iddiasinin kendisini korur: Ek C'ye alan eklenip ilk-kosu.md'ye
        # islenmezse bu test kirmiziya duser (kor testi degil).
        alanlar = bolum1_alanlari(EKC_CANLI.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(alanlar), 40)  # tablo buyudukce test de buyur
        ilk_metin = ILK_CANLI.read_text(encoding="utf-8")
        self.assertEqual(eksikler(alanlar, ilk_metin), [],
                         "Ek C Bolum-1 alani ilk-kosu.md'de gecmiyor")


if __name__ == "__main__":
    unittest.main()
