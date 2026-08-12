# GÖZDEN GEÇİRME STANDARDI — kalıcı saldırı geçişleri GG1–GG10 (v1.3)

**Neden var:** üçlü düzen (yazıcı + harici kırmızı takım) 2026-08-12 kullanıcı kararıyla
sona erdi; dış denetim boşluğu kişiye değil SİSTEME bağlanır. Kaynak analiz:
`docs/kor-nokta-analizi.md` (KN1–KN10 — her mercek oradaki kanıtlı bir davranış
eksiğinden doğdu; kanıtsız mercek yok).

**Sınır (v1.0.10 reddi sürer):** bu sistem model komitesi, persona konseyi veya skor
ortalaması DEĞİLDİR — tekrar açılmaz. Mercek = tek yürütücünün isimli, sıralı,
tekrarlanabilir geçişidir; puan üretmez, bulgu üretir. Deterministik hale gelen mercek
zamanla lint/test'e çevrilir (Sözleşme-5 sırası: lint → kontrol listesi → kural).

**Disiplin:** mercek geçişi ÜRETİM geçişinden ayrı turda koşulur (yazar kendi çıktısını
aynı turda denetleyemez — kanıt: kor-nokta-analizi "kendi payıma düşenler"). Bulgu olmazsa
"tarandı, bulgu yok + kapsam" yazılır; sessiz geçiş yok (6.md "boş liste" emsali).

## Mercekler (her geçişte sorulan tekil soru)

| Mercek | Soru | Ders kaynağı |
|---|---|---|
| GG1 Menşei | Her sayı/iddia kanıt sınıfı etiketli mi (muhakeme / kaynak+tarih / simülasyon / ölçüm-bekliyor / taahhüt / BİLİNMİYOR)? Etiketsiz yenisi girdi mi? | KN1 (devir yaması v1.1.1; ses_* borcu) |
| GG2 Girdi menşei | Bu standardın/kapının her girdisinin "nerede, kim üretir" satırı var mı? Boşluktan doğan girdi kaldı mı? | KN2 (palet — Belge 2, v1.2) |
| GG3 Yeniden-üretim | Bu artefakt/sayı 90 gün sonra aynen üretilebilir mi (çağrı + parametre + sürüm + hash)? | KN3 (G8 — Belge 1/V1) |
| GG4 Karşı taraf | Kuralın üretim tarafı ve tüketim tarafı ikisi de yazılı mı? Tek taraflı kural kaldı mı? | KN4 (6.md üretim yetkisi — V2) |
| GG5 Sıfır-gerçeklik provası | Yeni kapı/lint mevcut gerçekliğe (salt-okur) koşuldu mu; geçme oranı kayıtlı mı? | KN5 (0A eşik sağlaması — V3) |
| GG6 Bekleme zinciri | Yeni insan dokunuşu bekleme penceresiyle insan-yuku'ya girdi mi; tavanı/taahhüdü var mı? | KN6 (Alan 6 envanteri) |
| GG7 Erteleme taraması | "sonra/sonrası/ileride" içeren her satır şerhli TAM tasarım mı; kaçak erteleme var mı? | KN7 (6-ALAN kuralı) |
| GG8 Boş-veri davranışı | Yeni kapının ÇALIŞTI/ŞERHLİ/VERİ-YOK davranışı yazılı mı; "veri yok" "geçti" sayılmıyor mu? | KN8 (Alan 5, ilk-kosu) |
| GG9 Doğrulayıcı önceliği | Karar vitrinde (metin/görüntü) mi veriliyor, doğrulayıcıda mı? Doğrulayıcısı olmayan yeni iddia var mı? | KN9 (hero-shot dersi; canlı süpürmeler) |
| GG10 Kalıcı geçiş | Bu çalışmada hangi mercekler, hangi turda koşuldu — kayıt nerede? (Merceğin kendisi de denetlenir.) | KN10 (üçlü düzenin dağılışı) |

## Ne zaman koşulur

1. **Yeni dış belge/bilgi** geldiğinde: tam tur (GG1–GG10), alınan/alınmayan gerekçeli.
2. **Sözleşme-5 yükseltme adayı** açıldığında: ilgili mercekler (aday satırında adları).
3. **Her Aşama 10 hat bakımında:** rotasyonlu 2 mercek; sonuç hat bakım raporuna satır.
4. **Yeni standart/kapı/araç yazımında:** GG1–GG8 mini-turu, üretimden ayrı turda.

## Çıktı disiplini

Bulgu: `{tarih, etiket/sürüm, mercek, bulgu, aksiyon, kanıt}` olarak kayda düşer —
büyük turlar `docs/gecis-denetimi.md`'ye satır, tekil bulgular commit mesajında.
Aksiyon önceliği Sözleşme-5'tir (önce-kırmızı kanıtlı lint/test > kontrol listesi >
CLAUDE.md kuralı — son çare, tavana tabi). Mercek yeni norm üretmez: norm yalnız
Sözleşme-5 süreciyle girer; mercek raporu tekliftir, karar kullanıcıdadır.
