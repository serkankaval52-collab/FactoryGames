#!/usr/bin/env python3
"""Aşama 1 kura zarı — MODEL DIŞI (v1.0.10, M1).

Zar bu script'te atılır; executor çıktı dosyasını okur ve ŞART kabul eder
(docs/stages/1.md ön-adım 2). Havuz tek kaynaktır: docs/standards/havuz.json.
Filtre script içindedir, sırayla:
  1) model-klişe defteri — "## Klişeler" altındaki "- <ad> — ..." satırları;
     dosya yoksa/bölüm boşsa süzgeç boş geçer ve durum çıktıya kaydedilir;
     "bizde doğrulanmadı" etiketli satırlar ZAYIF AĞIRLIKTIR: elemez, yalnız
     çıktıda işaretlenir (şerh, v1.0.11). Bant kontrolü script'in işi değildir —
     yargıdır, karttaki zorunlu beyanda yaşar (model-klise-defteri.md).
  2) o ayın yasak listesi — "- **ad** — ..." satırları (aynı ayrıştırma),
  3) --dolu dosyası — Ek A tavanı dolmuş değerler; satır satır, executor defterden
     derler.
Eşleşme: küçük-harf + boşluk normalize eşitlik, ya da liste adı değerin başlangıcı.
Kalan uzayda herhangi bir eksen boşalırsa çıkış 3: kura YENİDEN ÇEKİLMEZ, hat
durur (Ek A tükenme protokolü) — hata JSON yine --out'a yazılır (kanıt).
Eksik/bozuk girdi: çıkış 2. Başarı: çıkış 0, --out JSON = seçim + filtre çıktısı
+ girdi sha256'larıdır; kart kaydı buradan beslenir.

Varsayılan yollar fabrika klonu köküne göredir; başka yerden koşarken mutlak yol
verin. Rastgelelik secrets modülündendir — tekrarlanabilirlik değil
Denetlenebilirlik hedeflenir (uzay + çıkanlar kayıtlıdır).

Kullanım:
  python3 tools/kura.py --yasak docs/standards/yasak-liste/YYYY-MM.md \
      [--dolu dolu-degerler.txt] --out kura.json
"""
import argparse
import hashlib
import json
import os
import secrets
import sys
from datetime import datetime, timezone


def norm(s):
    return " ".join(str(s).lower().replace("**", "").split())


def sha256(yol):
    with open(yol, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def liste_satirlari(yol):
    """'- **ad** — ...' / '- ad — ...' satırlarından ad listesi çıkar."""
    adlar = []
    with open(yol, encoding="utf-8", errors="replace") as f:
        for ln in f:
            ln = ln.strip()
            if not ln.startswith("- "):
                continue
            govde = ln[2:].strip().replace("**", "")
            ad = govde.split(" — ")[0].split(" —")[0].split("—")[0].strip()
            if ad:
                adlar.append(ad)
    return adlar


def defter_ekseni(defter_yolu):
    """Defterde yalnız '## Klişeler' bölümü süzgece girer (başlık metni değil).
    Dönüş: (güçlü, zayıf, durum). 'bizde doğrulanmadı' etiketli satır ZAYIF
    ağırlıktır: elemez, çıktıda işaretlenir (defter şerhi, v1.0.11)."""
    if not os.path.exists(defter_yolu):
        return [], [], "yok (sıfırıncı sürüm bekleniyor)"
    icerik = []
    bolum = False
    with open(defter_yolu, encoding="utf-8", errors="replace") as f:
        for ln in f:
            if ln.strip().startswith("## "):
                bolum = ln.strip().lower().startswith("## klişeler")
                continue
            if bolum:
                icerik.append(ln)
    if not any(l.strip().startswith("- ") for l in icerik):
        return [], [], "boş (sıfırıncı sürüm bekleniyor)"
    guclu, zayif = [], []
    for ln in icerik:
        ls = ln.strip()
        if not ls.startswith("- "):
            continue
        ad = ls[2:].strip().replace("**", "").split("—")[0].strip()
        if not ad:
            continue
        (zayif if "bizde doğrulanmadı" in norm(ls) else guclu).append(ad)
    return guclu, zayif, f"{len(guclu)} güçlü + {len(zayif)} zayıf"


def liste_satirlari_from_text(metin):
    adlar = []
    for ln in metin.splitlines():
        ln = ln.strip()
        if ln.startswith("- "):
            govde = ln[2:].strip().replace("**", "")
            ad = govde.split("—")[0].strip()
            if ad:
                adlar.append(ad)
    return adlar


def eslesme(deger, adlar):
    nd = norm(deger)
    for ad in adlar:
        na = norm(ad)
        if nd == na or nd.startswith(na) or na.startswith(nd):
            return ad
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--havuz", default="docs/standards/havuz.json")
    ap.add_argument("--yasak", required=True)
    ap.add_argument("--defter", default="docs/standards/model-klise-defteri.md")
    ap.add_argument("--dolu", default=None)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    for yol in (args.havuz, args.yasak):
        if not os.path.exists(yol):
            print(f"girdi eksik: {yol}", file=sys.stderr)
            return 2
    with open(args.havuz, encoding="utf-8") as f:
        havuz = json.load(f).get("eksenler", {})
    eksenler = list(havuz.keys())
    if not eksenler:
        print("havuz boş: eksenler yok", file=sys.stderr)
        return 2

    yasak_adlar = liste_satirlari(args.yasak)
    if not yasak_adlar:
        print(f"yasak listesi ayrıştırılamadı/boş: {args.yasak} "
              "('- **ad** — kanıt' satırları beklenir)", file=sys.stderr)
        return 2
    defter_guclu, defter_zayif, defter_durum = defter_ekseni(args.defter)
    dolu = set()
    if args.dolu:
        if not os.path.exists(args.dolu):
            print(f"girdi eksik: {args.dolu}", file=sys.stderr)
            return 2
        with open(args.dolu, encoding="utf-8", errors="replace") as f:
            dolu = {norm(l) for l in f if l.strip()}

    elenen, filtre_sonrasi = [], {}
    for eksen in eksenler:
        kalan = []
        for deger in havuz[eksen]:
            if eslesme(deger, defter_guclu):
                elenen.append({"eksen": eksen, "deger": deger, "sebep": "defter"})
            elif eslesme(deger, yasak_adlar):
                elenen.append({"eksen": eksen, "deger": deger, "sebep": "yasak"})
            elif norm(deger) in dolu:
                elenen.append({"eksen": eksen, "deger": deger, "sebep": "dolu"})
            else:
                kalan.append(deger)
        filtre_sonrasi[eksen] = kalan

    zayif_eslesme = []
    for eksen in eksenler:
        for deger in filtre_sonrasi[eksen]:
            m = eslesme(deger, defter_zayif)
            if m:
                zayif_eslesme.append({"eksen": eksen, "deger": deger, "satir": m})

    uzay = 1
    for eksen in eksenler:
        uzay *= max(1, len(filtre_sonrasi[eksen]))
    bos = [e for e in eksenler if not filtre_sonrasi[e]]

    sonuc = {
        "arac": "tools/kura.py",
        "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "girdiler": {
            "havuz": {"yol": args.havuz, "sha256": sha256(args.havuz)},
            "yasak": {"yol": args.yasak, "sha256": sha256(args.yasak),
                      "adet": len(yasak_adlar)},
            "defter": {"yol": args.defter, "durum": defter_durum},
            "dolu": {"yol": args.dolu, "adet": len(dolu)} if args.dolu else None,
        },
        "filtre_sonrasi": filtre_sonrasi,
        "elenen": elenen,
        "zayif_defter_eslesmeleri": zayif_eslesme,
        "uzay_boyutu": 0 if bos else uzay,
    }

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    if bos:
        sonuc["hata"] = ("kalan uzay boş — hat durur (Ek A tükenme protokolü); "
                         "kura YENİDEN ÇEKİLMEZ")
        sonuc["bos_eksenler"] = bos
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(sonuc, f, ensure_ascii=False, indent=2)
        print(sonuc["hata"] + f": {bos}", file=sys.stderr)
        return 3

    sonuc["secim"] = {e: secrets.choice(filtre_sonrasi[e]) for e in eksenler}
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=2)
    print(f"ok: {args.out} — seçim: {sonuc['secim']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
