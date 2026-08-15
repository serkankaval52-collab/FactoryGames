# Çeşitlilik defteri — iskelet

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** eksen listesi, rotasyon kuralları, ölüm fiilleri ve havuz
tavanları **burada tanımlanmaz** — tek kaynak `docs/appendix/A.md`. Bu dosya yalnız
**kayıt biçimini** ve **doldurma protokolünü** verir.

## Kayıt biçimi

Her oyun bir satırdır. Sekiz eksen + dört hesap-deseni öğesi `docs/appendix/A.md`
"Eksenler" maddesinde tanımlıdır; buradaki tablo o adları **başlık olarak** kullanır,
tanımlarını tekrarlamaz.

| alan | tip | not |
|---|---|---|
| `oyun_id` | metin | fabrika içi kısa ad |
| `durum` | `canli` \| `raf` \| `magaza_olumu` | iki ölüm fiilinin ayrımı Ek A'dadır |
| `tur`, `cekirdek_mekanik`, `kamera`, `oturum_uzunlugu`, `meta`, `gorsel_stil_ailesi`, `kitle`, `reklam_deseni` | metin | **8 eksen** (Ek A) |
| `ui_kit_ailesi`, `ikon_dili`, `reklam_yerlesim_matrisi`, `menu_akisi` | metin | **hesap-deseni envanteri** 4 öğesi (Ek A) |
| `yayin_tarihi` | tarih | rotasyon soğuma sayacının başlangıcı |
| `kaynak` | `form` \| `olcum` \| `beyan` | menşei etiketi (GG1 disiplini) |

## İlk kayıt — mevcut yayındaki oyun

`docs/appendix/A.md` "Başlangıç durumu": envanter boş başlamaz; kullanıcının yayında
olan oyunu **ilk kayıt** olarak işlenir, tam ağırlıklıdır ve stil/UI/reklam deseni
hücreleri **dolu** kabul edilir.

**Durum: FORM-BEKLIYOR (L8).** Bu satırın 12 alanı kullanıcının 0A adım 6 formundan
gelir (form, 8 eksen + şablon-deseni bloklarını içerir). Form dönene kadar:

```
oyun_id: <FORM-BEKLIYOR>        durum: canli
tur .. reklam_deseni:           <FORM-BEKLIYOR × 8>
ui_kit_ailesi .. menu_akisi:    <FORM-BEKLIYOR × 4>
kaynak: form
```

Alanlar **boş bırakılmaz**, tahminle **doldurulmaz** — etiketsiz tahmin yasaktır
(Ek C doldurma protokolü, L8). Etiket form dönüşüyle düşer ve o gün ölçümle yan yana
not edilir.

## Executor'ın payı

- Defteri **doldurmaz**; formdan gelen değerleri **işler**.
- Fark ölçümünü (≥3 eksen) mekanik yapar ve kanıt tablosunu Aşama 1 kartına ekler.
- Kimlik/kişisel veri buraya **girmez**; defter oyun düzeyindedir.
