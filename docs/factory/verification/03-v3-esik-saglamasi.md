# 0A / Adım 3 — V3 eşik sağlaması

**Tarih (UTC):** 2026-08-15 · **Sonuç:** planlanan biçimiyle **VERİ-YOK**; yerine
**araç doğrulaması + analitik eşik ölçümü** yapıldı (aşağıda). Kapı "geçti"
sayılmaz (ilk-kosu.md §1).

## Neden VERİ-YOK

0A.md adım 3, G1–G8/S1 lint'lerinin kullanıcının **yayındaki oyununun** varlıklarına
salt-okur koşulmasını istiyordu; amaç "eşikler gerçekçi mi?" sorusunu ilk oyundan önce
görmekti.

**Kullanıcı kararı (2026-08-15):** elde yalnızca acemi dönemde yapılmış bir oyun var ve
referans alınması önerilmedi. Karar teknik olarak yerindedir ve executor tarafından
kabul edilmiştir: o örneklemde çıkacak düşük geçme oranı **eşiğin yanlışlığını değil o
oyunun zayıflığını** ölçerdi — yani araç kendi kalibrasyonu için yanlış sinyal alırdı.

**Kanıt (VERİ-YOK zorunlu artefaktı):** ölçüm girdisi kümesi boştur; salt-okur lint
hiçbir dizinde koşulmamıştır, kullanıcının proje klasörüne erişilmemiştir (kural 26).

**Devir:** "eşikler gerçek bir oyunda tutuyor mu?" sorusu **kalibrasyon penceresine**
(ilk 3 koşu, ilk-kosu.md §3) devredilir; ilk fabrika oyununun varlıkları bu ölçümün
doğal girdisidir.

## Yerine yapılan: aracın kendisi ölçüldü

V3'ün iki amacı vardı. (a) eşiklerin gerçekçiliği — yukarıda devredildi.
(b) **lint gerçekten ölçüyor mu?** — bu, gerçek oyun verisi olmadan da kanıtlanabilir
ve kanıtlandı: `factory.core/templates/tools/lint/test_lint.py` (10 test, hepsi yeşil).

Testler **önce-kırmızı** disipliniyle yazıldı: her kapı için hem geçen hem **kalan**
örnek vardır — kapı her zaman yeşil yanan bir süsleme değildir.

| test | ne kanıtlar |
|---|---|
| siyah/beyaz = 21.00 | G4 WCAG formülü dış referansla doğru |
| `#767676`/beyaz ∈ [4.5, 5.0) | AA metin eşiğinin kanonik sınır örneği |
| kırmızı-yeşil çifti < 3.0 | G6'nın klasik ayırt-edilemez çifti **reddettiği** |
| mavi-sarı protanopide > 3.0 | kapının her şeyi reddetmediği (yanlış-pozitif değil) |
| iyi palet → 0 kırmızı | geçerli palet yeşil |
| gri palet → kırmızı | ayırt edilemeyen palet **yakalanıyor** |
| palet yok → VERİ-YOK + kanıt | eksik girdi sessizce geçmiyor |
| 40 nesneli sahne → exit 1 | `lint.py` süreç olarak kırmızı veriyor |
| temiz ağaç → exit 0 | yanlış-pozitif yok |

## Ölçülen bulgu: G6 eşiği uygulanabilir ama DAR

Test yazarken sezgisel olarak seçilen "iyi" palet
(`#101418`/`#40D0F0`/`#FFD200`/`#FF5A5A`) **düştü**. Ölçüm:

```
cift                normal  prot  dote  trit     esik
tehlike/vurgu         2.11  1.67  1.42  1.04      3.0   ← KIRMIZI (4/4)
tehlike/arka_plan     6.04  8.79 10.91  5.70      3.0   ✓
ana_ozne/arka_plan   10.13  5.46  4.50 11.51      3.0   ✓
```

Sonra 12 elle seçilmiş aday kombinasyonun **hiçbiri** geçmedi. Kök neden analitik
olarak çıkarıldı:

> Kontrast ≥ 3 ⇔ `L₁ ≥ 3·L₂ + 0.1`. Üç rol parlaklık ekseninde zincir oluşturur
> (arka plan < tehlike < vurgu): `L_vurgu ≥ 9·L_arka + 0.4`. `L ≤ 1` olduğundan
> **`L_arka ≤ 0.067`** — yani arka plan **zorunlu olarak çok koyu**, tehlike dar bir
> orta banda sıkışır.

Sistematik HSV taramasıyla (492 arka plan × 151 tehlike × 36 vurgu × 127 ana özne
adayı) **geçen bir palet bulundu**:

```
arka_plan #1A0D0D   tehlike #994C4C   vurgu #FFD480   ana_ozne #4C998C

cift                normal  prot  dote  trit
tehlike/vurgu         4.28  3.74  3.46  3.22   ✓
tehlike/arka          3.18  4.01  4.49  3.11   ✓
ana_ozne/arka         5.66  3.79  3.31  5.31   ✓
ui_metin/ui_zemin    19.01 18.51 18.27 19.04   ✓
```

**Çıkarım:** `gorsel_kontrast_ana_ozne = 3.0` eşiği **imkansız değildir** (kanıt:
geçen palet), ancak palet özgürlüğünü ciddi biçimde daraltır. Geçen palet **düşük
doygunluklu** tonlardadır; yüksek doygunluklu, ikisi de parlak tehlike–vurgu çiftleri
(tipik hyper-casual paleti) **sistematik olarak düşer**. Bu, tasarımı şu yöne zorlar:
koyu arka plan + parlaklık ekseninde üç ayrı bant.

**Sözleşme-5 gündemi (mimar kararı):** G6'nın kritik çift listesindeki
`tehlike ↔ vurgu` maddesi ya (i) eşiği bu çift için ayrı tanımlamalı, ya (ii) aynen
kalmalı — çünkü gorsel-sozlesme G6 zaten "renk TEK BAŞINA bilgi taşıyamaz; tehlike/vurgu
ayrımı biçim/ikonla da desteklenir" diyor ve sıkı eşik bu ilkeyi mekanik olarak
dayatıyor olabilir. Executor karar vermez; ölçümü sunar.

## Yan bulgu: bir test varsayımı ölçümle çürütüldü

İlk yazımda "protanopi simülasyonunda kontrast **düşer**" varsayılmıştı. Ölçüldü,
**yanlış** çıktı: `#D40000`/`#00A000` için normal 1.59 → protanopi 2.02 → döteranopi
3.77. Sebep: WCAG kontrastı **parlaklık farkına** bakar; simülasyon parlaklığı
değiştirdiği için oran artabilir. Test, doğru iddiaya çevrildi (çift **normal görüşte
zaten** eşiğin altındadır) ve gerekçe koda yazıldı — aynı yanılgı tekrar edilmesin diye.

## Artefaktlar

| ne | nerede |
|---|---|
| lint öz-testleri | `factory.core/templates/tools/lint/test_lint.py` (v0.1.1) |
| düzeltilmiş şablon paleti | aynı dosya, `IYI_PALET` |
| koşum | `python tools/lint/test_lint.py` → `Ran 10 tests ... OK` (exit 0) |
