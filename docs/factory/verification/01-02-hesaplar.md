# 0A / Adım 1 — Mağaza + fatura teyidi

Kanıt biçimi: metin (Sözleşme-4). Görüntü/ham artefakt cihazda kalır; buraya yalnız
`{tarih, kim, sonuç}` satırları girer. Bu dosya public repodadır — hesap kimliği,
uygulama adı, e-posta ve fatura tutarı **girmez** (kural 25).

## Kayıtlar

| tarih (UTC) | kim | konu | sonuç | kanıt türü |
|---|---|---|---|---|
| 2026-08-15 | kullanıcı | Google Play — üretim erişimi | **AÇIK** | doğrulanmış: hesapta kapalı testi geçmiş ve **hâlihazırda üretim aşamasında** bir oyun var |
| 2026-08-15 | kullanıcı | App Store Connect — yeni app kaydı | **AÇIK** | beyan (abonelik aktif, hesap açık) |
| 2026-08-15 | executor | GitHub — Actions/public runner | **AÇIK — ÖLÇÜLDÜ** | 8 gerçek CI koşusu (`factorygames-hello`); ubuntu + macOS runner'lar çalıştı, tahsilat yok |

## Değerlendirme

**Adım 1 geçti.** Hattın takvim varsayımını kilitleyebilecek tek madde Play'in
**12 tester × 14 gün** kapalı test şartıydı: bu şart karşılanmamış olsaydı yeni bir
uygulamada Üretim sekmesi kilitli olur ve ilk fabrika oyunu yayına 14 günden önce
çıkamazdı. Şart **hesap düzeyinde** bir kez karşılanır; hesapta kapalı testi geçmiş ve
üretimde canlı bir oyun bulunması bunu doğrular. Dolayısıyla yeni uygulamalarda üretim
yolu açıktır.

Diğer iki madde kullanıcı **beyanıdır** ve hattı kilitlemez:
- ASC yeni app kaydı: kilitleyici değil — iOS ayağı zaten 0B'de kuruluyor (L3).
- GitHub Actions/public runner: public repo döneminde hosted runner ücretsizdir
  (PIPELINE "CI" kararı); tüketim sayfası ilk gerçek CI koşusundan sonra anlamlı sayı
  taşıyacağı için ölçüm adım 4'te (hello-build) kendiliğinden kanıtlanır.

**Beyan ↔ ölçüm ayrımı:** yukarıdaki tabloda "doğrulanmış" ve "beyan" etiketleri
bilinçlidir; beyan satırları ilk CI koşusuyla ölçüme dönecektir (adım 4 çıktısı bu
dosyaya geri işlenir).

## Actions tüketim ölçümü (adım 4'te kapandı — 2026-08-15)

Adım 1'in bekleyen maddesi. `factorygames-hello` deposunda koşan **8 gerçek CI işinden**
ölçüldü (beyan değil):

```
is       sonuc         sure  runner    carpanli
lint     failure        9 sn  ubuntu       0.1 dk
test     success       28 sn  ubuntu       0.5 dk
test     success       32 sn  ubuntu       0.5 dk
lint     failure        8 sn  ubuntu       0.1 dk
test     success       35 sn  ubuntu       0.6 dk
lint     success        7 sn  ubuntu       0.1 dk
ios      failure       19 sn  macos        3.2 dk
ios      success      408 sn  macos       68.0 dk
TOPLAM   8 kosu      9.1 dk gercek      73.2 dk carpanli
```

**Çıkarım — 0A CI takvimini besleyen iki sayı:**

1. **Public repoda tahsilat yok**; sekiz koşunun tamamı ücretsiz kotada çalıştı
   (PIPELINE "CI" kararı sahada doğrulandı).
2. **macOS çarpanı 10×'tır ve iOS işi pahalıdır:** tek başarılı `ios` koşusu 6.8 dk
   gerçek sürede **68 dk çarpanlı** tüketim demek. Depo ÖLÇEKLE'de private'a çevrilirse
   (PIPELINE "CI" kararının ikinci yarısı) yalnız iOS işi, ücretsiz aylık kotanın büyük
   bölümünü tek koşuda yiyebilir. Ubuntu tarafı (lint + test) toplam **1.9 dk çarpanlı** —
   ihmal edilebilir. Bu, iOS işinin her push'ta değil, **yalnız `workflow_dispatch` ile**
   koşturulması kararını sayısal olarak destekler (mevcut tasarım zaten böyledir).

**Ölçülemeyen (kanıtlı):** hesap düzeyi faturalandırma API'si (`/users/{user}/settings/
billing/actions`) `user` scope istiyor; token'da yok ve **istenmedi** — yetki sınırı
"tam hesap yetkisi istenmez" der (`gh: This API operation needs the "user" scope`).
Tüketim bu yüzden koşu sürelerinden türetildi; yöntem ve ham sayılar yukarıdadır.

## Bekleyen

- ASC yeni app kaydı satırı **beyan** olarak kalıyor: iOS imza zinciri ve ASC anahtarı
  0B'nin konusudur (L3), bu adımda ölçülmedi.
