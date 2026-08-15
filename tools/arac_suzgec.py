#!/usr/bin/env python3
"""A1.2 arac suzgeci — normatif agacta adi gecen her aracin kurulum tablosunda
satiri olup olmadigini denetler. ESKI CLAUDE.md kural 30'un teste cevrilmis halidir
(A4.1, v1.0.19): meta kural dosyadan dustu, mekanik bekci burada yasar.
Not: numara 30, v1.0.20'de yeni bir kurala (resmi disi Unity MCP koprusu yasagi)
verildi; bu dosyanin konusu degildir — tarihsel karisiklik notudur, mantik ayni.

Kullanim: python3 tools/arac_suzgec.py  -> ihlal varsa liste + exit 1; yoksa PASS + exit 0.
CI: factory-gates.yml `arac-testleri` isinin adimidir.
"""
import re
import sys
from pathlib import Path

KURULUM_DOSYASI = Path("docs/stages/kurulum.md")

# oruntu -> kurulum arac tablosunda bulunmasi gereken etiket (buyuk/kucuk harf duyarsiz, kelime sinirli)
ARACLAR = [
    (re.compile(r"\bwinget\b"), "winget"),
    (re.compile(r"\bgcloud\b"), "Google Cloud SDK"),
    (re.compile(r"\bffmpeg\b", re.I), "FFmpeg"),
    (re.compile(r"\bgh\s"), "GitHub CLI"),
    (re.compile(r"\bgit\s|\bgit\b"), "Git"),
    (re.compile(r"\bpy -3\.12\b|\bpython3\b|\bpython\.exe\b"), "Python"),
    (re.compile(r"\bUnity\b|Unity\.exe"), "Unity 6000.3"),
    (re.compile(r"Unity Hub|--headless\b"), "Unity Hub"),
    (re.compile(r"\bMCP\b"), "MCP"),
    (re.compile(r"\bcode --version\b"), "VS Code"),
]
# Tablo satiri gerektirmeyenler: isletim sistemi / CI-runner yerlesikleri ve repo-ici scriptler
# (python satiri ustunden kosarlar). Bu liste genisletilirse GEREKCE commit mesajinda yazilir.
YERLESIK = {"robocopy", "powershell", "xcodebuild", "marker.py", "kura.py", "report.py",
            "arac_suzgec.py", "test_kura.py", "test_report.py", "test_arac_suzgec.py",
            "esik_kapsama.py", "test_esik_kapsama.py"}


def tara(metinler, kurulum):
    """metinler: {dosya_adi: icerik}. kurulum: kurulum.md icerigi.
    Donus: ihlal metinleri listesi (bos liste = yesil)."""
    ihlaller = []
    for dosya, icerik in sorted(metinler.items()):
        for oruntu, etiket in ARACLAR:
            if not oruntu.search(icerik):
                continue
            if not re.search(rf"\b{re.escape(etiket)}\b", kurulum, re.I):
                ihlaller.append(f"{dosya}: /{oruntu.pattern}/ geciyor ama kurulum tablosunda '{etiket}' yok")
    return ihlaller


def main():
    root = Path(__file__).resolve().parents[1]
    kurulum = (root / KURULUM_DOSYASI).read_text(encoding="utf-8")
    metinler = {}
    hedefler = sorted((root / "docs").rglob("*.md")) + [root / "CLAUDE.md", root / "README.md"]
    for yol in hedefler:
        if yol.name == "kurulum.md":
            continue  # tablonun kendisi taranmaz
        metinler[str(yol.relative_to(root))] = yol.read_text(encoding="utf-8")
    ihlaller = tara(metinler, kurulum)
    if ihlaller:
        print("A1.2 ARAC SUZGECI — KIRMIZI:")
        for i in ihlaller:
            print(" - " + i)
        print("Talya YOKSA: kapi bu araci kullanamaz; araci kurulum tablosuna ancak insan ekler.")
        return 1
    print(f"A1.2 arac suzgeci YESIL: {len(metinler)} dosya, {len(ARACLAR)} arac oruntusu tarandi; eksik satir yok.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
