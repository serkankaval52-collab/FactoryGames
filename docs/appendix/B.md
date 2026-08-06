# EK B — Kapasite Tahmini (ideal koşu, geri kenarsız)

> **ŞERH (2026-08-06 — ürün tanımı değişikliği):** bu tablodaki TÜM takvim ve
> insan-saat tahminleri eski ürün tanımına aittir (hyper-casual: tek ekran,
> ucuz deneme, hızlı öldür). Yeni tanım (küçük ama gerçek oyun: çok ekranlı,
> ilerlemeli, tasarım dokümanı + matematik modeli önceden) bu sayıları
> geçersiz kılar. Tablo, tasarım standardı yerleşip sonda ölçümü geldikten
> sonra BAŞTAN yazılacaktır; o güne kadar bu sayılarla planlama YAPILAMAZ.


| Aşama | Takvim |
|---|---|
| -2 Kurulum (makine başına, tek seferlik) | 1–3 sa (insan kapısı sayısına bağlı) |
| -1 Sonda (tek seferlik) | 1–2 gün |
| 0A Hat kurulumu (tek seferlik) | 1 hafta (insan ≈4 sa + bekleme) |
| 0B Pilot (tek seferlik) | kendi tam turuyla ayrı ölçülür (oyun satırlarının toplamı + iOS imza 2–4 sa ilk sefer) |
| 1 Fikir + seçim | 1 gün (veto + paralel hasat penceresi dahil) |
| 2 Plan + pre-mortem | 1 gün |
| 3 Envanter | 0,5 gün |
| 4 Gri kutu | **SONDA ÖLÇÜMÜNDEN** (tahmin değil; sonda raporu burayı yazar) |
| 5 Halka kapısı | 2–3 gün (48–72 sa pencere) |
| 6 İnce üretim | 2–4 gün |
| 7 QA | 1 gün |
| 8 Rubrik kapısı | 2–3 gün (tur ≤ 24 sa varsayımı) |
| 9 Mağaza + organik kit | 2–3 gün |
| 10 Ölçüm penceresi | 14 gün (Ek C) |

**Toplam: yayına ~11–19 gün (Aşama 4 hariç), karara ~25–33 gün.**
Aşama 4 gerçekleşeni sonda sonrası buraya eklenir ve toplam güncellenir.

**İnsan-saat/oyun ≈ 4–7 sa** (veto 0,1 + onaylar 0,5 + form/listeleme 1,5 +
oynama/rubrik 2–3 + yayınla/karar 0,5 + sosyal kit gözden geçirme 0,5).

**Halka maliyeti:** Aşama 5 + Aşama 8 birlikte oyun başına ~8–15 dış-göz oturumu
tüketir; havuz yenilenme hızı Ek C `halka_hakki` karşılığıdır — kıt kaynak
takviminden önce burası tükenebilir; telemetride ayrı sayılır.

**En kötü senaryo (geri kenarları yakarak):** Aşama 1:3 + 2:2 + 4:3 + 6:2 + 7:4 +
8:3 + 9:3-ret limitleri tam yakılırsa yayın öncesi +~12–20 gün. Sessiz taşma olamaz:
**her geri kenarı insana biter**. Takvim tavanı aşımı koşu sırasında telemetriyle
görülür; aşırı durumda karar insandadır.

Bu tablo Ek C `takvim_tavan_gun` ile her koşuda karşılaştırılır (Aşama 10 hat bakım
raporu). Tahmin uydurma varsayılır, ölçüm gerçektir.
