#!/usr/bin/env python3
"""FactoryGames denge simulasyonu — B3 sayilarinin TEK KAYNAGI (Sozlesme-2).

Aşama 2 kurali: docs/stages/2.md + docs/standards/tasarim-standardi.md B8 kaynak
denetimi — matematik modeldeki her SAYI bu aracin ciktisi veya gerekceli "simule
edilemez" satiridir; gerekcesiz tahmin Aşama 2'de kirmizidir.

MODEL ("tezgah-v1") — formuller burada yasar, belge alintilar:
  Sezon G gun. Gun g icin ham talep:
      talep_g = Yuvarla( taban * (1 + artis)^(g-1) * (1 + U(-jitter, +jitter)) )
  Tabela o gun kullanildiysa (olasilik tabela_p): talep_g *= tabela_carpani.
  Gunluk satis:
      satis_g = min(talep_g, stok, raf_sayisi * raf_basi_kapasite)
  Karsilanamayan talep > 0 ise gun "basarisiz gun" sayilir (kayip musteri).
  Stok <= 0 ise sezon ERKEN biter (kart A kurali: stok biterse sezon biter).
  Oturum suresi modeli: gun_sayisi * (tur_saniye + ara_saniye); tur 30 sn kart
  eksenidir, sabittir (kura kaydi), sim'e tabi degildir.

Girdi: oyunun config.json'u (B3 hucreleri). Hucresi null/bos olan alan varsa
cikis kodu 2 ve eksik alan listesi — VERI-YOK sessiz gecmez (ilk-kosu disiplini).

Cikti: JSON — parametreler + tohum + seeds + metrikler (ortalama, p10, p50, p90).
Deterministiktir: ayni config + ayni tohum => ayni cikti (rastgelelik yalniz
seed'li random.Random uzerinden, sistem girdisi yok).

Kullanim:
  python3 tools/denge_sim.py --config <config.json> [--seeds 200] [--tohum 42]
      [--cikti <rapor.json>]
Cikis: 0 basari, 1 dosya/ayristirma hatasi, 2 SIM-BEKLIYOR (null girdi var).
"""
import argparse
import json
import random
import sys

# Model ic parametreleri (kapı esigi degildir — Ek C kural 28 kapsami disi;
# her biri belgelenmis motor sabiti, asama-H2 kalibrasyonunda gozden gecer)
MODEL = "tezgah-v1"
TUR_SANIYE = 30.0   # kart A kura ekseni: oturum=30 sn = 1 oyun gunu (sabit)
ARA_SANIYE = 20.0   # gun dongusu disi UI/menu ara suresi (varsayilan; ayarlanabilir alan)
VARSAYILAN = {
    "tabela_p": 0.5,      # oyuncunun bir gunde tabela kullanma olasiligi
    "jitter": 0.15,       # gunluk talep salinim bandi (+-)
}

ZORUNLU_ALANLAR = [
    "sezon_gun_sayisi", "baslangic_stok_adet", "gun_taban_talep",
    "talep_artis_yuzde", "raf_kapasitesi", "tabela_carpani",
]
# Girdiyle ilgisiz/ayri kanit yolu olan B3 hucreleri (sim bu alanlari ISTENMEZ):
#   hedef_*           -> hedef degerler; sim CIKTISI bunlarla kiyaslanir (girdi degil)
#   dogal_reklam_ani_ -> reklam plani kaniti (B5), ekonomi motorunun konusu degil
#   ses_toplam_mb     -> varlik olcumu artefakti (S1 kaniti), sim konusu degil


def yukle(yol):
    try:
        with open(yol, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # pragma: no cover - hata mesaji kanittir
        print(f"HATA: config okunamadi: {e}", file=sys.stderr)
        sys.exit(1)


def cek_alanlar(cfg):
    """Sim girdisi alt kumesini cikar + null/bos alanlari raporla (VERI-YOK)."""
    eksik = [a for a in ZORUNLU_ALANLAR if cfg.get(a) is None]
    return eksik


def kostur(cfg, seeds, tohum):
    g = int(cfg["sezon_gun_sayisi"])
    stok0 = int(cfg["baslangic_stok_adet"])
    t0 = float(cfg["gun_taban_talep"])
    r = float(cfg["talep_artis_yuzde"]) / 100.0  # config'te % yazar: 8 -> 1,08 kat
    raf = int(cfg["raf_kapasitesi"])
    carp = float(cfg["tabela_carpani"])
    raf_basi = float(cfg.get("raf_basi_kapasite", 6))  # gunluk satis/raf (motor sabiti)
    tp = float(cfg.get("tabela_p", VARSAYILAN["tabela_p"]))
    jit = float(cfg.get("jitter", VARSAYILAN["jitter"]))
    ora = float(cfg.get("ara_saniye", ARA_SANIYE))

    tamamlanan, gunler, basarisiz_oranlari, oturum_sn = [], [], [], []
    toplam_satislar = []
    for s in range(seeds):
        rnd = random.Random(tohum * 1000003 + s)  # saltintili int seed: her kosu icin sabit
        stok, tamam, basarisiz_gun, oynanan, toplam_satis = stok0, True, 0, 0, 0
        for gun in range(1, g + 1):
            talep = t0 * (1.0 + r) ** (gun - 1) * (1.0 + rnd.uniform(-jit, jit))
            if rnd.random() < tp:
                talep *= carp
            talep = max(0, round(talep))
            satis = min(talep, stok, raf * raf_basi)
            if talep - satis > 0:
                basarisiz_gun += 1
            stok -= satis
            toplam_satis += satis
            oynanan = gun
            if stok <= 0:
                tamam = False
                break
        tamamlanan.append(1 if tamam else 0)
        gunler.append(oynanan)
        basarisiz_oranlari.append(basarisiz_gun / oynanan)
        oturum_sn.append(oynanan * (TUR_SANIYE + ora))
        toplam_satislar.append(toplam_satis)

    def ozet(x):
        xs = sorted(x)
        k = lambda q: xs[min(len(xs) - 1, max(0, int(q * len(xs))))]
        return {"orta": round(sum(xs) / len(xs), 4),
                "p10": round(k(0.10), 4), "p50": round(k(0.50), 4),
                "p90": round(k(0.90), 4)}

    return {
        "model": MODEL,
        "seeds": seeds, "tohum": tohum,
        "parametreler": {"sezon_gun_sayisi": g, "baslangic_stok_adet": stok0,
                         "gun_taban_talep": t0, "talep_artis_yuzde": r * 100,
                         "raf_kapasitesi": raf, "raf_basi_kapasite": raf_basi,
                         "tabela_carpani": carp, "tabela_p": tp, "jitter": jit,
                         "tur_saniye": TUR_SANIYE, "ara_saniye": ora},
        "metrikler": {
            "tamamlanma_orani": ozet(tamamlanan),
            "oynanan_gun": ozet(gunler),
            "gun_basarisizlik_orani": ozet(basarisiz_oranlari),
            "oturum_suresi_sn": ozet(oturum_sn),
            "toplam_satis": ozet(toplam_satislar),
        },
    }


def main():
    p = argparse.ArgumentParser(description="FactoryGames denge simulasyonu (B8 kaynak araci)")
    p.add_argument("--config", required=True, help="oyun config.json yolu")
    p.add_argument("--seeds", type=int, default=200)
    p.add_argument("--tohum", type=int, default=42)
    p.add_argument("--cikti", default=None, help="JSON rapor dosyasi (yoksa stdout)")
    a = p.parse_args()

    cfg = yukle(a.config)
    eksik = cek_alanlar(cfg)
    if eksik:
        rapor = {"model": MODEL, "durum": "SIM-BEKLIYOR", "eksik_alanlar": eksik}
        print(json.dumps(rapor, ensure_ascii=False, indent=2))
        return 2

    rapor = kostur(cfg, a.seeds, a.tohum)
    metin = json.dumps(rapor, ensure_ascii=False, indent=2)
    if a.cikti:
        with open(a.cikti, "w", encoding="utf-8", newline="\n") as f:
            f.write(metin + "\n")
        print(f"yazildi: {a.cikti}  (seeds={a.seeds}, tohum={a.tohum}, model={MODEL})")
    else:
        print(metin)
    return 0


if __name__ == "__main__":
    sys.exit(main())
