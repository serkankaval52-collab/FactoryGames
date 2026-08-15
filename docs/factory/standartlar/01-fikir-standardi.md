# Fikir standardı — Aşama 1 konsept üretimi

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** kart alanlarının tanımı, rotasyon aritmetiği ve kura mekaniği
**burada tekrarlanmaz**. Bu dosya yalnız **sırayı** ve **kapı öncesi kontrol listesini**
verir; her satır kendi kaynağına atıfla çalışır.

## Girdi zinciri (sıra bağlayıcıdır)

| # | adım | tek kaynağı |
|---|---|---|
| 1 | Aylık yasak liste arşivi üretilir | `docs/standards/yasak-liste/` (ayın ilk koşusu) |
| 2 | Kura çekilir (havuz + filtre) | `tools/kura.py` + `docs/standards/havuz.json` — zar **model dışıdır** |
| 3 | Kura çıktısı defter/yasak/dolu filtresinden geçer | `docs/appendix/A.md` "Kurallar" + `docs/standards/model-klise-defteri.md` |
| 4 | Konsept kartı yazılır (K1–K3 dahil) | `docs/standards/tasarim-standardi.md` **Bölüm A** |
| 5 | Rakip 8-eksen tablosu + defter farkı ölçülür | `docs/appendix/A.md` (≥3 eksen farkı) |
| 6 | Yorum hasadı (koşullu) | `docs/stages/1.md` — "sinyal yok" geçerli sonuçtur |

## Kapı öncesi kontrol listesi (executor doldurur, kapı "dolu ve tutarlı mı" bakar)

- [ ] Kura kaydı var (havuz sürümü + filtre + çekilen eksenler); **zar yeniden atılmadı**
- [ ] Yasak liste taraması yapıldı, çakışan klişe yok
- [ ] Defterdeki **her** kayıttan ≥3 eksende farklı (kanıt: eksen bazlı tablo)
- [ ] `(tür × stil ailesi)` hücresinde canlı oyun ≤1; aynı stil ailesinde canlı ≤2
- [ ] UI kit / ikon dili / reklam matrisi arka arkaya en fazla 2 oyunda (soğuma kuralı)
- [ ] K1 yaş beyanı yazıldı ve **stil ailesi seçimiyle tutarlı**
- [ ] K2 keşif videosu çekim listesi ≥3 sahne (videosu yazılamayan konsept geçemez)
- [ ] K3 ödül takası tanımlı (değeri B3'te sayılanacak)
- [ ] Bant beyanı yapıldı

## Boş-veri davranışı

İlk koşuda defter **boş değildir**: ilk kayıt mevcut yayındaki oyundur ve tam ağırlıklıdır
(`docs/appendix/A.md` "Başlangıç durumu"). Dolayısıyla ≥3 eksen farkı ilk koşuda da
**ölçülebilir**; "veri yok" gerekçesiyle atlanamaz (`docs/standards/ilk-kosu.md` §1).

## Havuz tükenmesi

Rotasyonu sağlayan konsept üretilemiyorsa kapı **açılmaz** ve katalog genişletme görevi
açılır; hat duraklar, kural sessizce esnetilmez. Tek kaynak: `docs/appendix/A.md`
"Havuz tükenmesi protokolü". Aynı protokol kuranın filtrelenmiş uzayı boşaldığında da
işler — **kura yeniden çekilmez**.

## FORM-BEKLIYOR alanları (L8)

| alan | durum |
|---|---|
| `dis_halka_havuzu`, `halka_hakki` | **FORM-BEKLIYOR** — Aşama 1'in çıktısını doğrudan bağlamaz ama Aşama 5 planlamasına girer |
| `sosyal_video_hakki` | **FORM-BEKLIYOR** — K2 çekim listesinin üst sınırı buradan gelir |

Etiket, kullanıcının 0A adım 6 form dönüşüyle düşer; o güne dek alan **boş bırakılmaz,
"FORM-BEKLIYOR" yazılır** (etiketsiz tahmin yasak — Ek C doldurma protokolü).
