# GÖRSEL SÖZLEŞME — görsel/ses uyumunun ölçülebilir tanımı (v1.0.13, Alan 1)

**İlke (kullanıcı manifestosu):** GÜZELLİK ÖLÇÜLMEZ, UYUM ÖLÇÜLÜR. Model bir görselin
insanı çekeceğini bilemez; insanların neye "iyi" dediğini bilir. Yargı yok (tat A8'de).

**Kaynak-bağımsızlık (köprü pozisyonu — KABUL, iki keskinleştirme):** varlık CC0/sentez/
satın-alma — aynı kapılar; kaynak kapıyı değil, kapıyı geçmenin maliyetini değiştirir.
(1) Kaynak disiplini (R3 lisans, T1 transform) ayrı ve üstte kalır. (2) Vekiller yanılabilir; insan sigortası Aşama 8'dir (G5 beyanı).
**Saha kaydı (Belge 1 — v1.2):** üretken-3B varlık hattı bütünüyle REDDEDİLDİ (kilit karar URP+2D; ikinci MCP +
araç zinciri = yeni yetki yüzeyi, sıfır karşılık — tekrar açılmaz). Taşınan tek hüküm: üretken-araç çıktısı
kütüphaneye girecek veya rig alacak varlıkta DOĞRUDAN kullanılamaz ("premium için üretken araçlara geç" tezine karşı kayıt).

**Sayı disiplini:** eşikler Ek C'dedir (Sözleşme-8); burada yapı+yöntem; varsayılanlar
dış standart/politika sabiti, kalibrasyon şerhliler işaretli.

## G1 Palet = renk rampası (CI)

- `StreamingAssets/palette.json` (tek kaynak; Aşama 2'de yazılır — değişim Sözleşme-5
  adayı): her rol TABAN hex + sabit kademeli türevler (kademe Ek C `gorsel_palet_kademe`):
  arka plan, ana özne, vurgu, tehlike, UI metin, UI zemin. Kaynak: ailenin ONAYLI sanat
  yönü paketi (`sanat-yonu/<aile>.md`; 0A kataloğu aileyi verir, rengi vermez).
- Ölçü: pikseller rampaya karşı; rampa dışı piksel oranı ≤ Ek C `gorsel_palet_disi_piksel_yuzde`.
  Yarı-saydam pikseller (alpha<1) HARİÇ — kenar yumuşatma G2'nin; yoksa her kenar ihlal (A1.1).

## G2 Sprite geometrisi (CI)

- Tüm sprite'lar tek `pixels-per-unit`; ana özneler manifest çözünürlük bandında; kenar
  yarı-saydam ≤ Ek C `gorsel_alpha_sacak_yuzde`; atlas doluluk ≥ `gorsel_atlas_doluluk_yuzde`.

## G3 Silüet (CI; kalibrasyon şerhli)

- Ayırt edilebilirlik: her ana özne çifti 32px siyah silüette ikili fark oranı ≥ Ek C
  `gorsel_siluet_fark_orani`.
- Okunabilirlik (mutlak, her özne VE ikon): doluluk Ek C `gorsel_siluet_doluluk_band`
  içinde + çeper karmaşıklığı ≥ Ek C `gorsel_siluet_ceper_min` + 32px'te tek parça;
  ikon çift testine GİRMEZ — mutlak testten geçer (A1.5).
- Şerh (sürer): fark eşiği kalibrasyon adayı — ilk 3 koşu kullanıcı onaylı; o güne dek
  varsayılan UYGULANIR, atlanmaz.

## G4 Kontrast (CI — rol renklerinden, piksel taramasız)

- WCAG göreli-parlaklık, rol çiftleri (rol rengi = rampa TABAN hex'i): ana özne ↔ arka
  plan ≥ Ek C `gorsel_kontrast_ana_ozne`; UI metin ↔ UI zemin ≥ `gorsel_kontrast_ui_metin`
  (WCAG AA); vurgu/tehlike ↔ arka plan ≥ ana-özne eşiği. Saf hesap; harici araç yok.
- Şerh (A1.4): oran metin okunabilirliği içindir; özne ayrımında kaba vekildir — asıl güvence G6'dadır.

## G5 Tutarlılık üçlüsü (CI + Aşama 8 insan)

- Manifest zorunlu alanları (değerler sanat yönü paketinden): perspektif, çizgi kalınlığı bandı,
  gölge yönü (8 yön/"yok"); lint oyun içinde tek üçlü ister — dağınıklığın mekanik bekçisi.
- BEYANIN DOĞRULUĞU insanda: Aşama 8 ikili EVET/HAYIR (kanıt: Aşama 7 screenshot paketi).

## G6 Renk körlüğü ayrımı (CI — saf matematik)

- palette.json TABAN rol renkleri üç simülasyondan geçer (protanopi, döteranopi, tritanopi
  — lint içi sabit matrisler); tehlike↔arka plan + ana özne↔arka plan her simülasyonda Ek C
  `gorsel_kontrast_ana_ozne` üstünde (A1.3). Tehlike↔vurgu (sinyal çifti) CIEDE2000 ile ölçülür:
  ΔE00 ≥ 2,0 — normal + 3 simülasyonda da (Şerh (0A-3): CIE literatürü, bakışta-ayrım ≈2; kalibrasyon adayı).
- Ek kural (beyan): renk TEK BAŞINA bilgi taşıyamaz — tehlike/vurgu ayrımı biçim/ikonla
  da desteklenir; ikili satır GDD B2'de yaşar (tasarim-standardi).

## G7 Animasyon varlığı (CI)

- Kare sayısı bandı Ek C `gorsel_anim_kare_band`; döngü işaretlilerde başlangıç↔bitiş
  örtüşmesi ≥ Ek C `gorsel_anim_dongu_ortusme` (dikişsiz döngü).
- Boyut payına ayrı eşik yok: bütçe R8 `uygulama_boyut_tavan_mb` içinde. Davranış (tepki
  gecikmesi, geçiş yumuşaması) premium standardındadır — varlık burada, davranış orada (A1.6).

## G8 Yeniden üretilebilirlik (CI — örneklem; Belge 1/V1)

- Manifest satırı dönüşümü PARAMETRELERİYLE taşır: kaynak dosya hash'i + dönüşüm adı +
  parametre değerleri + araç sürümü — satırdan aynı çıktı yeniden üretilebilir (gerekçe:
  üç ay sonraki palet değişiminde elde sohbet geçmişi değil, çağrı kalır).
- Kapı: her koşuda manifestten örneklem (≥1 varlık) satırdan yeniden üretilir, çıktı hash'i
  karşılaştırılır; uyuşmazlık = kırmızı (tamamı değil, örneklem — Belge 1/V1).

## S1 Ses sözleşmesi (CI)

- Bütünleşik yükseklik Ek C `ses_lufs_band`; tepe ≤ `ses_tepe_dbtp`; tekil SFX ≤ `ses_sfx_sure_tavan_sn`;
  format/örnekleme manifestte tek değer. Ölçü: FFmpeg ebur128 (kurulum satır 10; A1.2). B6 sessizde-oynama kapsamı kalır.

## Kontrol özeti ve kapı bağı

| Madde | Kim denetler | Kapı yuvası |
|---|---|---|
| G1–G4, G6–G8 | CI lint (şablon workflow — 0A adım 3) | Aşama 7 CI kapısı |
| G5 | CI (üçlü tutarlılığı) + İNSAN (doğruluk) | Aşama 7 + Aşama 8 bloğu |
| S1 | CI (FFmpeg ebur128) | Aşama 7 CI kapısı |

**İlk-koşu notu:** kapılar ilk koşuda da çalışır; "veri yok" diye sessizce atlanmaz — şerhli eşikler varsayılanla uygulanır, ölçüm rapora düşer.
