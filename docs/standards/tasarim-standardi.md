# TASARIM STANDARDI — Aşama 1/2 kapılarının zorunlu alanları (ürün tanımı v1.0.5)

Bu dosya "küçük ama gerçek oyun" tanımının ölçülebilir karşılığıdır. Alanları
**executor** doldurur; kapı yalnız "dolu ve tutarlı mı" diye bakar. Estetik/tat
yargısı bu standardın konusu değildir — Aşama 8 rubriğinindir; burada yargı
isteyen madde YOKTUR. Kısaltma: K = konsept kartı alanı, B = GDD bölümü.
Sayısal sınırların kaynağı Ek C'dir (Sözleşme-8); bu dosya yapıyı tanımlar.
Kapsam (A3.6 — v1.0.17'de tek-dil kararı geri alındı): ilk sürüm İKİ dilde
çıkar — İngilizce + Türkçe (Ek C `ilk_surum_diller`; mağaza listelemesi aynı
iki dilde). Yerelleştirme YAPISI ilk günden zorundur: koda gömülü kullanıcı
metni bulunamaz (lint kapısı — kod-standardi §6). Çok dil genişlemesi Aşama
10'un parasal olmayan ölçekleme kalemidir.

## Bölüm A — Konsept kartı ek alanları (Aşama 1 çıktısına eklenir; 3 alan)

- **K1 Hedef yaş beyanı + reklam modeli etkisi:** kart ikisinden birini işaretler:
  "genel kitle" veya "Families/Kids kapsamı". Families seçilirse kart, reklam
  modelinin nasıl değiştiğini de yazar (yalnız sertifikalı ağlar + kişiselleştirme
  kapalı → belirgin düşük eCPM beklentisi). Stil ailesi seçimi bu beyanla tutarlı
  olmak zorundadır — stil seçimi bir gelir kararıdır (E1).
- **K2 Keşif videosu çekim listesi:** 15–45 sn'lik organik video için ≥3 sahnelik
  çekim planı (kanca / çekirdek döngü / doruk). Videosu yazılamayan konsept
  kapıdan geçemez — organik video hattın tek büyüme kanalıdır; dağıtım pazarlama
  aşaması değil, tasarım girdisidir (F1).
- **K3 Ödül takası:** oyuncunun gerçekten isteyeceği tekil ödül (ikinci şans,
  çarpan, kilit açma) + karşılığında gösterilecek reklam biçimi. Takasın değeri
  B3'te sayılandırılır; takası olmayan konsept geçemez — reklam döngünün
  parçası olarak tasarlanır, sonradan yapıştırılmaz (E4).

## Bölüm B — GDD zorunlu bölümleri (Aşama 2 plan belgesi; 8 bölüm + açılış kuralı)

- **B0 Kanıtla başlama (devir yaması):** GDD konseptle değil KANITLA açılır — ilk
  bölüm B8'in simülasyon çıktı tablosudur (ne ölçüldü / sonuç / tasarıma etkisi /
  hangi kilitli karar geri alındı); B3 sayıları bu tablodan alıntılanır. Sabitle
  oynamaya kalkan uygulayıcı ilk okuduğu şeyde neden değiştiremeyeceğini görür.

- **B1 FTUE:** ilk 60 saniyenin adım adım akışı; her adım "metin okumadan
  anlaşılır mı" işaretli. Okuma gerektiren adım ya metinsizleştirilir ya açıkça
  gerekçelendirilir (E2).
- **B2 Ekran listesi + wireframe:** zorunlu ekranlar — ana menü, ayarlar
  (ses/müzik anahtarları), duraklat, gizlilik politikası bağlantısı, oyun-sonu
  (kazan/kaybet). Her ekran tek-kutu wireframe + geçiş okları. **Durum sütunu
  (P4 kapısı — A2.6):** yükleme, izin isteme (ATT/GDPR), ağ hatası, boş içerik,
  hata — her durumda ekranda ne gösterileceği yazılır; sistem izin penceresi
  açıkken arkadaki içerik de tanımlıdır. Son satır: kayıt dayanıklılığı beyanı
  ("ilerleme yalnız yerel, bulut yok" veya bulut şeması)(E7) + renk-yalnız-bilgi
  beyanı (G6): tehlike/vurgu ayrımının biçim/ikon desteği — ikili satır.
  **Metin diyeti (A3.6):** kullanıcıya görünen metin ekran başına asgaridedir;
  sayı ve ikon tercih edilir — metinsiz tasarım en ucuz yerelleştirmedir.
- **B3 Matematik modeli:** zorluk eğrisi (seviye/dakika başarısızlık oranı hedefi),
  ilerleme temposu, hedef oturum uzunluğu + oturum/gün, ekonomi dengesi (kaynak
  giriş-çıkış tablosu), doğal reklam anı yoğunluğu (oturum başına). Hepsi SAYI;
  "dengeli olur" türü cümle TBD sayılır (E5).
- **B4 Analitik olay haritası:** B3'ün her sayısal iddiası ↔ isimlendirilmiş olay
  (snake_case, tek kaynak). CI kapısı: GDD olay listesi ile koddaki event
  gönderimleri grep-paritesinde (F6). Zorunlu sabit satır: `sessiz_toparlanma`
  (P5) — her GDD'de bulunur ve koddaki gönderimi pariteye dahildir (A2.5).
- **B5 Reklam planı:** her yerleşim için satır: tür, tetikleyici, sıklık sınırı.
  Sınırlar Ek C `reklam_siklik_tavan` / `reklam_arasi_min_sn` sınırlarını aşamaz;
  aşan satır kapıdan döner (E3).
- **B6 Ses listesi + boyut bütçesi:** zorunlu set (çekirdek geri bildirim, kazan,
  kaybet, UI dokunuşları) + müzik; dosya biçimiyle; toplam MB tavanı. Sessizde-
  oynama notu: kritik geri bildirim yalnız sese bağlanamaz (F5).
- **B7 Cihaz/çözünürlük matrisi:** matrisin SAYISAL içeriği Ek C'dedir (A3.7 —
  Sözleşme-8): en-boy min/max aralığı, tablet ve katlanabilir kapsamı, çentik
  varsayımı (`ekran_*`), asgari dokunma hedefi mm (`dokunma_hedef_min_mm`),
  asgari test hücresi sayısı (`ekran_matris_min_hucre`); her ekran matrisin tüm
  hücrelerinde taşmadan çizilir. Kanıt red-flag R9'da verilir (G1). Hedef kare
  hızı beyanı da bu bölümdedir (Ek C `premium_kare_hizi_secenek` — P6'nın
  bütçesinin kaynağı; A2.3).
- **B8 Denge doğrulayıcısı (devir yaması):** "iki modelin mutabakatı tek
  simülasyondan zayıf kanıttır" — B3'ün her SAYISI `tools/denge_sim.py` çıktısından
  gelir (oyun reposunda taşınır; içerik domain'e göre değişir, yapı sabittir:
  (i) ürünü etkileyen sabitler dosyanın en üstünde, tek yerde; (ii) çekirdek
  kuralı modelleyen minimal fonksiyon; (iii) ≥3 alternatif değerin yan-yana
  karşılaştırması; (iv) açık eşikli PASS/FAIL + GDD'den bu dosyaya atıf). Simüle
  edilemeyen sayı "simüle edilemez, gerekçe: …" satırı taşır; gerekçesiz tahmin
  sayı = kırmızı. Değişim kontrolü: sabit değişirse sim yeniden koşar; sayının
  hangi bantta kalması gerektiği GDD'ye yazılır; kapı A7 CI listesinde ve A9
  gönderim öncesinde tekrar koşar (tek seferlik değildir).

## Kapı disiplini

Eksik alan, TBD veya çapraz tutarsızlık (ör. B5 sınırının Ek C'yi aşması, K1
beyanıyla stil ailesinin çelişmesi) = kapıdan dönme. B3 sayısı için kaynak denetimi (B8):
`denge_sim.py` çıktısı veya gerekçeli "simüle edilemez" satırı — ikisi de yoktur. Doğruluk/tat
ölçümü artık simülasyondadır (devir yaması); bu standart varlık + tutarlılık + kaynak ölçer. "Çevrilemeyen" maddeler (gerçekten oyun mu,
profesyonel mi, zanaat iyi mi) bilinçli yoktur: vekilleri Bölüm A/B'de, yargıları
Aşama 8'dedir.
