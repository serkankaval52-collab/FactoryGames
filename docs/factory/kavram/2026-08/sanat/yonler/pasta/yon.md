# Sanat yönü — PASTA

**Oyun:** Tezgâh (0B pilot, kart A) · **Aile:** düz-geometrik · **Aşama:** 3 (çoklu-yön)
**Tuval:** `yon.svg` (1600×1000, tek dosya, gömülü yazı tipi yok)

## 1. Tek cümlelik yön

Krem-şeftali bir öğle sonu: dükkân senin, mahalle tanıdık — köşeler yumuşak,
ölçek biraz büyük, hiçbir şey seni azarlamıyor.

**Duygu ekseni:** sıcak–rahat. **Tempo hissi:** yavaş. **Kalabalık:** hafif (5 tezgâh).

## 2. Palet

| rol | hex | kullanım |
|---|---|---|
| arka_plan | `#F5E3CE` | sahne zemini, kart zemini |
| ana_ozne | `#7A4326` | birincil şekil, kart başlığı, birincil düğme |
| vurgu | `#0B6E5F` | tente, etkin durum, ayraç çizgisi |
| tehlike | `#A32B1C` | uyarı üçgeni, "stok bitiyor" rozeti |
| ui_metin | `#3A2417` | tüm okunur metin |
| yol | `#E0C7A8` | zemin şeridi (dokusuz, tek ton) |
| govde | `#C97B3C` | tezgâh gövdesi üst yüzeyi |
| stok | `#D98C2B` | sayılabilir stok küpleri |

Sekiz renk tavan. `govde` ve `stok` bilerek komşu tonlar — sıcaklık bandını
kapatıyorlar; ayrımları biçimden gelir (küp boyutu), renkten değil.

## 3. Ölçümler (G6 — görsel sözleşme v1.4.1)

Ölçüm aracı: factory.core lint paketindeki `lint_varlik.py` (Brettel/Viénot CVD
yaklaşımı + CIEDE2000). Sıfırdan simülasyon yazılmadı; Machado 2009 matrisleri
kullanılmadı (mimar kararı v1.4.1).

| ölçü | eşik | normal | protanopi | döteranopi | tritanopi | sonuç |
|---|---|---|---|---|---|---|
| tehlike ↔ vurgu ΔE00 | ≥ 2,0 | 52,07 | 49,40 | 61,28 | 48,11 | GEÇER |
| ana_ozne ↔ arka_plan oran | ≥ 3,0 | 6,31 | 5,36 | 4,95 | 6,76 | GEÇER |
| ui_metin ↔ ui_zemin oran | ≥ 4,5 | 11,60 | 11,25 | 11,05 | 11,42 | GEÇER |

En dar pay: döteranopide ana_ozne↔arka oranı 4,95 (eşiğin 1,65 katı). Üç yön
içinde en dar payı olan yön budur — sıcak zeminde koyu-kahve özne, kırmızı-yeşil
eksende doğal olarak yaklaşıyor. Palet koyulaştırmadan daha ileri
açıklaştırılmamalı.

## 4. Kompozisyon kuralları

- **4 piksel ızgara:** tuvaldeki her koordinat 4'ün katına yuvarlanır (`q()`
  fonksiyonu, üretici script).
- **Köşe yarıçapı 12 px** — yönü NET-SOKAK'tan ayıran birincil biçim değişkeni.
  Yarıçap ızgaranın katı; keyfi yuvarlama yok.
- **Ölçek çarpanı 1,15** — bloklar NET-SOKAK'a göre bir kademe iri; "el altında"
  hissi buradan gelir.
- **Panel düzeni:** ikon sol üst, gün-sonu kartı sol alt, oyun sahnesi sağ üst
  (~19,5:9), palet şeridi sağ alt. Aralık 24 px, paneller değmez.
- **Sahne kırpması:** `clipPath` ile panel dikdörtgenine kilitli — taşma
  yapısal olarak imkânsız.
- **Okuma sırası:** en büyük şekil = en önemli karar. Uyarı işareti tek.

## 5. Tipografi

Sistem sans (`Segoe UI` / `Inter` / `system-ui` yığını) — dosyaya yazı tipi
gömülmez. İki kademe: başlık 600, gövde 400. Yön yumuşak olduğu için başlık
harf aralığı normal bırakıldı (sıkıştırma yok). Türkçe diyakritikler tuvalde
birebir kullanıldı ve render denetiminden geçti.

## 6. Yasak-uyum beyanı

`docs/standards/yasak-liste/2026-08.md` on maddesi:

| # | klişe | uyum |
|---|---|---|
| 1 | blok/çizgi-temizleme bulmacası | uyumlu — çünkü ızgara temizleme yok; tezgâh sayısı sabit, satır dolup patlamıyor. |
| 2 | renk/su sıralama bulmacası | uyumlu — çünkü renk sınıflandırma hedefi değil; sıcak palet atmosfer, oyun kuralı değil. |
| 3 | üçlü eşleştirme (match-3) | uyumlu — çünkü eşleşme mekaniği yok; stok küpleri yalnızca sayaç. |
| 4 | mahjong solitaire | uyumlu — çünkü taş çifti/katman yok; tüm bilgi tek düzlemde açık. |
| 5 | merge/birleştirme + hikâye | uyumlu — çünkü nesneler birleşip yükselmiyor; "mahalle" bir ton, anlatı katmanı değil. |
| 6 | ok-kaçış okunur bulmacası | uyumlu — çünkü uzamsal çıkış bulmacası yok; karar ticari. |
| 7 | sudoku/beyin bulmacası (hayvan kaplamalı) | uyumlu — çünkü kural-çözme ızgarası ve maskot yok; sahnede tek bir yüz bile yok. |
| 8 | şehir/çiftlik kurma (builder) | uyumlu — çünkü sıcak-mahalle tonu builder çağrışımına en yakın yön budur; ama kalıcı inşa/genişleme yok — gün bitince tezgâh sıfırlanır, hiçbir yapı bir sonraki güne taşınmaz. |
| 9 | endless runner | uyumlu — çünkü otomatik ilerleme yok; oyun 30 saniyelik kapalı bir gün. |
| 10 | boyama (dijital renk doldurma) | uyumlu — çünkü oyuncu renk seçmiyor; palet sabit ve arayüzün parçası. |

**Model-klişe defteri bandı** ("yalnız figür + kaybolmuş/solmuş dünya + hüzünlü
sakinlik"): **girmiyor** — çünkü palet solmuş değil doymuş-sıcak; dünya kaybolmuş
değil, açık ve işleyen bir mahalle. Ton hüzün değil rahatlık; ve figür yalnız
değil — tezgâhlar çoğul, müşteriler dolaşıyor.

**DİKKAT şerhi (açık yargı):** bu yön üç yön içinde banda ve 8. maddeye en yakın
duranıdır — sıcak nostalji paleti "kaybolmuş kasaba" çağrışımını taşıyabilir.
Bandın üç bileşeninden hiçbiri tek başına yeterli değil, ama bu yön seçilirse
Aşama 4'te dizginleme şartı konmalı: sahne her zaman çalışır/kalabalık gösterilir,
boş sokak ve alacakaranlık ışığı üretilmez.

## 7. Risk ve dizginleme

- **Risk:** sıcak palet "rahatlık"tan "uyuşukluk"a kayabilir; oyunun 30 saniyelik
  baskısı görselde okunmaz. **Dizginleme:** tehlike rengi doygun ve koyu tutuldu;
  uyarı rozeti kart içinde sabit konumda, kaçırılamaz.
- **Risk:** `govde`/`stok`/`yol` komşu sıcak tonlar — düşük parlaklıkta ekranda
  birbirine karışabilir. **Dizginleme:** ayrım biçimden geliyor (küp boyutu ve
  konum), renkten değil; renk tek başına bilgi taşımıyor (G4 ilkesi).
- **Bilinen sınır:** ana_ozne↔arka payı döteranopide 4,95 — üç yönün en darı.
  Bu yön seçilirse palet daha fazla açıklaştırılamaz; sıcaklık artırma isteği
  gelirse arka plandan değil, `stok`/`govde` doygunluğundan alınmalı.
