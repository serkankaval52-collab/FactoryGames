# İNSAN YÜKÜ ENVANTERİ — dokunuş, bekleme, kuyruk (Alan 6)

**Kapsam (köprü görevi):** hattaki her insan dokunuşunun tam envanteri; sayılabilir, ölçüm
gerektirmez. Ölçü **bekleme süresidir**, işlem süresi değil — 5 dakikalık iş 2 gün bekliyorsa
hattın hızını belirleyen 2 gündür; Ek B işlem saatlerini sayar, bu zinciri göremez. Sayı
yalnız yazılı pencereden veya tarihli kaynakla gelir; aksi hâlde BİLİNMİYOR yazılır, uydurma
yasak (güvenilirlik etiketi: "yazılı" = ağaçta tanımlı pencere; "kaynak" = tarihli dış okuma).
**Kuyruk** sütunu Sözleşme-9'a (insan kapısı kuyruğu ≤2, tek insan WIP=1) girdi verir;
"zaman-aşımlı" = sessizlik onaya sayılır, insan yanıt vermese hat durmaz (gerçek tıkanma
değildir).

## 1. Koşu başına envanter (A1–A10)

| Yerde | İnsan eylemi | Bekleme penceresi | Kuyruk |
|---|---|---|---|
| A1 veto | konsept kartını inceleme; itiraz isteğe bağlı | 24 sa (yazılı; sessizlik = onay) | zaman-aşımlı |
| A1 yorum hasadı | 2–3 kanala tek görsel + tek cümle (hesap temsili onayı) | veto penceresiyle paralel, ≤48 sa (yazılı) | hayır |
| A3 lisans/hesap | lisans/şifre/hesap anı (koşullu; secrets pinliyse yok) | BİLİNMİYOR (koşullu) | koşullu |
| A5 davet | kanal çağrısı/mesajı (hesaplar kullanıcının; metin halka-std) | BİLİNMİYOR — halka yanıt hızı ilk ölçüm konusu | evet |
| A5 toplama | pencere beklemesi; toplama/tablolama otonom | 48–72 sa (yazılı; halka-std §5) | hayır (duvar saati) |
| A5 GEÇ/RAF | yazılı karar (yürüten karma — sahiplik ayrımı kayıt noksanı) | BİLİNMİYOR | evet |
| A8 kullanıcı oturumu | oyunu oynar; rubrik 3 eksen + R2b/R4/G5 EVET-HAYIR + yazılı onay | tur ≤24 sa VARSAYIMI (Ek B şerhli; pencere yazılı değil — ölçüm adayı) | evet |
| A8 dış-göz turu | ≥2 taze göz oynar, * eksenleri puanlar | BİLİNMİYOR (pencere yazılı yok — ölçüm adayı) | evet |
| A9 T3 veto | ikon / screenshot / feature graphic onayı | BİLİNMİYOR | evet |
| A9 formlar + gönder | yaş/App Privacy/Data Safety gözden geçirme + iki gönder | BİLİNMİYOR (ilk oyundan sonra şablonlaşır) | evet |
| A9 review | mağaza inceleme beklemesi (ret döngüsü aynı pencereyi tekrar eder, max 3) | Apple resmi %90 ≤24–48 sa; derleme ilk gönderim 2–5 gün; Play çoğu saatler–7 gün (kaynak: 2026-08 taraması, resmi+derleme, değişken) | hayır (duvar saati) |
| A10 ölçüm penceresi | organik vitalleri bekleme | `olcum_penceresi_gun` (örn. 14 — Ek C, şerhli) | hayır |
| A10 karar oturumu | üç-kelime karar + Ek C formu + halka raporu + PR merge | BİLİNMİYOR | evet |

## 2. Tek seferlik ve ömür-boyu envanter

| Yerde | İnsan eylemi | Bekleme penceresi | Kuyruk |
|---|---|---|---|
| kurulum (-2) | UAC onayları (≥2) + tarayıcı akışı + koşullu hesaplar; kapı ön-bildirimi tek mesaj (yazılı) | BİLİNMİYOR (işlem tahmini Ek B'dedir; bekleme değil) | evet (tek sefer) |
| sonda (-1) | insan-kapisi durakları ≤10 (sayılır) + BAŞARISIZ kararı | BİLİNMİYOR — sonda ölçümünün konusu | evet |
| 0A | hesap doğrulamaları; TEK form (defter 8 eksen + L6 blokları + Ek C Bölüm-1); private ikiz; sosyal hesaplar | form işlemi ~1 dk yazılı; bekleme BİLİNMİYOR | evet |
| 0B | konseptin açık onayı; darboğaz satırı yorumları; iOS imza zinciri; review gönderimi | iOS imza ≈2–4 sa + tıkanma payı (L3, yazılı); kalanı BİLİNMİYOR | evet |
| ömür boyu | yıllık target-API bakım turu (oyun başına — Ek A F4) | yıllık takvim (Ek A, yazılı) | hayır |
| ömür boyu | Ek A katalog genişletme kürasyonu (tetikte; insan onaylı) | BİLİNMİYOR (koşullu) | koşullu |
| ömür boyu | aylık yasak-liste arşivi (otonom; web yoksa insan tek cümle ile) | BİLİNMİYOR (koşullu) | koşullu |
| ömür boyu | Ek C değişimleri (tek form disiplini — L8) | istisnai | evet |

## 3. Yargılar: birleştir / kaldır

- **Kaldırma:** satır kaldırılamadı — her dokunuş ya veto/yargı ya hesap temsiliyetidir.
  Envanterin ana bulgusu budur: dokunuş sayısı az; maliyet bekleme zincirinde toplanıyor.
- **Birleştirme-1:** A10 oturumu tek mesajda toplanır (karar + Ek C formu + halka raporu +
  PR'lar) — uygulama protokolü; aşama metni gerektirmez.
- **Birleştirme-2:** A9 insan blokları tek oturumdur (T3 + formlar + gönder) — yazılı
  insan kapısı bunu zaten toplar; envanter doğrular.
- **Birleştirme-3:** A1 veto penceresi ile yorum hasadı örtüktür (yazılı) — ek bekleme
  yaratmaz. Kurulum onaylarının ön-bildirimi tek mesajdır (yazılı) — birleşik durumda.

## 4. Kritik bekleme zinciri ve kuyruk tutarlılığı

- **Zincir (koşu başına, sıralı):** A1 veto 24 sa → A5 pencere 48–72 sa → A8 tur (≤24 sa
  varsayımı) → A9 review (Apple %90 ≤48 sa / Play ≤7 gün aralığı; değişken) → A10 pencere
  (örn. 14 gün, şerhli). Toplam yazılmaz: takvim tavanı ve toplam Ek B/Ek C'nin işidir;
  bu dosya zincirin halkalarını ve BİLİNMİYOR noktalarını sayar — BİLİNMİYOR satırları
  pilot koşunun (0B) darboğaz PR'ının doldurma listesidir.
- **Kuyruk durumu (Sözleşme-9 ≤2):** aşamalar seri; eşzamanlı "evet" en fazla 2 kalemde
  toplanır (A8: kullanıcı oturumu + dış-göz turu paralel). Tasarımla tutarlı; gözlenen
  aşım A10 hat bakım raporuna satır olarak düşer — bu dosya sayımın tek kaynağıdır.
