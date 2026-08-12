# KÖR NOKTA ANALİZİ — dışarıdan gelen bulguları biz neden göremedik (v1.3)

**Görev (kullanıcı talimatı, 2026-08-12):** hatta bu güne dek dışarıdan gelen her metin/
model bulgusu için soruyu cevaplamak: "bunu biz neden üretmedik — görmemizde eksik olan
DAVRANIŞ neydi?" Yöntem: git tarihindeki her dış bulgu tarandı (etiket + commit kanıtlı),
her birinden davranış eksiği çıkarıldı, her eksik kalıcı bir merceğe (GG1–GG10,
`standards/gozden-gecirme.md`) bağlandı. İddia disiplini: örnek verilemeyen davranış
eksiği yazılmadı; her madde ağaçta kanıtı olan bir olaya dayanır.

**Gözlem 0 (yapısal):** dışarıdan gelen her bulgu üç özellikten en az birini taşıyordu —
(i) arkasında ÖLÇÜM/kanıt vardı, (ii) bizim baktığımız tarafın KARŞI tarafına bakıyordu,
(iii) "bu değer nereden doğar?" sorusunu soruyordu. Biz ise çoğunlukla kendi metnimizi
savunuyorduk; metin karşılıklı onaydan geçince "doğrulandı" sanıyorduk. Aşağıdaki on
eksik bu tek cümlenin açılımıdır.

## On davranış eksiği (kanıt etiketli)

| # | Davranış eksiği | Kanıt (etiket/commit) | Kalıcı ders → mercek |
|---|---|---|---|
| KN1 | **Mutabakatı kanıt sanmak.** İki model aynı fikirdeyse madde "doğrulandı" sayıldı; sayıların kaynağı sorulmadı. | Threadline devir belgesi (v1.1.1): "iki AI modelinin mutabakatı tek simülasyondan zayıf kanıttır" → B8/B0 doğdu; `ses_lufs_band`/`ses_tepe_dbtp` ağaçta aylarca kaynaksız durdu (açık borç kaydı v1.1.1); Ek C kaynak etiketleri ancak devir yamasıyla geldi. | Her iddianın kanıt sınıfı yazılır: muhakeme / kaynak+tarih / simülasyon / ölçüm-bekliyor / taahhüt. → GG1 |
| KN2 | **Girdinin doğum yerini sormamak.** Kapı ve ölçümler tanımlıydı ama girdilerin NEREDE doğduğu tanımsızdı. | Belge 2 (v1.2): sözleşme palete UYUMU ölçüyordu; paletin kaynağı yoktu — "stil ailesi" bir isimdi, yön değil. Sanat yönü süreci ancak dış belgeyle doğdu. | Her standardın her girdisi için "kaynağı kim/nerede" satırı bulunur. → GG2 |
| KN3 | **Kaydı yeniden-üretilebilirlik sanmak.** "Manifest var" sandık; manifest olayı yazıyordu, çağrıyı değil. | Belge 1/V1 (v1.2): transform manifesti parametresizdi; paleti üç ay sonra değiştirmek sohbet geçmişine kalıyordu → G8 (parametreli satır + örneklem hash kapısı). | Her artefakt: "90 gün sonra aynen üretilebilir mi?" testinden geçer. → GG3 |
| KN4 | **Kuralı tek tarafta yazmak.** Kuralın koyulduğu kapı ile uygulanması gereken kapı farklıydı. | Belge 1/V2 (v1.2): katalog-tükenme kuralı Ek A'da yazılıydı; üretim tarafı (Aşama 6) katalog dışına çıkma yetkisini hiç kapatmamıştı. | Her kural için üretim tarafı + tüketim tarafı birlikte denetlenir. → GG4 |
| KN5 | **Kendi eşiğini gerçekliğe önceden koşmamak.** Lint'ler hiçbir gerçek varlığa koşulmadan yazılıyordu. | Belge 1/V3 (v1.2): "doğrulayıcıyı mevcut varlıklara geçir, kaçı kalıyor gör" dışarıdan geldi → 0A eşik sağlaması. Eşiklerin ulaşılamaz olma riski ilk oyuna kalacaktı. | Yeni kapı/lint önce mevcut gerçekliğe SALT-OKUR koşulur, geçme oranı yazılır. → GG5 |
| KN6 | **Beklemeyi maliyet saymamak.** İşlem süresi ölçülüyordu (Ek B), bekleme zinciri hiç sayılmıyordu. | Alan 6 (v1.0.22): insan-yuku envanteri dış görevle doğdu — "5 dakikalık iş 2 gün bekliyorsa hızı belirleyen 2 gündür"; zincirin ~2/3'ü oyun bittikten sonraki bekleme çıktı. | Her insan dokunuşunun bekleme penceresi + tavanı envanterdedir. → GG6 |
| KN7 | **Ertelemeyi tasarım sanmak.** "Sonda sonrası yazılacak" tahliyesi tasarım yerine geçiyordu. | Köprü 6-ALAN kuralı: erteleme yasaklandı; ölçüm gereken madde bile şerhli TAM tasarımla yazılır (ilk-kosu üç-durum tablosu v1.0.20 böyle doğdu). | Erteleme yok; şerhli tam tasarım var. → GG7 |
| KN8 | **Sessiz varsayılanlar.** Kapıların boş-veri davranışı yazılı değildi; "veri yok" ile "geçti" karışabiliyordu. | Alan 5 (v1.0.20–21): üç-durum zorunluluğu (ÇALIŞTI/ŞERHLİ/VERİ-YOK) + VERİ-YOK kanıt ister (kanıtsız satır ihlal); R6 tek-doluluk düzeltmesi ancak saldırıyla görüldü. | Her kapının boş-veri davranışı yazılıdır. → GG8 |
| KN9 | **Vitrin hedefini üretim hedefi sanmak.** Doğrulanan şey hero görüntüydü, üretilebilirlik değil. | Belge 1 (v1.2): ekran görüntüsü döngüsü tek kameraya optimize eder; bizde karşılık: güzel metin ≠ koşan kapı. `arac_suzgec.py`/`esik_kapsama.py` canlı süpürmeleri (v1.0.19/21) ve CI'daki failing-gate disiplini bu dersin ürünüdür. | Karar vitrinde değil doğrulayıcıda verilir. → GG9 |
| KN10 | **Dış saldırıyı kişiye bağlamak.** Saldırgan geçiş köprüdeydi, sistemde değildi; köprü kalkınca boşluk doğdu. | Üçlü düzenin dağılışı (2026-08-12, kullanıcı kararı): v1.0.x–v1.2 arası neredeyse her derinleşme dış saldırı turuyla geldi (A1.1–A6.4, devir yaması, Belge 1-2) — sistem kendi kendine saldırmıyordu. | Saldırı geçişi kalıcı, isimli, tekrarlanabilir sistemdir. → GG10 + bu dosyanın kardeş standardı |

## Kendi payıma düşenler (açık kayıt)

Yazan, kendi çıktısını aynı turda denetleyemez — kanıtları:
- "Doğruluk/tat ölçümü simülasyondadır" cümlesi (v1.1.1) anlam bozuyordu; köprü yakaladı,
  v1.1.2'de düzeltildi. Yazan bendim.
- 2.md Çıktı satırı "B1–B7" v1.1.1'de bayat kaldı (geçiş B1–B8 diyordu); v1.2'de kendi
  taramamda bulundu. Yazan bendim.
- Commit mesajı yazım kazaları ("kapsisi" v1.2; daha önce "olju kanal", "ohaset",
  "kosto/Bolunce") — tarih yeniden yazılmadı, kayıtlı.
- v1.1.1'de ses_* kaynak borcunu kendim bildirmem doğruydu ama borç ancak devir belgesi
  saldırısıyla etiketlendi — KN1'in canlı örneği bizzat benim üretimimdir.
Kalıcı kural (GG disiplini): **mercek geçişi, üretim geçişinden AYRI turda koşulur.**

## Bu dosyanın kullanımı

Bir defalık rapor değildir: yeni dış bulgu geldiğinde tabloya satır eklenir (tarih +
kanıt etiketi + ders); bir mercek defalarca aynı eksiği yakalıyorsa eksik Sözleşme-5
sırasıyla lint/test'e çevrilir ve ilgili GG satırına "artık mekanik" damgası düşülür.
