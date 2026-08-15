#!/usr/bin/env python3
"""denge_sim.py karar sınırı testleri (v1.4.11 / B8 aracı). stdlib dışı yok.

Koşturma: python3 tools/test_denge_sim.py  (CI: ci/factory-gates.yml arac-testleri)
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
DENGE = os.path.join(HERE, "denge_sim.py")

# B8 kapisinin bekledigi zorunlu B3 hucrelerini kapsayan ornek config (sayilar
# test amacli kasitli ornektir — oyun degeri DEGIL; oyun degerleri sim ciktisiyla
# docs/plan.md B3'e islenir)
CFG = {"sezon_gun_sayisi": 15, "baslangic_stok_adet": 120, "gun_taban_talep": 8,
       "talep_artis_yuzde": 10, "raf_kapasitesi": 3, "tabela_carpani": 1.5}


def kosut(cfg=None, *ek):
    with tempfile.TemporaryDirectory() as d:
        yol = os.path.join(d, "c.json")
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(CFG if cfg is None else cfg, f)
        p = subprocess.run([sys.executable, DENGE, "--config", yol, *ek],
                           capture_output=True, text=True)
    return p


class T(unittest.TestCase):
    def test_deterministik(self):
        a, b = kosut(), kosut()
        self.assertEqual(a.returncode, 0)
        self.assertEqual(a.stdout, b.stdout, "ayni config + tohum => ayni cikti")

    def test_null_alan_sim_bekliyor(self):
        cfg = dict(CFG, gun_taban_talep=None)
        p = kosut(cfg)
        self.assertEqual(p.returncode, 2, "null hucresi VERI-YOK sessiz gecilmez")
        rapor = json.loads(p.stdout)
        self.assertEqual(rapor["durum"], "SIM-BEKLIYOR")
        self.assertIn("gun_taban_talep", rapor["eksik_alanlar"])

    def test_stok_monoton_tamamlanma(self):
        az, cok = dict(CFG, baslangic_stok_adet=40), dict(CFG, baslangic_stok_adet=400)
        pa, pb = kosut(az), kosut(cok)
        ra = json.loads(pa.stdout)["metrikler"]["tamamlanma_orani"]["orta"]
        rb = json.loads(pb.stdout)["metrikler"]["tamamlanma_orani"]["orta"]
        self.assertGreaterEqual(rb, ra, "stok artinca tamamlanma azalmaz")

    def test_sifir_talep_tam_basarim(self):
        p = kosut(dict(CFG, gun_taban_talep=0))
        m = json.loads(p.stdout)["metrikler"]
        self.assertEqual(m["tamamlanma_orani"]["orta"], 1.0)
        self.assertEqual(m["toplam_satis"]["orta"], 0.0)
        self.assertEqual(m["gun_basarisizlik_orani"]["orta"], 0.0)

    def test_artis_monoton_basarisizlik(self):
        dusuk = json.loads(kosut(dict(CFG, talep_artis_yuzde=1)).stdout)
        yuksek = json.loads(kosut(dict(CFG, talep_artis_yuzde=30)).stdout)
        self.assertGreaterEqual(
            yuksek["metrikler"]["gun_basarisizlik_orani"]["orta"],
            dusuk["metrikler"]["gun_basarisizlik_orani"]["orta"],
            "talep artisi yukseldikce basarisiz gun orani azalmaz")

    def test_cikti_dosyasi_sema(self):
        with tempfile.TemporaryDirectory() as d:
            cfg_yol, cikti = os.path.join(d, "c.json"), os.path.join(d, "r.json")
            with open(cfg_yol, "w", encoding="utf-8") as f:
                json.dump(CFG, f)
            p = subprocess.run([sys.executable, DENGE, "--config", cfg_yol,
                                "--seeds", "50", "--tohum", "7", "--cikti", cikti],
                               capture_output=True, text=True)
            self.assertEqual(p.returncode, 0)
            with open(cikti, encoding="utf-8") as f:
                rapor = json.load(f)
        self.assertEqual(rapor["model"], "tezgah-v1")
        self.assertEqual(rapor["seeds"], 50)
        for k in ("tamamlanma_orani", "oynanan_gun", "gun_basarisizlik_orani",
                  "oturum_suresi_sn", "toplam_satis"):
            self.assertIn(k, rapor["metrikler"])
            self.assertIn("p50", rapor["metrikler"][k])


if __name__ == "__main__":
    unittest.main(verbosity=2)
