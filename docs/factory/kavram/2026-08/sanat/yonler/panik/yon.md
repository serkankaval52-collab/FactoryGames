# Sanat yönü — PANIK

**Oyun:** Tezgâh (0B pilot, kart A) · **Aile:** düz-geometrik · **Aşama:** 3 (çoklu-yön)
**Tuval:** `yon.svg` (1600×1000, tek dosya, gömülü yazı tipi yok)

## 1. Tek cümlelik yön

Bordo karanlıkta asit sarısı bir tezgâh: ekran bağırıyor, saniye sayıyor, el
tezgâhtan çekilmiyor.

**Duygu ekseni:** enerjik–gergin. **Tempo hissi:** hızlı. **Kalabalık:** yoğun (6 tezgâh).

## 2. Palet

| rol | hex | kullanım |
|---|---|---|
| arka_plan | `#2A1620` | sahne zemini, kart zemini (koyu bordo) |
| ana_ozne | `#F2E205` | birincil şekil, kart başlığı, birincil düğme |
| vurgu | `#FF7A00` | tente, etkin durum, ayraç çizgisi |
| tehlike | `#E01E5A` | uyarı üçgeni, "stok bitiyor" rozeti |
| ui_metin | `#FFF3D6` | tüm okunur metin |
| yol | `#43203A` | zemin şeridi (dokusuz, tek ton) |
| govde | `#7B2D4A` | tezgâh gövdesi |
| stok | `#00C2A8` | sayılabilir stok küpleri |

Sekiz renk tavan. Koyu zemin, üç sıcak yüksek-doygunluk rengini aynı anda
taşıyabilmek için seçildi — açık zeminde bu üçlü G6'yı geçmezdi.

## 3. Ölçümler (G6 — görsel sözleşme v1.4.1)

Ölçüm aracı: factory.core lint paketindeki `lint_varlik.py` (Brettel/Viénot CVD
yaklaşımı + CIEDE2000). Sıfırdan simülasyon yazılmadı; Machado 2009 matrisleri
kullanılmadı (mimar kararı v1.4.1).

| ölçü | eşik | normal | protanopi | döteranopi | tritanopi | sonuç |
|---|---|---|---|---|---|---|
| tehlike ↔ vurgu ΔE00 | ≥ 2,0 | 35,37 | 20,32 | 15,59 | **6,15** | GEÇER |
| ana_ozne ↔ arka_plan oran | ≥ 3,0 | 12,69 | 12,64 | 12,54 | 5,36 | GEÇER |
| ui_metin ↔ ui_zemin oran | ≥ 4,5 | 15,43 | 15,14 | 14,92 | 13,58 | GEÇER |

**En dar pay bütün turun en darı:** tritanopide tehlike↔vurgu ΔE00 = 6,15
(eşiğin 3,1 katı, ama diğer iki yönün ~48'ine karşı bir büyüklük mertebesi
altında). Sebep yapısal: turuncu ve magenta-kırmızı mavi-sarı ekseninde
komşudur; tritanopi tam o ekseni çökertir. Eşiği geçiyor, fakat bu yön seçilirse
tehlike/vurgu ayrımı renge yalnız bırakılamaz — biçim eşliği (üçgen vs. tente)
zorunludur ve Aşama 4'te sözleşme notu olarak taşınmalıdır.

## 4. Kompozisyon kuralları

- **4 piksel ızgara:** tuvaldeki her koordinat 4'ün katına yuvarlanır (`q()`
  fonksiyonu, üretici script).
- **Köşe yarıçapı 4 px** — neredeyse keskin; enerji köşeden geliyor.
- **Ölçek çarpanı 1,60** — bloklar üç yönün en irisi. Sahne bilerek doludur;
  kırpma sınırında blok kesilmesi kabul edilir ve "devam eden kalabalık"
  okumasını üretir.
- **Panel düzeni:** ikon sol üst, gün-sonu kartı sol alt, oyun sahnesi sağ üst
  (~19,5:9), palet şeridi sağ alt. Aralık 24 px, paneller değmez.
- **Sahne kırpması:** `clipPath` ile panel dikdörtgenine kilitli — yoğunluk
  yüksek olduğu için taşma riski en çok bu yöndeydi; kısıt yapısal konuldu,
  göz denetimine bırakılmadı.
- **Okuma sırası:** en büyük şekil = en önemli karar. Doygunluk yüksek olduğu
  için ekranda tek `tehlike` işareti kuralı burada daha da katıdır.

## 5. Tipografi

Sistem sans (`Segoe UI` / `Inter` / `system-ui` yığını) — dosyaya yazı tipi
gömülmez. İki kademe: başlık 600, gövde 400. Koyu zeminde ince gövde metni
kaybolduğu için gövde 400'ün altına inmez. Türkçe diyakritikler tuvalde birebir
kullanıldı ve render denetiminden geçti.

## 6. Yasak-uyum beyanı

`docs/standards/yasak-liste/2026-08.md` on maddesi:

| # | klişe | uyum |
|---|---|---|
| 1 | blok/çizgi-temizleme bulmacası | uyumlu — çünkü doygun neon palet o türü çağrıştırsa da ızgara temizleme yok; bloklar patlamıyor, satır dolmuyor. |
| 2 | renk/su sıralama bulmacası | uyumlu — çünkü renk sıralanmıyor; yüksek doygunluk okunurluk aracı, oyun hedefi değil. |
| 3 | üçlü eşleştirme (match-3) | uyumlu — çünkü eşleşme mekaniği yok; stok küpleri sayaç. |
| 4 | mahjong solitaire | uyumlu — çünkü taş çifti/katman yok. |
| 5 | merge/birleştirme + hikâye | uyumlu — çünkü birleşme-yükselme zinciri ve anlatı katmanı yok. |
| 6 | ok-kaçış okunur bulmacası | uyumlu — çünkü uzamsal çıkış bulmacası yok; karar ticari, mekân sabit. |
| 7 | sudoku/beyin bulmacası (hayvan kaplamalı) | uyumlu — çünkü ızgara-kural çözümü ve maskot kaplama yok. |
| 8 | şehir/çiftlik kurma (builder) | uyumlu — çünkü kalıcı büyüme yok; gün bitince tezgâh sıfırlanır. |
| 9 | endless runner | uyumlu — çünkü hız hissi tempo tasarımından geliyor, otomatik ilerleyen sonsuz mesafe yok; gün 30 saniyede kapanır. |
| 10 | boyama (dijital renk doldurma) | uyumlu — çünkü oyuncu renk seçmiyor; palet sabit ve arayüzün parçası. |

**Model-klişe defteri bandı** ("yalnız figür + kaybolmuş/solmuş dünya + hüzünlü
sakinlik"): **girmiyor** — üç bileşenin üçü de yok. Palet solmuş değil azami
doygun; dünya kaybolmuş değil aşırı kalabalık; ton hüzünlü sakinlik değil
gerginlik. Üç yön içinde banda en uzak duran yön budur.

## 7. Risk ve dizginleme

- **Risk (birincil):** yüksek doygunluk uzun oturumda göz yorar; 30 saniyelik
  gün için doğru, 20 dakikalık seans için yanlış olabilir. **Dizginleme:** doygun
  renkler yalnız küçük alanlarda (tente, stok, uyarı); alanın çoğunluğu koyu
  bordo zemin ve düşük-doygunluk gövde. Oran korunmalı.
- **Risk:** koyu zemin + neon "arcade/neon" klişesine kayabilir — yasak listede
  bir madde değil ama tanıdıklık riski. **Dizginleme:** parıltı, dış-ışıma
  (glow), tarama çizgisi ve krom yok; biçimler düz ve mat kalır.
- **Risk:** tritanopide tehlike↔vurgu payı dar (6,15). **Dizginleme:** ayrım
  renge yalnız bırakılmaz — tehlike her zaman üçgen, vurgu her zaman yatay
  tente; biçim tek başına yeterlidir.
- **Bilinen sınır:** ölçüm yalnız palet rolleri arasında koşuldu; sahne içi
  türev tonlar G6 kapsamında değil. Bu yön seçilirse türevler ayrıca ölçülmeli,
  çünkü koyu zeminde türev farkları hızla eşiğin altına iner.
