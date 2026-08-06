# EK C — Kaynak Dosyası Şeması

**Sahibi: kullanıcı.** Hat yalnız ölçer; dosyada olmayan sayı hiçbir kapıda
kullanılamaz; değişiklik yalnız kullanıcı onayıyla. Hat standart akışta yalnız
**Bölüm 1**'i okur. **Bölüm 2**'yi yalnız Aşama 10 yatırım ofisi okur.

**Doldurma protokolü (L8):** kullanıcı TEK form doldurur (0A adım 6); ilk koşudan
önce ölçülemeyecek alanlar "ilk koşuda ölçülecek — şimdilik tahmin" etiketi taşır.
Etiketsiz tahmin YASAK (üç oyun sonra gerçek sanılır); etiket ilk ölçüm gelince
düşer ve eski tahminle ölçüm yan yana not edilir.

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
| `olcekle_arpu_esik` | ÖLÇEKLE tetik: organik AdMob ARPU alt sınırı |
| `d1_kalibrasyon_offset` | Halka D1 düzeltmesi; 3 koşu sonrası, kullanıcı onaylı |
| `iyilestir_hakki` | Konsept başına 1 (Aşama 5) + oyun başına 1 (Aşama 10) |
| `raf_gozden_gecirme_gun` | RAFTA TUT kararının yeniden bakım periyodu |

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
