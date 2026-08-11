# İLK-KOŞU STANDARDI — kapıların boş-veri davranışı (Alan 5)

**Kapsam:** ilk oyun koşusu (= 0B pilotu) + kalibrasyon penceresi (ilk 3 koşu; pencere
ilgili eşiğin kullanıcı onaylı yazımıyla kapanır). Başlangıç durumu: çeşitlilik defteri
boş, kalibrasyon dosyası boş, halka tek tur, telemetri tek oyunu kapsıyor, Ek B sayıları
şerhli (eski ürün tanımı), Ek C şerhli alanları "şimdilik tahmin" etiketli.

## 1. İlke: sessiz geçiş yok

İlk koşuda hiçbir kapı SESSİZCE geçmez. Her kapı ya çalışır ya "veri yok, kapı atlandı"
diye rapora düşer; çalışmak iki biçimde olur — toplam üç durum:

- **ÇALIŞTI** — eşik politika sabitidir (Ek C şerh-dışı liste) veya girdi geçmiş veri
  gerektirmez; normal işler, kararı bağlayıcıdır.
- **ŞERHLİ** — kapı koşulur ama eşiği geçicidir (Ek C'de "ilk koşuda ölçülecek — şimdilik
  tahmin" etiketi veya "kalibrasyon adayı — ilk 3 koşu" notu taşıyan alan). Karar
  geçerlidir; satır eşik değeri + "geçici" damgasıyla yazılır. Eşik pencere sonunda revize
  edilirse alınmış karar GERİYE DÖNÜK değişmez; raf edilmiş konsept yeni veriyle Aşama 1'e
  dönebilir (5.md geri kenarı — tek kaynak oradadır, burada tekrarlanmaz).
- **VERİ-YOK** — girdi kümesi boştur; kapı ATLANIR ve satıra "veri yok — kapı atlandı"
  yazılır; bu satır **"kapı geçti" SAYILMAZ**. Mekanik ayrım (köprü kontrolü): telemetri
  `kapi_sonucu` değer kümesi bu dosyayla `{gecti, kaldi, veri_yok}` olur (Sözleşme-1
  şemasına eklenti); ŞERHLİ bir sonuç değildir — `gecti`/`kaldi` satırında `serhli:true`
  işaretidir. Aşama 10 özeti geçti / kaldı / veri-yok sayılarını ÜÇ AYRI sütunda verir.
  VERİ-YOK ile atlamak hat kusuru değildir; satırın tabloda OLMAYIŞI hat kusurudur —
  sessizlik ihlaldir.

## 2. Kapı bazında ilk-koşu davranışı

| Kapı | Durum | Mekanik gerekçe / not |
|---|---|---|
| A1 kura (havuz + filtre) | ÇALIŞTI | filtre boş kümeyle mekanik koşar (defter→yasak→dolu); defter zayıf-ağırlık satırları elemez, çıktıda işaretler (kura semantiği); boş eksen → exit 3 kapısı değişmez |
| A1 yasak listesi | ÇALIŞTI | ön-adım 1 ayın ilk koşusunda arşivi zaten üretir; ilk koşuya özel durum yok |
| A1 rakip 8-eksen tablosu (≥3 fark) | ÇALIŞTI | mağaza araması geçmiş veri gerektirmez; ilk koşudaki bağlayıcı özgünlük ölçüsü budur |
| A1 defter ≥3 eksen farkı (kendi öncekilerimiz) | VERİ-YOK | defter boş; 2. koşudan itibaren tek önceki kartla ÇALIŞTI'ya döner |
| A1 Ek A rotasyonu | ÇALIŞTI | tüm hücreler boş; sıfır-doluluk üzerinden kurallar uygulanır, esnetilemez (eş-konum bedeli) |
| A1 K1–K3 + bant beyanı | ÇALIŞTI | yargı/beyan alanlarıdır, veri gerektirmez |
| A1 yorum hasadı | ÇALIŞTI | "sinyal yok" geçerli sonuçtur (1.md'de yazılı) |
| A2 B1–B7 + grep-paritesi | ÇALIŞTI | dosya lint'i; geçmişe bakmaz |
| A2 pre-mortem tekrar taraması | VERİ-YOK | önceki pre-mortem kümesi boş; boş-küme taraması satır olarak düşer, etiket sayacı bu koşuda başlar (3-koşu kuralı 2.md) |
| A3 envanter / hello-build / sürüm kilidi | ÇALIŞTI | üretim kapısı; tarihsel veri gerektirmez |
| A4 bot 3 döngü / soak / boot imzası / DoD | ÇALIŞTI | ölçüm geçmişe bakmaz; Aşama-4 süre beklentisi Ek B'ye sonda tarafından yazılmıştır — ilk oyun koşusuna hazır gelir (sonda önkoşulu) |
| A5 kurulum hunisi (kanal başına) | ÇALIŞTI | eşik konmaz (halka-std §5): sayılar üretilir; dağılım 3 koşuda kalibre olur |
| A5 küçük-n D1/D2 | ŞERHLİ | ham değer okunur; `d1_kalibrasyon_offset` düzeltmesi VERİ-YOK'tur — ayrı satır düşer, ham kaydedilir |
| A5/D1-2 ENSTRÜMAN YORGUN bayrağı | VERİ-YOK | 2 koşu üst üste düşüş ister; sayaç bu koşuda başlar |
| A5 rotasyon (iki tur dönüşümü) | VERİ-YOK | ilk koşuda tek tur vardır; kural 2. oyundan itibaren bağlar, bu koşuda seçim kısıtsızdır |
| A5 dış-göz metinsizlik testi | ÇALIŞTI | ≥1 dış göz koşulu ilk oyundan geçerlidir; bulunamazsa düşüş şerhi halka-std §7'de yazılı |
| A7 CI lint paketi (G1/G2/G4/G6/G7, S1, P2/P4/P5/P7/P9(a), gömülü-metin, R1/R8/R9) | ÇALIŞTI | eşikler Ek C politika sabitidir (şerh-dışı liste) |
| A7 G3 silüet fark oranı | ŞERHLİ | `gorsel_siluet_fark_orani` kalibrasyon adayı — varsayılanla karar verilir, damgalı yazılır |
| A7 R6 fabrika-içi örtüşme | VERİ-YOK | fabrika envanteri N=1: örtüşme ancak oyunun kendisiyle ölçülür — anlamsız; 2. oyundan itibaren bağlar |
| A7 cihaz koşusu P1/P3/P6 | ÇALIŞTI | ölçüm için pin gereklidir ve ilk koşuda ÜRETİLİR: koşu öncesi `gcloud firebase test android models list` çıktısından kullanıcı onaylı seçim Ek C'ye pinlenir (tek seferlik; insan kapısı sayılır) |
| A7 cihaz koşusu P8 / P9(b) | ŞERHLİ | `premium_soguk_acilis_sn` ve `premium_ses_esik_ms` kalibrasyon adayı — varsayılanla karar, damgalı |
| A8 rubrik (5 veya 3 eksen) | ŞERHLİ | `rubrik_esik` Ek C şerhli alanıdır; dış göz yoksa 3 eksene iniş kuralı zaten yazılı (8.md) |
| A8 R2b / R4 / G5 beyanı | ÇALIŞTI | insan EVET/HAYIR kapısı; veri gerektirmez |
| A9 mağaza gönderimi + organik kit | ÇALIŞTI | `sosyal_video_hakki` tavanı şerhlidir — aşım kararı "geçici tavan" damgasıyla alınır |
| A10 ÖLÇEKLE tetikleri | ŞERHLİ | `organik_indirme_esik`/`organik_d1_esik`/`olcekle_arpu_esik` şerhli alanlar; tetik kararı zaten insanındır |
| A10 Ek B beklenti karşılaştırması | VERİ-YOK | beklenti sütunu şerhli (eski ürün tanımı) → sapma hesaplanmaz; yalnız gerçekleşen kaydedilir — bu koşunun çıktısı Ek B'yi besler |
| A10 büyütme eskalasyonu (2 koşu 0) | VERİ-YOK | arka arkaya 2 koşu ister; tek sayım satırı düşer |
| Sözleşme-3 prose→test dönüşümü | ÇALIŞTI | koşu bağımsız; ilk koşu da ≥1 dönüşüm/silme üretir |
| Geri kenar tur üst sınırları (tüm aşamalar) | ÇALIŞTI | sınırlar ilk koşuda aynen bağlayıcıdır; hepsi insana biter |

Kurulum (-2), sonda (-1) ve 0A bu tablonun dışındadır: tek seferlik aşamalar ilk-koşu
davranışını kendi dosyalarında taşır (sonda karar tablosu "ilk sonda bu eşikleri de
kalibre eder" başlığıyla açık; kurulum kanıt kapısıdır; 0A hat kurulumudur).

## 3. Kalibrasyon penceresi kapanışı (3. koşunun Aşama 10'u)

Tek kullanıcı formuyla (Ek C yazım disiplini — L8 etiketleri düşer, eski tahminle ölçüm
yan yana not edilir): kalibrasyon adayları (`gorsel_siluet_fark_orani`,
`premium_ses_esik_ms`, `premium_soguk_acilis_sn`) ölçülenlerle revize edilir;
`d1_kalibrasyon_offset` ilk değerini alır (medyan fark — yazım 10.md'dedir); Ek B
satırları gerçekleşenlerle baştan yazılır ve ürün-tanımı şerhi düşer; huni dağılımı eşik
ÖNERİSİ üretir — eşik konması zorunlu değildir, "eşiksiz devam" da kayıtlı karardır.
Pencere kapanana dek kalıcı öldürme yoktur (5.md): kalibrasyon verisi birikmeden yapılan
öldürme oyunu değil enstrümanı yargılamış olur.

## 4. Rapor biçimi

Aşama 10 raporu koşu 1–3'te "ilk-koşu şerh tablosu" bloğu taşır: her satır
`{kapı, durum, eşik_değeri (ŞERHLİ ise), not}` — §2 tablosunun o koşudaki gerçekleşen
hâlidir (ör. ÇALIŞTI ilanlı bir kapı o koşuda kırmızıysa satır `kaldi` + `serhli` durumu
taşır; durum sütunu {gecti, kaldi, veri_yok} kümesinden doldurulur). 4. koşudan itibaren
blok düşer; yalnız hâlâ şerhli alan kaldıysa o satırlar kalır.
