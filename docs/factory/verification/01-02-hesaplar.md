# 0A / Adım 1 — Mağaza + fatura teyidi

Kanıt biçimi: metin (Sözleşme-4). Görüntü/ham artefakt cihazda kalır; buraya yalnız
`{tarih, kim, sonuç}` satırları girer. Bu dosya public repodadır — hesap kimliği,
uygulama adı, e-posta ve fatura tutarı **girmez** (kural 25).

## Kayıtlar

| tarih (UTC) | kim | konu | sonuç | kanıt türü |
|---|---|---|---|---|
| 2026-08-15 | kullanıcı | Google Play — üretim erişimi | **AÇIK** | doğrulanmış: hesapta kapalı testi geçmiş ve **hâlihazırda üretim aşamasında** bir oyun var |
| 2026-08-15 | kullanıcı | App Store Connect — yeni app kaydı | **AÇIK** | beyan (abonelik aktif, hesap açık) |
| 2026-08-15 | kullanıcı | GitHub — hesap + Actions/public runner | **AÇIK** | beyan (hesap aktif) |

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

## Bekleyen

- Adım 4 (hello-build) yeşil olduğunda GitHub Actions tüketim satırı **ölçülmüş**
  kanıta çevrilecek ve bu tablo güncellenecek.
