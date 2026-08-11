# İLK-KOŞU STANDARDI — kapıların boş-veri davranışı (Alan 5)

**Kapsam:** ilk oyun koşusu (= 0B pilotu) + kalibrasyon penceresi (ilk 3 koşu; pencere
ilgili eşiğin kullanıcı onaylı yazımıyla kapanır). Başlangıç durumu: defter + Ek A envanterinde
TEK kayıt işli (mevcut yayında oyun; dolu hücreler tam ağırlıklıdır), kalibrasyon boş, halka
tek tur, telemetri tek oyun; Ek B şerhli, Ek C şerhli alanları "şimdilik tahmin" etiketli.

## 1. İlke: sessiz geçiş yok

İlk koşuda hiçbir kapı SESSİZCE geçmez. Her kapı ya çalışır ya "veri yok, kapı atlandı"
diye rapora düşer; çalışmak iki biçimde olur — toplam üç durum:

- **ÇALIŞTI** — eşik politika sabitidir (Ek C şerh-dışı liste) veya girdi geçmiş veri
  gerektirmez; normal işler, kararı bağlayıcıdır.
- **ŞERHLİ** — kapı koşulur ama eşiği geçicidir (Ek C'de "ilk koşuda ölçülecek — şimdilik
  tahmin" etiketi veya "kalibrasyon adayı — ilk 3 koşu" notu taşıyan alan). Karar
  geçerlidir; satır eşik değeri + "geçici" damgasıyla yazılır. Eşik pencere sonunda revize
  edilirse karar GERİYE DÖNÜK değişmez; raf konsepti yeni veriyle Aşama 1'e döner (5.md — tek kaynak orada).
- **VERİ-YOK** — girdi kümesi boştur; kapı ATLANIR ve satıra "veri yok — kapı atlandı"
  yazılır; bu satır **"kapı geçti" SAYILMAZ**. Mekanik ayrım: telemetri `kapi_sonucu`
  değer kümesi `{gecti, kaldi, veri_yok}`'tur (Sözleşme-1 şemasına bu dosyayla eklenti);
  ŞERHLİ sonuç değildir — `gecti`/`kaldi` satırında `serhli:true` işaretidir. Aşama 10
  özeti geçti / kaldı / veri-yok'u üç ayrı sütunda sayar. VERİ-YOK beyan değildir — KANIT
  ister (Sözleşme-10'un bu tabloya uygulanması, A5.2): satır boş girdinin ARTEFAKTINI
  taşır — boş dosyanın yolu + boyutu, sıfır uzunluklu listenin komut çıktısı veya okunan
  kaynağın yokluğunu gösteren komut çıktısı. Kanıtsız VERİ-YOK, satırın yokluğu kadar ihlaldir.

## 2. Kapı bazında ilk-koşu davranışı

| Kapı | Durum | Mekanik gerekçe / not |
|---|---|---|
| A1 kura (havuz + filtre) | ÇALIŞTI | filtre boş kümeyle mekanik koşar (defter→yasak→dolu); defter zayıf-ağırlık satırları elemez, çıktıda işaretler (kura semantiği); boş eksen → exit 3 kapısı değişmez |
| A1 yasak listesi | ÇALIŞTI | ön-adım 1 ayın ilk koşusunda arşivi zaten üretir; ilk koşuya özel durum yok |
| A1 rakip 8-eksen tablosu (≥3 fark) | ÇALIŞTI | mağaza araması geçmiş veri gerektirmez; ilk koşudaki bağlayıcı özgünlük ölçüsü budur |
| A1 defter ≥3 eksen farkı | ÇALIŞTI | defter tek kayıtlı ama BOŞ DEĞİL (A5.1): mevcut oyun 0A-6 formuyla (8 eksen) işlidir — fark bu kayda karşı ölçülür |
| A1 Ek A rotasyonu | ÇALIŞTI | tek-doluluk (A5.1): mevcut oyun ilk kayıt, tam ağırlıklı (Ek A başlangıç durumu); stil ailesi / UI kiti / ikon dili+baskın rengi / reklam yerleşim matrisi / menü akışı hücreleri DOLU — ilk fabrika oyunu bu hücrelerden kaçınır; esnetilemez (eş-konum bedeli) |
| A1 K1–K3 + bant beyanı | ÇALIŞTI | yargı/beyan alanlarıdır, veri gerektirmez |
| A1 yorum hasadı | ÇALIŞTI | "sinyal yok" geçerli sonuçtur (1.md'de yazılı) |
| A2 B1–B7 + grep-paritesi | ÇALIŞTI | dosya lint'i; geçmişe bakmaz |
| A2 pre-mortem tekrar taraması | VERİ-YOK | önceki pre-mortem kümesi boş (kanıt: arşiv dizininin boş-liste çıktısı); boş-küme taraması satır düşer, etiket sayacı başlar (3-koşu kuralı 2.md) |
| A3 envanter / hello-build / sürüm kilidi | ÇALIŞTI | üretim kapısı; `ilk_surum_diller` (EN+TR) paketleme disiplini bu aşamada kurulur |
| A4 bot 3 döngü / soak / boot imzası / DoD | ÇALIŞTI | ölçüm geçmişe bakmaz; Aşama-4 süre beklentisi Ek B'ye sonda tarafından yazılmıştır — ilk oyun koşusuna hazır gelir (sonda önkoşulu) |
| A5 kurulum hunisi (kanal başına) | ÇALIŞTI | eşik konmaz (halka-std §5): sayılar üretilir, dağılım 3 koşuda kalibre olur; halka ölçekleri `dis_halka_havuzu`/`halka_hakki` şerhli zamanlanır (kayıt olarak yazılır) |
| A5 küçük-n D1/D2 | ŞERHLİ | ham değer okunur; `d1_kalibrasyon_offset` düzeltmesi VERİ-YOK'tur — ayrı satır düşer (kanıt: kalibrasyon dosyasının yokluğu), ham kaydedilir |
| A5/D1-2 ENSTRÜMAN YORGUN bayrağı | VERİ-YOK | 2 koşu üst üste düşüş ister; sayaç bu koşuda başlar (kanıt: telemetri dosyasında tek koşu) |
| A5 rotasyon (iki tur dönüşümü) | VERİ-YOK | ilk koşuda tek tur vardır (kanıt: envanterin tek-tur çıktısı); kural 2. oyundan itibaren bağlar |
| A5 dış-göz metinsizlik testi | ÇALIŞTI | ≥1 dış göz koşulu ilk oyundan geçerlidir; bulunamazsa düşüş şerhi halka-std §7'de yazılı |
| A7 CI lint paketi | ÇALIŞTI | eşikler politika sabiti (şerh-dışı): G1/G2/G4/G6/G7 + S1 + P2/P4/P5/P7/P9(a) + gömülü-metin — `gorsel_palet_disi_piksel_yuzde`, `gorsel_alpha_sacak_yuzde`, `gorsel_atlas_doluluk_yuzde`, `gorsel_kontrast_ana_ozne`, `gorsel_kontrast_ui_metin`, `gorsel_palet_kademe`, `gorsel_anim_kare_band`, `gorsel_anim_dongu_ortusme`, `ses_lufs_band`, `ses_tepe_dbtp`, `ses_sfx_sure_tavan_sn`, `premium_tepki_kare_tavan` (P1 üst sınırı cihazda), `premium_gecis_sure_band`, `premium_kare_hizi_secenek`, `premium_kare_tutarlilik_payi`; R1 `reklam_siklik_tavan`/`reklam_arasi_min_sn`/`reklam_ilk_gun_sifir_turler`, R8 `uygulama_boyut_tavan_mb`, R9 `ekran_matris_min_hucre`+`ekran_centik_varsayimi`; B7 sabitleri `ekran_enboy_min`/`ekran_enboy_max`/`ekran_tablet_dahil`/`ekran_katlanabilir_dahil`/`dokunma_hedef_min_mm` |
| A7 G3 silüet üçlüsü | KARIŞIK | `gorsel_siluet_fark_orani` kalibrasyon adayı → ŞERHLİ (varsayılanla karar, damgalı); `gorsel_siluet_doluluk_band` + `gorsel_siluet_ceper_min` politika sabiti → ÇALIŞTI |
| A7 R6 varlık-hash örtüşmesi (`ortusme_esik_yuzde`) | VERİ-YOK | mevcut oyunun varlıkları hash'lenemez (yayında; kaynağa erişim yetki sınırı + K4 dışı); fabrika varlık envanteri N=1 (kanıt: envanter scriptinin sıfır-hash çıktısı) |
| A7 R6 palet/UI eşleşmesi (aynı eşik) | ÇALIŞTI | palet / UI kiti / ikon dili / reklam yerleşimi karşılaştırması 0A-6 formundan gelir (A5.1) — mevcut oyuna karşı ilk koşuda ölçülür; eş-konum kapısı ilk koşuda AÇIKTIR |
| A7 cihaz koşusu P1/P3/P6 | ÇALIŞTI | ölçü `min_spec_cihaz` satırıdır; pin ilk koşuda ÜRETİLİR — `min_spec_testlab_pin`: gcloud models-list çıktısından kullanıcı onaylı seçim Ek C'ye pinlenir (tek seferlik; insan kapısı sayılır); her koşu `testlab_gunluk_kota_fiziksel` kotasından düşer |
| A7 cihaz koşusu P8 / P9(b) | ŞERHLİ | `premium_soguk_acilis_sn` ve `premium_ses_esik_ms` kalibrasyon adayı — varsayılanla karar, damgalı yazılır |
| A8 rubrik (5 veya 3 eksen) | ŞERHLİ | `rubrik_esik` Ek C şerhli alanıdır; dış göz yoksa 3 eksene iniş kuralı zaten yazılı (8.md) |
| A8 R2b / R4 / G5 beyanı | ÇALIŞTI | insan EVET/HAYIR kapısı; veri gerektirmez |
| A8 insan-yargısı öldürmesi (A5.3) | ÇALIŞTI — kilide tabi değil | kullanıcı oyunu gerçekten oynar; açık "bu kötü" kararı her koşuda bağlayıcıdır; öldürülen oyunun rubrik puanları `rubrik_esik` yerleşiminin kalibrasyon verisidir |
| İnsan taahhüt alanları (A6.1/A6.4) | ÇALIŞTI | `insan_yanit_tavan_rubrik_gun`, `insan_yanit_tavan_t3_gun`, `insan_yanit_tavan_magaza_form_gun`, `insan_yanit_tavan_karar_gun` kullanıcının 0A-6 taahhüdünden gelir (ölçüm değil); aşım kapıyı DURDURMAZ — A10 hat bakımına satır düşer. `halka_davet_tavan_gun` dolarsa A5 eldeki N ile devam eder (N rapora, şerhli) |
| A9 mağaza gönderimi + organik kit | ÇALIŞTI | `sosyal_video_hakki` tavanı şerhlidir — aşım kararı "geçici tavan" damgasıyla alınır |
| A10 ÖLÇEKLE tetikleri + pencere | ŞERHLİ | `organik_indirme_esik`/`organik_d1_esik`/`olcekle_arpu_esik`/`olcum_penceresi_gun` şerhli alanlar; tetik kararı zaten insanındır |
| A10 Ek B karşılaştırması + tavanlar | VERİ-YOK | beklenti sütunu şerhli (eski ürün tanımı) → sapma hesaplanmaz (kanıt: Ek B şerh satırı); yalnız gerçekleşen kaydedilir — bu koşu Ek B'yi besler; `takvim_tavan_gun`/`insan_saat_tavan` uygulaması ŞERHLİ damgalı okunur |
| A10 büyütme eskalasyonu (2 koşu 0) | VERİ-YOK | arka arkaya 2 koşu ister (kanıt: tek koşuluk halka kaydı); tek sayım satırı düşer |
| Sözleşme-3 prose→test dönüşümü | ÇALIŞTI | koşu bağımsız; ilk koşu da ≥1 dönüşüm/silme üretir |
| Geri kenar tur üst sınırları (tüm aşamalar) | ÇALIŞTI | sınırlar ilk koşuda aynen bağlayıcıdır; hepsi insana biter |

Kurulum (-2), sonda (-1), 0A tablo dışı: ilk-koşu davranışları kendi dosyalarındadır (sonda
"ilk sonda eşikleri kalibre eder"; kurulum kanıt kapısı; 0A hat kurulumu).

## 3. Kalibrasyon penceresi kapanışı (3. koşunun Aşama 10'u)

Tek kullanıcı formuyla (Ek C yazım disiplini — L8 etiketleri düşer, eski tahminle ölçüm
yan yana not edilir): kalibrasyon adayları (`gorsel_siluet_fark_orani`,
`premium_ses_esik_ms`, `premium_soguk_acilis_sn`) ölçülenlerle revize edilir;
`d1_kalibrasyon_offset` ilk değerini alır (medyan fark — yazım 10.md'dedir);
kullanıcının öldürdüğü oyunların rubrik puanları `rubrik_esik` önerisine girdi olur
(A5.3); Ek B satırları gerçekleşenlerle baştan yazılır ve şerhi düşer; huni dağılımı eşik
ÖNERİSİ üretir ("eşiksiz devam" da kayıtlı karardır).
Sayaç sabitleri `iyilestir_hakki` ve `raf_gozden_gecirme_gun` ilk koşuda ÇALIŞTI sayılır
(biri sıfırdan başlar, öteki takvime yazılır) — kapanış formunun konusu değildir.
Öldürme kilidi yalnız METRİK kaynaklı kalıcı öldürmeyi kapsar (A5.3; tek kaynak 5.md):
kalibrasyonsuz sayıyla öldürme oyunu değil enstrümanı yargılar; insan yargısı kilide tabi
değildir — metrik kalibrasyonsuz olabilir, insan yargısı değildir.

## 4. Rapor biçimi

Aşama 10 raporu koşu 1–3'te "ilk-koşu şerh tablosu" bloğu taşır: her satır
`{kapı, durum, eşik_değeri (ŞERHLİ ise), kanıt (VERİ-YOK ise zorunlu artefakt yolu/çıktısı),
not}` — §2 tablosunun o koşudaki gerçekleşen hâlidir; durum sütunu {gecti, kaldi, veri_yok}
kümesinden dolar (ör. ÇALIŞTI ilanlı kapı kırmızıysa `kaldi` + `serhli` taşır). 4. koşudan
itibaren blok düşer; yalnız hâlâ şerhli alan kaldıysa o satırlar kalır. Ek C Bölüm-1'in her
alan adı bu dosyada geçer (CI: `tools/esik_kapsama.py`); eşleşmeyen alan kırmızıdır.
