# Sanat yönü paketi — düz-geometrik

**Yön:** NET-SOKAK (saf; 0 hibrit turu) · **Pilot:** Tezgâh (0B, kart A) · **Kaynak tuval:**
`docs/factory/kavram/2026-08/sanat/yonler/net-sokak/yon.svg` — Aşama 3 PR #1, `v1.4.8`
(`74f8157`). Paket kendi kaynağıdır, Ek C'ye girmez. Sayılar tuvalden ölçüldü; sıfat yok.

## 1. Renk paleti
| rol | hex | sahne oranı | kullanım |
|---|---|---|---|
| arka_plan | `#E8E4DA` | %64,1 | sahne ve kart zemini |
| yol | `#CFC8BA` | %18,1 | zemin şeridi, tek ton |
| govde | `#5B7285` | %8,2 | tezgâh yan yüzeyleri |
| ana_ozne | `#1F4E66` | %5,6 | tezgâh üst yüzeyi, birincil şekil |
| vurgu | `#0F7A5A` | %2,5 | tente, etkin durum, ayraç |
| stok | `#D9A521` | %0,9 | sayılabilir stok küpleri |
| ui_metin | `#16202A` | %0,5 | metin; sahnedeki pay koyu türevlerdir |
| tehlike | `#B4341F` | %0,02 | uyarı üçgeni — tek işaret |

Ölçüm: 1160×536 sahne, 621 760 piksel; %82,4 hex'e tam eşleşir, %17,6 kenar yumuşatması en yakın role katıldı. Zemin/özne dengesi %82,2 / %17,8.

## 2. Kontur kuralı
Oyun sanatında **kontur YOK** — ayrım konturla değil parlaklık basamağıyla kurulur (§3).
G5 üçlüsüne `"0 px (konturusuz)"` **STRING** yazılır: sayısal `0` JSON'da falsy'dir ve
G5 kapısı `not ucslu.get(alan)` ile baktığından manifestte `0` KIRMIZI üretir.
**İstisna (çelişki değil):** kalın kontur yalnız ikon dili ekseninden gelir (tohum
`kalin-kontur-tek-nesne`); ölçülen ikon konturu nesne genişliğinin %1,85'i (4/216 px). G5 üçlüsü oyun sanatını kapsar; ikon paketi ayrı eksendir.

## 3. Gölgeleme
Üç basamak, çarpansal koyultma; gradyan ve yumuşak gölge yok. Üst yüzey **1,00** (rolün
kendi hex'i) · sağ yan **0,86** · sol ön **0,72** (en koyu ana yüzey) · ince detay (tente
direği, kart ayracı) **0,60**. Işık sağ-üstten; komşu yüzeyler arasında en az %14
parlaklık farkı korunur, türev tonlar G6'ya tabidir.

## 4. Silüet / geometri
- **Izgara:** her koordinat 4 px'in katı. Yarım piksel kenar ve hizasız kutu yok.
- **Köşe yarıçapı:** 0 px — keskin. Yumuşatma oranı 0; yönün kimlik değişkeni budur.
- **Perspektif:** izometrik; üst yüzey 2:1 eşkenar dörtgen. Her blok tek poligon
  fonksiyonundan üretilir — serbest çizim yok.
- **Ölçek:** 1,00 taban, blok yüksekliği 96 px; abartı oranı yok. **Okuma sırası:** en
  büyük şekil = en önemli karar.

## 5. Doku / yüzey
**Doku YOK — düz yüzey.** Açık karardır, boşluk değil: çizgi sıklığı 0, yüzey içi
kontrast 0; ayrım tümüyle palet kontrastından gelir, çözünürlükten bağımsızdır.

## 6. Işıklandırma
**Gradyan KULLANILMIYOR — açık karardır, boşluk değil;** gradyan hex'i yoktur. Işık yönü
sağ-üst, karşılığı §3'teki üç basamaklı çarpansal koyultmadır. Bloom, glow, post-process ve renkli ışık yoktur.

## 7. Obje / ekran tablosu
| nesne | renk | kontur | not |
|---|---|---|---|
| tezgâh (üst / yan) | `ana_ozne` / `govde` ×0,86 ×0,72 | yok | izometrik 2:1, ışık sağ-üst |
| tente + direği | `vurgu` / `govde` ×0,60 | yok | direk tepesine oturur, havada durmaz |
| stok küpü | `stok` | yok | üst yüzeye oturur; tek sıcak nokta |
| yol şeridi | `yol` | yok | dokusuz tek ton |
| uyarı üçgeni | `tehlike` | yok | ekranda tek; biçim eşliği taşır |
| kart zemini / ayraç | `arka_plan` / `vurgu` | yok | ayraç 3 px |
| birincil düğme / metin | `ana_ozne` / `ui_metin` | yok | düğme metni `arka_plan`; sans 600/400 |

## 8. Hibrit köprüsü
Hibrit yok — saf NET-SOKAK; 0 hibrit turu. Köprü kurulmadığı için kural tanımlanmadı.

## 9. URP 2D yol haritası
Sprite-Unlit materyal; düz renk + tek atlas → batch dostu; gradyan/glow/post yok.
**Ölçüm YOK:** Unity koşulmadan kare hızı, draw call ve doldurma oranı BEYAN EDİLMEZ — Aşama 2'de ölçülür, o güne kadar VERİ-YOK. Risk: izometrik derinlik sıralaması.

## 10. Referans eserler
- **Mini Metro** — rol rengi tek anlam taşır; kontursuz düz alan okunur.
- **Mini Motorways** — yol şeridi tek tonda ve dokusuz; trafik biçimle ayrışır.
- **Harry Beck, Londra metro şeması** — şematik netlik; açı disiplini bilgi taşır.
- **Josef Müller-Brockmann afişleri** — ızgara disiplini; tek vurgu rengi.

Yasak-liste `2026-08` ile çaprazlandı: hiçbiri on maddeden birine girmiyor — kopya
değil, özellik alımı. Kural 26: kullanıcının kendi projeleri referans değildir.

## Sabitlenen dizginlemeler (Aşama 2 bunları alıntılar)
- `stok` sarısı sahnenin tek sıcak noktasıdır; başka role genişletilmez.
- Ekranda en fazla **2** kırmızı öge bulunur; uyarı işareti tektir.
- Türev tonlar G6'ya tabidir; tritanopide `ana_ozne`↔`arka_plan` payı **5,84'ün altına düşmez** — tavan budur.
- Renk tek başına bilgi taşımaz: `tehlike` daima üçgen, `vurgu` daima yatay tente.

## G5 manifest üçlüsü (Aşama 2'de birebir alıntılanır)
```json
"stil": {
  "perspektif": "izometrik 2:1",
  "cizgi_kalinligi_bandi": "0 px (konturusuz)",
  "golge_yonu": "sag-ust isik; 1,00 / 0,86 / 0,72 uc basamak"
}
```
