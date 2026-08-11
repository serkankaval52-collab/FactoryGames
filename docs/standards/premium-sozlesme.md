# PREMIUM SÖZLEŞMESİ — "pahalı his"in ölçülebilir bileşenleri (v1.0.15 — Alan 2)

"Premium" tanımsız hedef değildir: aşağıdaki ikili/sayısal bileşenlerin tamamıdır.
Yargı yok; tat Aşama 8 rubriğinde kalır. Görsel VARLIK kapıları gorsel-sozlesme.md'dedir
(G7) — varlık orada, davranış burada. Eşikler Ek C'dedir (Sözleşme-8).

## Ölçüm yeri (A2.2) — batchmode render ETMEZ

- **Başsız (CI/batchmode):** manifest/lint/mantık kanıtları — P2, P4, P5, P7, P9(a).
  Batchmode'da ekran çıkışı yoktur; kare ve kare-zamanı ÜRETİLEMEZ (H1'in geneli).
- **Cihaz koşusu (Firebase Test Lab, fiziksel cihaz):** render/zaman ölçen her madde —
  P1, P3, P6, P8, P9(b). Ölçümü koşu APK'sının kendisi yapar (uygulama-içi damga kaydı;
  kanıt = logcat + Test Lab çıktısı), Aşama 7'ye özet düşer; ham artefakt cihazda kalır
  (Sözleşme-4).
- **Min-spec tanımsız referans değildir (A2.1):** Ek C `min_spec_cihaz` (somut model +
  RAM + API) + Test Lab karşılığı `min_spec_testlab_pin` (ilk koşuda `gcloud firebase
  test android models list` çıktısından pinlenir). Kullanıcının iPhone 15'i min-spec
  SAYILMAZ (amiral gemisi); iOS kanıtı Aşama 8 insan bloğundadır — 7.md'nin "iOS'lu
  dış göz yoksa pas" kuralı burada da geçerlidir.
- **Kota:** fiziksel koşular Ek C `testlab_gunluk_kota_fiziksel` (koşu/gün, proje
  bazlı) ile sınırlı; taşma sonraki güne ertelenir. Aşmak için ücretli plan = para =
  Sözleşme-8 istisnası — standart akışta YASAK. Aşama 7 geri-kenar turları kotadan düşer.

## P1 Tepki süresi (cihaz koşusu)

- Dokunuştan ilk görsel karşılığa ≤ Ek C `premium_tepki_kare_tavan` kare. Ölçü:
  scripted-input damga çifti (girdi ↔ render değişim karesi), uygulama-içi kayıt +
  Test Lab — batchmode taşıması geri alındı (A2.2).

## P2 Geri bildirim doygunluğu (CI + manifest)

- Oyuncu eylem listesi manifestte; her eylem ≥1 görsel karşılık (işitsel/titreşim
  beyanla). Karşılıksız eylem = 0. Kritik geri bildirim yalnız sese bağlanamaz (B6
  ruhu). Lint: manifest ↔ kod gönderim paritesi (B4 grep-paritesinin kardeşi).

## P3 Geçiş kalitesi (CI liste + cihaz koşusu süre)

- Ekran geçişleri listeli; her geçiş animasyonlu, süresi Ek C `premium_gecis_sure_band`
  içinde; ani kesme = 0. Liste lint'i CI; süre ölçümü cihaz koşusu (A2.2).

## P4 Boş kare yok (CI — sayılabilir durum listesi; A2.6)

- "Her durumda" kör temennisi değil, sayılabilir liste: GDD B2'nin durum sütunu —
  yükleme, izin isteme (ATT/GDPR), ağ hatası, boş içerik, hata; izin diyaloğu açıkken
  arkadaki içerik de tanımlı. Lint listeyi tarar: tanımsız durum = kırmızı.

## P5 Ham hata yok + sessiz toparlanma kaydı (CI + cihaz; A2.5)

- Release oyuncuya ham hata/exception metni göstermez; kilitlenmede sessiz toparlanma
  (önceki kayıttan dönüş). Soak 0 exception'a EK "hata UI'sı yok" kanıtı cihaz koşusu
  karelerinden düşer.
- Her sessiz toparlanma `sessiz_toparlanma` analitik olayı yazar (B4'te zorunlu sabit
  satır). Aşama 10 raporu bu olayı AYRI satırda gösterir: sıfır çökme okuması
  toparlanmaları YUTAMAZ. Oyuncudan gizlenen bizden de gizlenmez.

## P6 Akıcılık (cihaz koşusu — beyan + oran; A2.3)

- Sabit çıta YOK: GDD (B7) hedefi beyan eder — Ek C `premium_kare_hizi_secenek`
  (30/60); bütçe = 1000/hz ms (60 → 16,7). Kapı ikilisi: p95 ≤ bütçe VE p99 − p50 ≤
  bütçe × Ek C `premium_kare_tutarlilik_payi` (varsayılan 1) — düzensiz kare, düşük ama
  sabit kareden kötü hissettirir (takılma). Ölçü: FrameTimingManager, min-spec koşu.

## P7 Hareket imzası (CI)

- Easing seti manifestte sınırlı liste; her animasyon listeden işaretli — G5'in hareket
  karşılığı: tek hareket dili. Liste dışı eğri = lint kırmızı.

## P8 Soğuk açılış bütçesi (cihaz koşusu; kalibrasyon şerhli)

- Soğuk başlangıç → ilk anlamlı kare ≤ Ek C `premium_soguk_acilis_sn` (boot damgaları,
  uygulama-içi kayıt). Şerh: ilk 3 koşuyla kalibre, kullanıcı onaylı; o güne dek
  varsayılan UYGULANIR, atlanmaz.

## P9 Ses gecikmesi (A2.4)

- (a) Yapılandırma (CI — ikili): ses tamponu "en iyi gecikme" tarafında (DSP buffer =
  Best latency; sürümlü presette sabit — elle ayar Sözleşme-2 ihlali). Geç gelen
  işitsel karşılık olmayandan kötüdür.
- (b) Ölçüm (cihaz koşusu): dokunuş damgası → ses başlangıcı ≤ Ek C
  `premium_ses_esik_ms`. O koşuda ölçüm üretilemediyse kapı (a) ile yetinir, rapora
  "gecikme ÖLÇÜLEMEDİ" şerhi düşer (sessiz yeşil yok).

## Kapı bağı

- CI lint (başsız): P2, P4, P5(lint), P7, P9(a). Cihaz koşusu (Test Lab): P1, P3,
  P5(kanıt), P6, P8, P9(b). İlk-koşu notu gorsel-sozlesme ile aynı: şerhli eşikler
  varsayılanla uygulanır; hiçbir kapı "veri yok" diye sessizce atlanmaz.

Köprü listesi P1–P5 alındı; P6–P9 eklenti. Ses eşzamanlılığı, dokunuşun pahalı
hissettirmesinin büyük payıdır.
