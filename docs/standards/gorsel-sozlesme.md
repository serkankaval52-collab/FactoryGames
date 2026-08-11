# GÖRSEL SÖZLEŞME — görsel/ses uyumunun ölçülebilir tanımı (v1.0.12, Alan 1)

**İlke (kullanıcı manifestosu):** GÜZELLİK ÖLÇÜLMEZ, UYUM ÖLÇÜLÜR. Model bir
görselin insanı çekip çekmeyeceğini bilemez; bilebildiği, insanların hangi
görsellere "iyi" dediğidir. Bu dosya yargı içermez: her madde ikili veya
sayısal. Tat Aşama 8 rubriğinde kalır; burada vekiller ve tutarlılık kapıları.

**Kaynak-bağımsızlık (köprü pozisyonu — KABUL, iki keskinleştirmeyle):** varlık
CC0'dan gelse, sentezlense, satın alınsa da aynı kapılardan geçer; kaynak yalnız
kapıyı geçmenin MALİYETİNİ değiştirir, kapıyı değil. Keskinleştirme 1: sözleşme
artefaktın uyumunu ölçer; kaynak disiplini (lisans defteri R3, T1 transform
manifesti) ayrı ve üstte durur — buradan geçmek orayı silmez. Keskinleştirme 2:
mekanik vekiller yanılabilir; insan sigortası tek maddede Aşama 8'dedir (G5 beyan
doğruluğu).

**Sayı disiplini:** eşiklerin kaynağı Ek C'dir (Sözleşme-8); bu dosya yapı +
ölçüm yöntemi. Varsayılanlar dış standart/politika sabitidir; kalibrasyon şerhli
olan işaretlidir.

## G1 Palet (CI)

- Oyun başına sabit hex listesi, rollerle: arka plan, ana özne, vurgu, tehlike,
  UI metni, UI zemini. Tek kaynak: `StreamingAssets/palette.json` — Aşama 2'de
  yazılır, sonra değişmez (değişiklik = Sözleşme-5 yükseltme adayı). Renk, kartın
  stil ailesi seçiminden gelir (0A kataloğu).
- Ölçü: tüm texture piksellerinin palete renk uzaklığı; palet dışı piksel oranı
  ≤ Ek C `gorsel_palet_disi_piksel_yuzde` (uzaklık metriği lint içinde tanımlı).

## G2 Sprite geometrisi (CI)

- PPU tutarlılığı: oyundaki tüm sprite'lar tek `pixels-per-unit` değeri
  (manifest alanı). Hedef çözünürlük bandı: ana özne sprite'ları manifest
  bandında.
- Alpha kenar temizliği: kenar hattında yarı-saydam (0<alpha<1) piksel oranı
  ≤ Ek C `gorsel_alpha_sacak_yuzde`.
- Atlas doluluk: paketlenmiş alan / atlas alanı ≥ Ek C `gorsel_atlas_doluluk_yuzde`.
- Kontrol: manifest sayımları + texture taraması — script, insan değil.

## G3 Silüet okunabilirliği (CI; kalibrasyon şerhli)

- Her ana özne 32px'e küçültülür, siyah silüete çevrilir (alpha eşiği); ikili
  fark oranı (farklı piksel yüzdesi) her özne çiftinde ≥ Ek C
  `gorsel_siluet_fark_orani`. Mağaza ikonu aynı testten kendisi geçer — küçük
  ekran ve ikon tek testle kurtulur.
- Şerh: eşik kalibrasyon adayı — ilk 3 koşunun ölçümüyle, kullanıcı onaylı
  güncellenir; o güne dek varsayılan politika sabitidir (uygulanmaz sayılmaz).

## G4 Kontrast (CI — rol renklerinden, piksel taramasız)

- Rol çiftlerinin WCAG göreli-parlaklık oranı: ana özne ↔ arka plan ≥ Ek C
  `gorsel_kontrast_ana_ozne`; UI metin ↔ UI zemin ≥ Ek C `gorsel_kontrast_ui_metin`
  (WCAG AA normal metin); vurgu/tehlike ↔ arka plan ≥ ana-özne eşiği.
- Kontrol: saf hesap — palette.json üzerinden; harici görüntü aracı gerekmez.

## G5 Tutarlılık üçlüsü (CI + Aşama 8 insan)

- Manifest zorunlu alanları (her varlık): perspektif, çizgi kalınlığı bandı,
  gölge yönü (8 yön veya "yok"). Lint: oyun içinde tek değer üçlüsü — "tek tek
  güzel, bir arada dağınık" hatasının mekanik bekçisi.
- BEYANIN DOĞRULUĞU gözle: Aşama 8 ikili bloğunda EVET/HAYIR — "varlıklar beyan
  edilen üçlüye görsel olarak uyuyor mu" (kanıt: Aşama 7 screenshot paketi).
- Bölüşüm: tutarlılık CI'da, doğruluk insanda — ikisi tek kapı gibi sayılmaz.

## S1 Ses sözleşmesi (CI)

- Bütünleşik yükseklik Ek C `ses_lufs_band` içinde; tepe ≤ Ek C `ses_tepe_dbtp`;
  tekil SFX süresi ≤ Ek C `ses_sfx_sure_tavan_sn`; format/örnekleme manifestte
  tek değer. Ölçü: ebur128 (FFmpeg) + dosya taraması, CI'da. Sessizde-oynama
  kuralı tasarim-standardi B6'da kalır (orası kapsam, burası ölçü).

## Kontrol özeti ve kapı bağı

| Madde | Kim denetler | Kapı yuvası |
|---|---|---|
| G1, G2, G3, G4 | CI lint (şablon workflow — 0A adım 3) | Aşama 7 CI kapısının içinde |
| G5 | CI (üçlü tutarlılığı) + İNSAN (beyan doğruluğu) | Aşama 7 + Aşama 8 bloğu |
| S1 | CI (ebur128 + tarama) | Aşama 7 CI kapısının içinde |

**İlk-koşu notu:** bu kapılar ilk koşuda da çalışır — "veri yok" diye sessizce
atlanmaz; gerçekleşen ölçüm rapora düşer, şerhli eşik kullanıcı onayına kadar
varsayılanla uygulanır.
