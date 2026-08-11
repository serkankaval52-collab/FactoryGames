# EK C — Kaynak Dosyası Şeması

**Sahibi: kullanıcı.** Hat yalnız ölçer; dosyada olmayan sayı hiçbir kapıda
kullanılamaz; değişiklik yalnız kullanıcı onayıyla. Hat standart akışta yalnız
**Bölüm 1**'i okur. **Bölüm 2**'yi yalnız Aşama 10 yatırım ofisi okur.

**Doldurma protokolü (L8):** kullanıcı TEK form doldurur (0A adım 6); ilk koşudan
önce ölçülemeyecek alanlar "ilk koşuda ölçülecek — şimdilik tahmin" etiketi taşır.
Etiketsiz tahmin YASAK (üç oyun sonra gerçek sanılır); etiket ilk ölçüm gelince
düşer ve eski tahminle ölçüm yan yana not edilir.

> **ŞERH (2026-08-06 — ürün tanımı değişikliği):** Bölüm-1'deki takvim/insan-saat/
> halka/pencere ölçekli değerler eski ürün tanımına (hyper-casual) göre
> düşünülmüştür; tasarım standardı + sonda sonrasında kullanıcı tek formda
> günceller (D2 — şimdi yeni sayı yazılmaz). `reklam_*`, `uygulama_boyut_tavan_mb`,
> `ortusme_esik_yuzde`, `gorsel_*`, `ses_*`, `premium_*`, `min_spec_*`, `testlab_*`,
> `ilk_surum_diller`, `ekran_*`, `dokunma_*`
> politika sabitleridir, bu şerhin kapsamı dışındadır.

## Bölüm 1 — Standart tavanlar ve eşikler (her koşuda geçerli)

| Alan | Anlam |
|---|---|
| `takvim_tavan_gun` | Oyun başına azami takvim günü |
| `insan_saat_tavan` | Oyun başına azami insan-saat (yeni ana para birimi) |
| `dis_halka_havuzu` | Dış göz havuz büyüklüğü (kişi) ve tur yapısı |
| `halka_hakki` | Oyun başına azami dış-göz oturumu (tükenebilir kaynak) |
| `sosyal_video_hakki` | Oyun başına azami organik video sayısı/insan-saati (örn. 3) |
| `rubrik_esik` | Aşama 8 eksen bazında asgari puan |
| `olcum_penceresi_gun` | Aşama 10 pencere (örn. 14) |
| `organik_indirme_esik` | ÖLÇEKLE tetik: pencerede asgari organik indirme |
| `organik_d1_esik` | ÖLÇEKLE tetik: organik kohort D1 alt sınırı |
| `olcekle_arpu_esik` | ÖLÇEKLE tetik: organik reklam ARPU alt sınırı (MAX/AdMob) |
| `d1_kalibrasyon_offset` | Halka D1 düzeltmesi; 3 koşu sonrası, kullanıcı onaylı |
| `iyilestir_hakki` | Konsept başına 1 (Aşama 5) + oyun başına 1 (Aşama 10) |
| `raf_gozden_gecirme_gun` | RAFTA TUT kararının yeniden bakım periyodu |
| `reklam_siklik_tavan` | R1: oturum başına azami tam-ekran reklam (varsayılan 3; tür kırılımı aşağıdaki satırda) |
| `reklam_arasi_min_sn` | R1: iki tam-ekran reklam arası asgari saniye (varsayılan 90) |
| `reklam_ilk_gun_sifir_turler` | R1 tür kırılımı: ilk gün (kurulum günü) tam-ekran reklam = 0 olan türler — varsayılan: bulmaca/mantık; kartın `tur` beyanıyla eşleşir, lint denetler (M3) |
| `gorsel_palet_disi_piksel_yuzde` | G1: palet dışı piksel üst sınırı (varsayılan 5) |
| `gorsel_alpha_sacak_yuzde` | G2: sprite kenarında yarı-saydam piksel üst sınırı (varsayılan 2) |
| `gorsel_atlas_doluluk_yuzde` | G2: atlas doluluk alt sınırı (varsayılan 70) |
| `gorsel_siluet_fark_orani` | G3: 32px silüet ikili fark alt sınırı, % (varsayılan 25; kalibrasyon adayı — ilk 3 koşu) |
| `gorsel_kontrast_ana_ozne` | G4: ana özne ↔ arka plan WCAG oran alt sınırı (varsayılan 3.0) |
| `gorsel_kontrast_ui_metin` | G4: UI metin ↔ zemin WCAG AA (varsayılan 4.5) |
| `ses_lufs_band` | S1: bütünleşik yükseklik bandı (varsayılan -16 ± 1 LUFS) |
| `ses_tepe_dbtp` | S1: tepe üst sınırı (varsayılan -1 dBTP) |
| `ses_sfx_sure_tavan_sn` | S1: tekil SFX süre tavanı (varsayılan 2) |
| `gorsel_palet_kademe` | G1: rol başına rampa kademe sayısı (varsayılan 5) |
| `gorsel_siluet_doluluk_band` | G3: 32px silüet doluluk bandı (varsayılan %15–70) |
| `gorsel_siluet_ceper_min` | G3: dış çeper/alan karmaşıklık alt sınırı (varsayılan 0.15) |
| `gorsel_anim_kare_band` | G7: animasyon kare sayısı bandı (varsayılan 4–12) |
| `gorsel_anim_dongu_ortusme` | G7: döngü başlangıç↔bitiş karesi örtüşme alt sınırı, % (varsayılan 90) |
| `premium_tepki_kare_tavan` | P1: dokunuş→ilk görsel karşılık kare tavanı, min-spec (varsayılan 3) |
| `premium_gecis_sure_band` | P3: ekran geçişi süre bandı, ms (varsayılan 150–400) |
| `premium_kare_hizi_secenek` | P6: GDD'nin (B7) beyan ettiği hedef kare hızı — izinli değerler 30 veya 60; kapı bütçesi = 1000/hz ms (60 beyanı 16,7 ms bütçeye tabidir) (A2.3) |
| `premium_kare_tutarlilik_payi` | P6: p99−p50 fark tavanı, hedef bütçenin katı (varsayılan 1; aşım = takılma) (A2.3) |
| `premium_ses_esik_ms` | P9: dokunuş→ses gecikme tavanı, min-spec cihaz koşusu, ms (varsayılan 100; kalibrasyon adayı — ilk 3 koşu) (A2.4) |
| `premium_soguk_acilis_sn` | P8: soğuk açılış→ilk anlamlı kare tavanı, sn (varsayılan 3; kalibrasyon adayı — ilk 3 koşu) |
| `min_spec_cihaz` | P1/P3/P6/P8/P9 ölçüm cihazının TANIMI — referans model: Samsung Galaxy A14 (4 GB RAM, Android 13 / API 33); "düşük seviye" sıfatı değil bu satır ölçüdür (A2.1) |
| `min_spec_testlab_pin` | Test Lab'de koşulacak FİZİKSEL model kimliği: ilk koşuda `gcloud firebase test android models list` çıktısından referansa eş/alt özellikteki model seçilir; kullanıcı onayıyla pinlenir — tek seferlik kilit (kurulum satır 6 disiplininin kardeşi) |
| `testlab_gunluk_kota_fiziksel` | Test Lab fiziksel cihaz koşu kotası, koşu/gün, proje bazlı (Spark planı varsayılan 5; plan değişirse kullanıcı günceller — "şimdilik tahmin" etiketi gerekmez, politika sabitidir) |
| `ilk_surum_diller` | İlk sürüm dilleri (varsayılan: `en, tr`); mağaza listelemesi aynı iki dilde (kullanıcı kararı — A3.6) |
| `ekran_enboy_min` | B7 matrisi en dar oran, uzun/kısa kenar (varsayılan 1,78 ≈ 16:9 — eski telefon tabanı) (A3.7) |
| `ekran_enboy_max` | B7 matrisi en geniş oran (varsayılan 2,33 ≈ 21:9 — üst uç) (A3.7) |
| `ekran_tablet_dahil` | B7: tablet matris kapsamında mı — hayır; telefon dışı form Aşama 10 ölçekleme konusudur (A3.7) |
| `ekran_katlanabilir_dahil` | B7: katlanabilir kapsamda mı — hayır (aynı gerekçe) (A3.7) |
| `ekran_centik_varsayimi` | B7: çentik/delik VAR; arayüz kökleri güvenli alana (Screen.safeArea) oturur — R9'un temeli (A3.7) |
| `dokunma_hedef_min_mm` | B7: asgari dokunma hedefi FİZİKSEL boyutu (varsayılan 9 mm ≈ 48 dp; kaynak: Material Design erişilebilirlik kılavuzu) (A3.7) |
| `ekran_matris_min_hucre` | R9'un test ettiği asgari oran hücresi (varsayılan 3: ~1,78 / ~2,17 / ~2,33; yaygın küme 2,16–2,22 — kaynak: StatCounter mobil çözünürlük dağılımı, 2026-08 taraması) (A3.7) |
| `uygulama_boyut_tavan_mb` | R8: APK/IPA boyut bütçesi |
| `ortusme_esik_yuzde` | R6: fabrika içi varlık/palet örtüşme üst sınırı (%) |

## Bölüm 2 — İstisna girdileri (varsayılan KAPALI; yalnız yatırım ofisi açar)

| Alan | Anlam |
|---|---|
| `istisna_butce_usd` | Varsa ayrılabilecek toplam istisnai yatırım havuzu (0 olabilir) |
| `ua_tavan_usd` | Tek oyuna koşulabilecek azami UA tutarı (yatırım ofisi onayıyla) |
| `ipm_esik`, `ctr_esik` | Standart kapı DEĞİL; yalnız yatırım ofisinin UA analizi kullanır |
| `sinyal_test_butcesi`, `d1_kapi_butcesi` | ARŞİV — G2 ile standart akıştan düştü; yatırım ofisi isterse doldurur |

**Kurallar:**
- Bölüm 2 boşsa (tamamı 0/kapalı) hat eksiksiz çalışır; hiçbir kapı kilitlenmez.
- Oyunlar arası çapraz tanıtım bu hatta tanımlı değildir (kullanıcı kararı);
  hiçbir alan, istisna veya onay bunu açamaz — Sözleşme-8.
- Para içeren her Bölüm-2 kararı tek kullanımlık insan onayına tabidir
  (Sözleşme-8); hat bakiye üzerinden kendiliğinden harcama yapamaz.
