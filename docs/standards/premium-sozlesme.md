# PREMIUM SÖZLEŞMESİ — "pahalı his"in ölçülebilir bileşenleri (v1.0.14, Alan 2)

"Premium" tanımsız hedef değildir: aşağıdaki ikili/sayısal bileşenlerin
tamamıdır. Yargı yok; tat Aşama 8 rubriğinde kalır. Görsel VARLIK kapıları
gorsel-sozlesme.md'dedir (G7) — varlık orada, davranış burada; iki dosya bağlı.
Eşikler Ek C'dedir (Sözleşme-8); kalibrasyon şerhli olan işaretlidir.

## P1 Tepki süresi (Aşama 7 bot)

- Girdiden (dokunuş) ilk görsel karşılığa ≤ Ek C `premium_tepki_kare_tavan`
  kare (min-spec cihaz). Ölçü: scripted-input koşusunda girdi damgası ↔ render
  değişim karesi — Aşama 4 bot standardının uzantısı.

## P2 Geri bildirim doygunluğu (CI + manifest)

- Oyuncu eylem listesi manifestte; her eylem ≥1 görsel karşılık taşır (işitsel
  ve titreşim karşılığı beyanla). Karşılıksız eylem = 0. Kritik geri bildirim
  yalnız sese bağlanamaz (B6 ruhu). Lint: manifest ↔ kod gönderim paritesi
  (B4 grep-paritesinin kardeşi).

## P3 Geçiş kalitesi (manifest + bot)

- Ekran geçişleri listeli; her geçiş animasyonlu ve süresi Ek C
  `premium_gecis_sure_band` içinde; ani kesme = 0 (bot süre ölçümü + manifest
  lint'i).

## P4 Boş kare yok (CI — ikili)

- Yükleme/izin/hata anları dahil her durumda tanımlı içerik bileşeni ekrandadır;
  tanımsız boş durum yoktur. Boot testinin kapsamı.

## P5 Ham hata yok (CI — ikili)

- Release oyuncuya ham hata/exception metni göstermez; kilitlenmede sessiz
  toparlanma (önceki kayıttan dönüş). Bot soak çıktısı 0 exception'a EK "hata
  UI'sı yok" kanıtı taşır.

## P6 Akıcılık (Aşama 7 min-spec raporu)

- Kare süresi p95 ≤ Ek C `premium_kare_p95_ms` (min-spec; bot döngüleri + soak).
  "Çökme 0, exception 0" çıplak tabandır; p95 premium çizgisidir.

## P7 Hareket imzası (CI)

- Easing/zamanlama seti manifestte sınırlı liste; her animasyon listeden birini
  işaretler — G5'in hareket karşılığı: tek hareket dili. Liste dışı eğri =
  lint kırmızı.

## P8 Soğuk açılış bütçesi (Aşama 7; kalibrasyon şerhli)

- Soğuk başlangıç → ilk anlamlı kare ≤ Ek C `premium_soguk_acilis_sn` (min-spec;
  boot zaman damgaları). Şerh: ilk 3 koşuyla kalibre, kullanıcı onaylı; o güne
  dek varsayılan UYGULANIR, atlanmaz.

## Kapı bağı

- P1, P6, P8 → Aşama 7 performans/bot raporu; P2, P4, P5, P7 → CI lint; P3 →
  manifest + bot. İlk-koşu notu gorsel-sozlesme ile aynı: şerhli eşikler
  varsayılanla uygulanır, kapı "veri yok" diye sessizce atlanmaz.

Köprü listesi P1–P5 olarak alındı; P6–P8 eklenti: akıcılık (pahalı hissin en
sessiz bileşeni), hareket imzası (tek el hareket dili), açılış bütçesi.
