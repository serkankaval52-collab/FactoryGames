#!/usr/bin/env python3
"""Esik kapsama testi — Alan 5 'Kucuk' bulgu (v1.0.21).

Kapsam iddiasi beyan degil CI kanitidir: Ek C Bolum-1'deki her esik/limit alan
adi docs/standards/ilk-kosu.md icinde gecmelidir; eslesmeyen alan kirmizidir.

Kullanim: python3 tools/esik_kapsama.py  -> eksik varsa liste + exit 1; yoksa PASS + exit 0.
CI: factory-gates.yml `arac-testleri` isinin adimidir.
"""
import re
import sys
from pathlib import Path

EKC = Path("docs/appendix/C.md")
ILK_KOSU = Path("docs/standards/ilk-kosu.md")

# Bolum-1 satir bicimi: | `alan_adi` | Anlam |
ALAN_RE = re.compile(r"^\|\s*`([a-z0-9_]+)`\s*\|", re.M)
BOLUM2_RE = re.compile(r"^##\s*Bölüm 2", re.M)


def bolum1_alanlari(ekc_metin):
    """Ek C metninden yalniz Bolum-1 tablosunun alan adlarini cikarir.

    Bolum-2 (istisna/yatirim girdileri) kapsam disidir: standart aks yalniz
    Bolum-1'i okur; kapsam iddiasi da bu alanlar icindir.
    """
    bolum1 = BOLUM2_RE.split(ekc_metin)[0]
    return ALAN_RE.findall(bolum1)


def eksikler(alanlar, ilk_metin):
    """ilk-kosu.md icinde adi gecmeyen alan adlarini dondurur."""
    return [a for a in alanlar if a not in ilk_metin]


def main():
    ekc_metin = EKC.read_text(encoding="utf-8")
    ilk_metin = ILK_KOSU.read_text(encoding="utf-8")
    alanlar = bolum1_alanlari(ekc_metin)
    bulunamayan = eksikler(alanlar, ilk_metin)
    if bulunamayan:
        print(f"ESIK KAPSAMA KIRMIZI: {len(bulunamayan)} alan ilk-kosu.md'de gecmiyor:")
        for a in bulunamayan:
            print(f"  - {a}")
        print("Duzeltme: alani ilgili kapi gerekcesine isle veya VERI-YOK satiri ac.")
        return 1
    print(f"Esik kapsama YESIL: Ek C Bolum-1'deki {len(alanlar)} alanin tamami "
          f"ilk-kosu.md'de geciyor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
