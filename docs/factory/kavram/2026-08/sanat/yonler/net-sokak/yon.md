# Sanat yönü — NET-SOKAK

**Oyun:** Tezgâh (0B pilot, kart A) · **Aile:** düz-geometrik · **Aşama:** 3 (çoklu-yön)
**Tuval:** `yon.svg` (1600×1000, tek dosya, gömülü yazı tipi yok)

## 1. Tek cümlelik yön

Beyaz-kâğıt netliğinde bir sokak: her tezgâh bir bakışta okunur, hiçbir piksel
"atmosfer" için harcanmaz.

**Duygu ekseni:** nötr–serin. **Tempo hissi:** ölçülü. **Kalabalık:** yok (4 tezgâh).

## 2. Palet

| rol | hex | kullanım |
|---|---|---|
| arka_plan | `#E8E4DA` | sahne zemini, kart zemini |
| ana_ozne | `#1F4E66` | tezgâh gövdesi üst yüzeyi, birincil şekil |
| vurgu | `#0F7A5A` | tente, etkin durum, birincil eylem |
| tehlike | `#B4341F` | uyarı üçgeni, "stok bitiyor" rozeti |
| ui_metin | `#16202A` | tüm okunur metin |
| yol | `#CFC8BA` | zemin şeridi (dokusuz, tek ton) |
| govde | `#5B7285` | tezgâh yan yüzeyleri (ana_ozne türevi) |
| stok | `#D9A521` | sayılabilir stok küpleri |

Sekiz renk tavan. Gradyan yok; gölge tek koyultma adımıyla üretilir (`govde`
ve sahne-zemin türevleri), ayrı renk sayılmaz.

## 3. Ölçümler (G6 — görsel sözleşme v1.4.1)

Ölçüm aracı: factory.core lint paketindeki `lint_varlik.py` (Brettel/Viénot CVD
yaklaşımı + CIEDE2000). Sıfırdan simülasyon yazılmadı; Machado 2009 matrisleri
kullanılmadı (mimar kararı v1.4.1).

| ölçü | eşik | normal | protanopi | döteranopi | tritanopi | sonuç |
|---|---|---|---|---|---|---|
| tehlike ↔ vurgu ΔE00 | ≥ 2,0 | 56,51 | 48,47 | 62,26 | 48,72 | GEÇER |
| ana_ozne ↔ arka_plan oran | ≥ 3,0 | 7,07 | 9,31 | 10,08 | 5,84 | GEÇER |
| ui_metin ↔ ui_zemin oran | ≥ 4,5 | 12,98 | 13,66 | 13,89 | 11,96 | GEÇER |

En dar pay: tritanopide ana_ozne↔arka oranı 5,84 (eşiğin 1,95 katı).

## 4. Kompozisyon kuralları

- **4 piksel ızgara:** tuvaldeki her koordinat 4'ün katına yuvarlanır (`q()`
  fonksiyonu, üretici script). Yarım piksel kenar ve hizasız kutu yok.
- **Panel düzeni:** ikon (320×320) sol üst, gün-sonu kartı sol alt, oyun sahnesi
  sağ üst (~19,5:9 — en dar telefon en-boyu), palet şeridi sağ alt. Paneller
  birbirine değmez; aralık 24 px.
- **Sahne kırpması:** sahne içeriği `clipPath` ile panel dikdörtgenine kilitlidir
  — taşma yapısal olarak imkânsız, göz denetimine bırakılmaz.
- **İzometrik blok:** üst yüzey eşkenar dörtgen, iki yan yüzey koyultulmuş
  türev. Serbest çizim yok; her blok aynı poligon fonksiyonundan üretilir.
- **Okuma sırası:** en büyük şekil = en önemli karar (tezgâh). Uyarı işareti tek
  ve küçük; ekranda ikiden fazla kırmızı yok.

## 5. Tipografi

Sistem sans (`Segoe UI` / `Inter` / `system-ui` yığını) — dosyaya yazı tipi
gömülmez, lisans yükü taşınmaz. İki kademe: başlık 600 ağırlık, gövde 400.
Sayılar tablo hizalı. Türkçe diyakritikler (ı/İ/ğ/ş/ç/ö/ü/â) tuvalde birebir
kullanıldı ve render denetiminden geçti.

## 6. Yasak-uyum beyanı

`docs/standards/yasak-liste/2026-08.md` on maddesi:

| # | klişe | uyum |
|---|---|---|
| 1 | blok/çizgi-temizleme bulmacası | uyumlu — çünkü ızgara temizleme yok; tezgâh sayısı sabit, hiçbir şey "patlayıp" yerini doldurmuyor. |
| 2 | renk/su sıralama bulmacası | uyumlu — çünkü renk bir sınıflandırma hedefi değil, rol kodu; oyuncu renk taşımıyor. |
| 3 | üçlü eşleştirme (match-3) | uyumlu — çünkü eşleşme mekaniği yok; stok küpleri sayaçtır, birbirine değince bir şey olmaz. |
| 4 | mahjong solitaire | uyumlu — çünkü taş çifti/katman yok; sahne tek düzlemde, açık bilgi. |
| 5 | merge/birleştirme + hikâye | uyumlu — çünkü iki nesne birleşip üçüncüyü doğurmuyor ve anlatı katmanı yok. |
| 6 | ok-kaçış okunur bulmacası | uyumlu — çünkü yön/çıkış bulmacası yok; karar "neyi kime satacağın", uzamsal değil. |
| 7 | sudoku/beyin bulmacası (hayvan kaplamalı) | uyumlu — çünkü kural-çözme ızgarası ve maskot kaplama yok. |
| 8 | şehir/çiftlik kurma (builder) | uyumlu — çünkü kalıcı büyüme/genişleme yok; gün biter, tezgâh sıfırlanır. |
| 9 | endless runner | uyumlu — çünkü otomatik ilerleme ve sonsuz mesafe yok; oyun 30 saniyelik kapalı bir gün. |
| 10 | boyama (dijital renk doldurma) | uyumlu — çünkü palet oyuncuya açık değil; renk bir içerik değil, arayüz. |

**Model-klişe defteri bandı** ("yalnız figür + kaybolmuş/solmuş dünya + hüzünlü
sakinlik"): **girmiyor** — çünkü sahne kalabalık bir sokak günü, dünya kaybolmuş
değil çalışıyor, palet açık ve serin (soluk-nostaljik değil), ton hüzün değil
verimlilik. Yalnız bir figür yok; tezgâhlar çoğul ve müşteri akışı var.

## 7. Risk ve dizginleme

- **Risk:** netlik soğukluğa kayabilir — oyun "tablo" gibi görünüp sıcaklığını
  kaybedebilir. **Dizginleme:** `stok` sarısı yalnız sayılabilir küplerde
  kullanılıyor; sahnedeki tek sıcak nokta o. Genişletilmez.
- **Risk:** düz renkler düşük çözünürlükte yassı durabilir. **Dizginleme:** yan
  yüzey koyultması tek adımda sabit; kontrast ölçümü bu türevle değil ana
  rollerle yapıldığı için eşik payı korunuyor.
- **Bilinen sınır:** ölçüm yalnız palet rolleri arasında koşuldu; sahne içi
  türev tonlar (koyultulmuş yan yüzeyler) G6 kapsamında değil. Aşama 4'te varlık
  üretimi başlarsa bu türevler ayrıca ölçülmeli.
