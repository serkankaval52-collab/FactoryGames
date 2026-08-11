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
> `ortusme_esik_yuzde`, `gorsel_*`, `ses_*`, `premium_*` politika sabitleridir, bu
> şerhin kapsamı dışındadır.

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
| `premium_kare_p95_ms` | P6: kare süresi p95 tavanı, min-spec, ms (varsayılan 33) |
| `premium_soguk_acilis_sn` | P8: soğuk açılış→ilk anlamlı kare tavanı, sn (varsayılan 3; kalibrasyon adayı — ilk 3 koşu) |
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
