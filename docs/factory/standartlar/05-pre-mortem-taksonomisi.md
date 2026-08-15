# Pre-mortem taksonomisi — Aşama 2

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** politika maddelerinin kendisi `docs/standards/red-flag.md`'de
(R1–R9), hata ayıklama kategorileri `docs/standards/kod-standardi.md` §9'da, mercek
soruları `docs/standards/gozden-gecirme.md`'de (GG1–GG10), geçmiş dersler
`docs/kor-nokta-analizi.md`'dedir. Bu dosya bunları **tekrarlamaz**; yalnız
"bu oyun nasıl ölür?" sorusunun **kök listesini** ve kayıt biçimini verir.

## Kullanım

Aşama 2'de plan yazılmadan önce koşulur. Her kök için tek satır: **başarısızlık
senaryosu + erken uyarı sinyali + hangi kapının yakalayacağı**. Kapısı olmayan
senaryo, ya kapı önerisine (Sözleşme-5) ya kabul edilmiş riske dönüşür — sessiz
kalamaz.

## Kök listesi

| # | kök | tipik senaryo | yakalayan kapı (tek kaynağı) |
|---|---|---|---|
| T1 | **Ürün** | döngü 60 sn'de anlaşılmıyor, ilk başarı gelmiyor | Aşama 8 rubriği eksen 1–2 (`8.md`) |
| T2 | **Denge** | B3 sayıları tahmin; zorluk eğrisi çöküyor | B8 `denge_sim.py` + değişim kontrolü (`tasarim-standardi.md`) |
| T3 | **Politika** | reklam temposu/karanlık desen/yaş beyanı uyumsuz | R1, R2a/R2b, R4 (`red-flag.md`) |
| T4 | **Teknik** | zamanlama/sıra, durum makinesi varsayımı, referans yaşam döngüsü | kod-standardi §9 üç kategorisi + CI testleri |
| T5 | **Araç zinciri** | build/CI/lisans/paket sürümü kırılması | CI kapıları + `standartlar/FALLBACK.md` |
| T6 | **Ölçüm** | metrik beyana dayanıyor, kapı sessizce yeşil yanıyor | Sözleşme-10 + `ilk-kosu.md` §1 (veri-yok geçti sayılmaz) |
| T7 | **Rotasyon/desen** | defter farkı yetersiz, hesap deseni tekrarlıyor | `appendix/A.md` kuralları + R6 |
| T8 | **İnsan yükü** | kapı kuyruğu tıkanıyor, dönüş süresi taahhüdü aşıyor | `insan-yuku.md` + Ek C `insan_yanit_tavan_*` |
| T9 | **Halka** | kuran sayısı düşük, dış göz yok, kanal ölüyor | `halka-standardi.md` §5–§7 |

## Kayıt biçimi

```
{ kok: T4, senaryo: "...", erken_sinyal: "...", kapi: "CI PlayMode",
  durum: acik | kapatildi | kabul_edilmis_risk, kanit: "..." }
```

## Tekrar taraması

Aşama 2, önceki koşuların pre-mortem kümesini tarar ve **tekrar eden kökü** işaretler
(sayaç kuralı `docs/stages/2.md`'dedir). İlk koşuda küme boştur; bu **VERİ-YOK**'tur ve
kanıtı arşiv dizininin boş-liste çıktısıdır (`ilk-kosu.md` §2) — "tarandı, bulgu yok"
diye geçilmez, satır düşer.

## Sıfır-gerçeklik notu (GG5)

Yeni bir kapı önerisi bu taksonomiden doğuyorsa, önerinin **mevcut gerçekliğe salt-okur
koşulması** ve geçme oranının kaydı gerekir. 0A'da bu ölçüm yapılamadı (V3 VERİ-YOK,
gerekçesi `verification/03`'te) ve kalibrasyon penceresine devredildi.
