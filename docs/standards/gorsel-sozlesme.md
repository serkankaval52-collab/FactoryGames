# GÖRSEL SÖZLEŞME — görsel/ses uyumunun ölçülebilir tanımı (v1.0.13, Alan 1)

**İlke (kullanıcı manifestosu):** GÜZELLİK ÖLÇÜLMEZ, UYUM ÖLÇÜLÜR. Model bir
görselin insanı çekip çekmeyeceğini bilemez; bilebildiği, insanların hangi
görsellere "iyi" dediğidir. Yargı içeren madde yok; tat Aşama 8 rubriğinde.

**Kaynak-bağımsızlık (köprü pozisyonu — KABUL, iki keskinleştirme):** varlık
CC0/sentez/satın-alma — aynı kapılar; kaynak kapıyı değil, kapıyı geçmenin
maliyetini değiştirir. (1) Sözleşme uyum ölçer; kaynak disiplini (R3 lisans,
T1 transform) ayrı ve üstte kalır. (2) Mekanik vekiller yanılabilir; insan
sigortası tek maddede Aşama 8'dir (G5 doğruluk beyanı).

**Sayı disiplini:** eşikler Ek C'dedir (Sözleşme-8); burada yapı + yöntem.
Varsayılanlar dış standart/politika sabitidir; kalibrasyon şerhli olan işaretli.

## G1 Palet = renk rampası (CI)

- `StreamingAssets/palette.json` (tek kaynak; Aşama 2'de yazılır, sonra
  değişmez — değişim Sözleşme-5 adayı) her rol için TABAN hex + sabit kademeli
  türev varyantları tutar (kademe sayısı Ek C `gorsel_palet_kademe`): arka plan,
  ana özne, vurgu, tehlike, UI metni, UI zemin. Kaynak renk, kartın stil ailesi
  seçiminden gelir (0A kataloğu).
- Ölçü: pikseller rampaya karşı; rampa dışı piksel oranı ≤ Ek C
  `gorsel_palet_disi_piksel_yuzde`. Yarı-saydam pikseller (alpha<1) ölçümden
  HARİÇ — kenar yumuşatma G2'nin konusu; yoksa her kenar palet ihlali sayılırdı
  (A1.1 düzeltmesi: düz liste değil rampa; rampasız kapı ilk koşuda ölürdü).

## G2 Sprite geometrisi (CI)

- Tüm sprite'lar tek `pixels-per-unit`; ana özne sprite'ları manifest
  çözünürlük bandında.
- Kenar hattında yarı-saydam piksel oranı ≤ Ek C `gorsel_alpha_sacak_yuzde`;
  atlas doluluk ≥ Ek C `gorsel_atlas_doluluk_yuzde`.

## G3 Silüet (CI; kalibrasyon şerhli)

- Ayırt edilebilirlik: her ana özne çifti 32px siyah silüette ikili fark oranı
  ≥ Ek C `gorsel_siluet_fark_orani`.
- Okunabilirlik (mutlak, her özne VE ikon): doluluk oranı Ek C
  `gorsel_siluet_doluluk_band` içinde (ince leke de, biçimsiz blok da geçemez) +
  dış çeper karmaşıklığı ≥ Ek C `gorsel_siluet_ceper_min` (düz daire yetmez) +
  32px'te tek parça kalma. İkon çift testine GİRMEZ — mutlak testten geçer (A1.5).
- Şerh (sürer): fark eşiği kalibrasyon adayı — ilk 3 koşu, kullanıcı onaylı;
  o güne dek varsayılan UYGULANIR, atlanmaz.

## G4 Kontrast (CI — rol renklerinden, piksel taramasız)

- WCAG göreli-parlaklık oranı, rol çiftleri (rol rengi = rampanın TABAN hex'i):
  ana özne ↔ arka plan ≥ Ek C `gorsel_kontrast_ana_ozne`; UI metin ↔ UI zemin ≥
  Ek C `gorsel_kontrast_ui_metin` (WCAG AA); vurgu/tehlike ↔ arka plan ≥ ana-özne
  eşiği. Saf hesap; harici görüntü aracı yok.
- Şerh (A1.4): bu oran metin okunabilirliğinin ölçüsüdür; özne ayrımında kaba
  vekildir (zıt tonlar aynı parlaklıkta düşük oran verir). Asıl güvence G6'dadır.

## G5 Tutarlılık üçlüsü (CI + Aşama 8 insan)

- Manifest zorunlu alanları (her varlık): perspektif, çizgi kalınlığı bandı,
  gölge yönü (8 yön veya "yok"); lint oyun içinde tek üçlü ister — "tek tek
  güzel, bir arada dağınık" hatasının mekanik bekçisi.
- BEYANIN DOĞRULUĞU insanda: Aşama 8 ikili EVET/HAYIR (kanıt: Aşama 7
  screenshot paketi).

## G6 Renk körlüğü ayrımı (CI — saf matematik)

- palette.json taban rol renkleri üç simülasyondan geçirilir (protanopi,
  döteranopi, tritanopi — lint içi sabit dönüşüm matrisleri); kritik çiftler
  (tehlike↔vurgu, tehlike↔arka plan, ana özne↔arka plan) her simülasyonda da
  Ek C `gorsel_kontrast_ana_ozne` üstünde kalır. Global hedefin ölçülebilir
  karşılığı (A1.3).
- Ek kural (beyan): renk TEK BAŞINA bilgi taşıyamaz — tehlike/vurgu ayrımı
  biçim/ikonla da desteklenir; ikili satır GDD B2'de yaşar (tasarim-standardi).

## G7 Animasyon varlığı (CI)

- Kare sayısı bandı Ek C `gorsel_anim_kare_band`; döngü işaretlilerde başlangıç↔
  bitiş karesi örtüşmesi ≥ Ek C `gorsel_anim_dongu_ortusme` (dikişsiz döngü).
- Boyut payına ayrı eşik yok: toplam bütçe R8 `uygulama_boyut_tavan_mb` içinde.
- Davranış tarafı (tepki gecikmesi, geçiş yumuşaması) premium standardındadır
  — varlık burada, davranış orada; iki dosya bağlı (A1.6).

## S1 Ses sözleşmesi (CI)

- Bütünleşik yükseklik Ek C `ses_lufs_band`; tepe ≤ Ek C `ses_tepe_dbtp`; tekil
  SFX süresi ≤ Ek C `ses_sfx_sure_tavan_sn`; format/örnekleme manifestte tek
  değer. Ölçü aracı FFmpeg ebur128 — kurulum satır 10 (A1.2). B6 sessizde-oynama
  kapsamında kalır; burası ölçüdür.

## Kontrol özeti ve kapı bağı

| Madde | Kim denetler | Kapı yuvası |
|---|---|---|
| G1–G4, G6, G7 | CI lint (şablon workflow — 0A adım 3) | Aşama 7 CI kapısı |
| G5 | CI (üçlü tutarlılığı) + İNSAN (doğruluk) | Aşama 7 + Aşama 8 bloğu |
| S1 | CI (FFmpeg ebur128) | Aşama 7 CI kapısı |

**İlk-koşu notu:** bu kapılar ilk koşuda da çalışır — "veri yok" diye sessizce
atlanmaz; gerçekleşen ölçüm rapora düşer, şerhli eşikler onaya dek varsayılanla
uygulanır.
