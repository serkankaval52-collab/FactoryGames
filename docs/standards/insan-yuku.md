# İNSAN YÜKÜ ENVANTERİ — dokunuş, bekleme, kuyruk (Alan 6)

**Kapsam (köprü görevi):** hattaki her insan dokunuşunun tam envanteri; sayılabilir, ölçüm
gerektirmez. Ölçü **bekleme süresidir**, işlem süresi değil — 5 dakikalık iş 2 gün bekliyorsa
hattın hızını belirleyen 2 gündür; Ek B işlem saatlerini sayar, bu zinciri göremez. Sayı
üç kaynaktan gelir: **yazılı** pencere / **kaynak**lı tarihli dış okuma / **taahhüt** (kullanıcının
0A-6 formunda kendi azami dönüş süresi — ölçülecek şey değil, vaat edilecek; A6.1). Hiçbiri
yoksa BİLİNMİYOR yazılır, uydurma yasak. **Kuyruk** sütunu Sözleşme-9'a (insan kapısı kuyruğu
≤2, tek insan WIP=1) girdi verir; "zaman-aşımlı" = sessizlik onaya sayılır, insan yanıt
vermese hat durmaz (gerçek tıkanma değildir). Taahhüt aşılırsa kapı DURMAZ — aşım A10 hat
bakım raporuna satır olarak düşer; kullanıcı kendi darboğazını görür (A6.1).

## 1. Koşu başına envanter (A1–A10)

| Yerde | İnsan eylemi | Bekleme penceresi | Kuyruk |
|---|---|---|---|
| A1 veto | konsept kartını inceleme; itiraz isteğe bağlı | 24 sa (yazılı; sessizlik = onay) | zaman-aşımlı |
| A1 yorum hasadı | metni executor hazırlar, gönderen KULLANICIDIR — kendi hesapları, kendi itibarı (A6 hükmü) | veto penceresiyle paralel, ≤48 sa (yazılı) | zaman-aşımlı |
| A3 lisans/hesap | lisans/şifre/hesap anı (koşullu; secrets pinliyse yok) | BİLİNMİYOR (koşullu) | koşullu |
| A5 davet | kanal çağrısı/mesajı (hesaplar kullanıcının; metin halka-std) | `halka_davet_tavan_gun` (Ek C, taahhüt) — dolarsa eldeki N ile devam, N rapora yazılır, küçük örneklem şerhli (A6.4) | evet |
| A5 toplama | pencere beklemesi; toplama/tablolama otonom | 48–72 sa (yazılı; halka-std §5) | hayır (duvar saati) |
| A5 GEÇ/RAF | model öneri yazar, KULLANICI onaylar — sessizlik onay SAYILMAZ (A6 hükmü; öldürme komşusu karar) | `insan_yanit_tavan_karar_gun` (taahhüt) | evet |
| A8 kullanıcı oturumu | oyunu oynar; rubrik 3 eksen + R2b/R4/G5 EVET-HAYIR + yazılı onay | `insan_yanit_tavan_rubrik_gun` (taahhüt) | evet |
| A8 dış-göz turu | ≥2 taze göz oynar, * eksenleri puanlar | BİLİNMİYOR — gönüllü yanıt hızı (ölçüm adayı; tavan A5 ile aynı hücreden türetilemez — kayıt) | evet |
| A9 T3 veto | ikon / screenshot / feature graphic onayı | `insan_yanit_tavan_t3_gun` (taahhüt) | evet |
| A9 formlar + gönder | yaş/App Privacy/Data Safety gözden geçirme + iki gönder | `insan_yanit_tavan_magaza_form_gun` (taahhüt) | evet |
| A9 review | mağaza inceleme beklemesi (ret döngüsü aynı pencereyi tekrar eder, max 3) | Apple resmi %90 ≤24–48 sa; derleme ilk gönderim 2–5 gün; Play çoğu saatler–7 gün (kaynak: 2026-08 taraması, resmi+derleme, değişken) | hayır (duvar saati) |
| A10 ölçüm penceresi | organik vitalleri bekleme — bu pencerede hat BAŞKA oyun üretir (WIP dışı, A6.3) | `olcum_penceresi_gun` (örn. 14 — Ek C, şerhli) | hayır |
| A10 karar oturumu | üç-kelime karar + Ek C formu + halka raporu + PR merge | `insan_yanit_tavan_karar_gun` (taahhüt) | evet |

## 2. Tek seferlik ve ömür-boyu envanter

| Yerde | İnsan eylemi | Bekleme penceresi | Kuyruk |
|---|---|---|---|
| kurulum (-2) | UAC onayları (≥2) + tarayıcı akışı + koşullu hesaplar; kapı ön-bildirimi tek mesaj (yazılı) | BİLİNMİYOR (işlem tahmini Ek B'dedir; bekleme değil) | evet (tek sefer) |
| sonda (-1) | insan-kapisi durakları ≤10 (sayılır) + BAŞARISIZ kararı | BİLİNMİYOR — sonda ölçümünün konusu | evet |
| 0A | hesap doğrulamaları; TEK form (defter 8 eksen + L6 blokları + Ek C Bölüm-1 + insan-yanıt taahhütleri bölümü); private ikiz; sosyal hesaplar | form işlemi ~1 dk yazılı; bekleme BİLİNMİYOR | evet |
| 0B | konseptin açık onayı; darboğaz satırı yorumları; iOS imza zinciri; review gönderimi | iOS imza ≈2–4 sa + tıkanma payı (L3, yazılı); kalanı BİLİNMİYOR | evet |
| ömür boyu | yıllık target-API bakım turu (oyun başına — Ek A F4) | yıllık takvim (Ek A, yazılı) | hayır |
| ömür boyu | Ek A katalog genişletme kürasyonu (tetikte; insan onaylı) | BİLİNMİYOR (koşullu) | koşullu |
| ömür boyu | aylık yasak-liste arşivi (otonom; web yoksa insan tek cümle ile) | BİLİNMİYOR (koşullu) | koşullu |
| ömür boyu | Ek C değişimleri (tek form disiplini — L8) | istisnai | evet |

## 3. Yargılar: birleştir / kaldır / taahhüt

- **Kaldırma:** satır kaldırılamadı — her dokunuş ya veto/yargı ya hesap temsiliyetidir.
  Envanterin ana bulgusu budur: dokunuş sayısı az; maliyet bekleme zincirinde toplanıyor.
- **Taahhüt (A6.1):** kullanıcı-kaynaklı BİLİNMİYOR'lar bilinmez değil SORULMAMIŞ'tı — beş
  kalem 0A-6 TEK formunun insan-yanıt bölümünden Ek C `insan_yanit_tavan_*` alanlarına
  yazılır. Dış bilinmezler kalır: mağaza review (üçüncü taraf), halka/dış-göz yanıt hızı
  (gönüllüler — ama artık tavanlı, A6.4).
- **Birleştirme:** A10 tek oturum (karar + Ek C formu + halka raporu + PR'lar); A9 tek
  oturum (T3 + formlar + gönder); A1 veto ↔ hasat örtüklüğü yazılı; kurulum ön-bildirimi
  tek mesaj. Ek birleşme adayı bulunamadı.

## 4. Kritik bekleme zinciri, ağırlık dağılımı ve kuyruk

- **Zincir (koşu başına, sıralı):** A1 veto 24 sa → A5 pencere 48–72 sa → A8 turu (taahhüt)
  → A9 review (Apple %90 ≤48 sa / Play ≤7 gün aralığı) → A10 pencere (örn. 14 gün, şerhli).
- **Ağırlık dağılımı (A6.2):** kaba alt sınır ≈20 gün ve bunun ≈14'ü TEK kalemde: ölçüm
  penceresi. Takvimin yaklaşık üçte ikisi oyun bittikten sonra beklemektir — uydurma değil,
  yazılı pencerelerin toplamıdır. BİLİNMİYOR kalan satırlar 0B darboğaz PR'ının doldurma
  listesidir.
- **Pencere WIP dışıdır (A6.3):** A10 ölçüm penceresindeki oyun WIP'i işgal ETMEZ — Sözleşme-9
  cümlesi orada. Pencerede üretim işi ve insan kapısı yoktur (karar oturumu pencere
  sonundadır); hat bu beklemede boş durmaz. Kuyruk ≤2 buna göre de tutar: eski oyunun A10
  karar oturumu ile yeni oyunun tek insan kapısı eşzamanlı düşse bile toplam 2'dir.
