# Kavram ön-turu 2026-08 — kura + 3 kart (kullanıcı emriyle 0B öncesi koşuldu)

**Kura:** `docs/factory/kavram/2026-08/kura.json` — `strateji × "kaynak azalır, yenilenmez" × izometrik × 30 sn`.
Yasak: `docs/standards/yasak-liste/2026-08.md` (12 ayrıştırılan satır — 10 klişe + 2 kaynak-URL satırı;
ayrıştırma gürültüsü kayıtlı, hiçbir havuz değeriyle eşleşme yok). Defter durumu: 9 güçlü + 0 zayıf.
Seçim: Açık insan onayı (0B-1; veto penceresi pilotta geçmez). Defter ≥3 eksen kontrolü:
FORM-BEKLIYOR şerhli — mevcut-oyun eksenleri dönünce Aşama 2'den önce tamamlanır.
Stil/UI/ikon/reklam seçimleri **katalog tohumu**dur (katalog henüz yok; insan onaylı kürasyon, Ek A).

---

## KART A — "Tezgâh" (çalışma adı)

- **Çekirdek döngü:** izometrik mahalle pazarı tezgâhı. Sezon stoğu oyun başında BİR KEZ verilir
  ve asla yenilenmez. Her 30 sn'lik tur = bir gün: müşteri dalgası gelir; sen tur arasında raf
  dizilimi + hangi ürünü öne çıkaracağın + kimi geri çevireceğin kararlarını verirsin. Stok biterse
  sezon biter; kalan stokla sezonu bitirmek skor getirir.
- **Meta:** günler arası tek ekran — puanla yeni raf yeri/tabela (stok yemez). 
- **Kitle:** rahat strateji/tycoon, 20-45, tek el "bir tur daha" oyuncusu.
- **K1:** 13+. Reklam: yalnız Aşama 5+ opsiyonel ödüllü video; ilk gün reklam yok.
- **K2 çekim listesi:** (i) boş tezgâh + stok sayacı, (ii) yoğun dalga + fiyat köpükleri,
  (iii) gün sonu kâr sayacı + eriyen stok, (iv) "stok bitti" sezon finali. Tek sabit izometrik açı.
- **K3 ödül takası:** 1 izleme = 1 tura mahsus müşteri-çekim tabelası. STOK VERİLMEZ (kısıt ruhu).
- **Bant beyanı:** klişe bandında DEĞİL — kalabalık, parlak, komik köpüklü; hüzünlü yalnızlık yok.
- **Hipotez:** 30 sn tur + tükenen sezon stoğu, aynı iskeletin sınırsız-stok varyantına göre
  3. tura ulaşma oranını ≥20 puan artırır (telemetry ile ölçülür).
- **Rakipler (2026-08-15, sorgu: "mobile game market shopkeeper stock management strategy short
  rounds"):** 1) Supermarket Simulator (aynı çekirdek stok/raf; fark: 3B boy-kişi, uzun oturum).
  2) Idle Furniture Tycoon (tycoon stili; fark: idle, kaynak sınırsız). 3) Builderment (üretim
  zinciri; fark: sonsuz, PC-kökenli uzun oturum). Atlananlar: DECA/SMG (borsa, oyun-dışı konu),
  Steam listeleri (PC-only), Bus Traffic Fever vb. (ok-kaçış — farklı çekirdek).
- **8 eksen:** strateji / stok tahsisi / izometrik / 30 sn tur / puan-yükseltme meta /
  `duz-geometrik` stil adayı / rahat-strateji kitlesi / opsiyonel ödüllü reklam.
- **Yasak kesişim:** boş (en yakın yasak "builder": sabit tek tezgâh, büyüyen şehir yok).
- **UI/ikon/reklam tohumu:** UI kit adayı `yuvarlak-kose-koyu-zemin`; ikon `kalin-kontur-tek-nesne`;
  reklam matrisi `menu-sonu-tek-dugme`.

## KART B — "Vardiya" (çalışma adı)

- **Çekirdek döngü:** izometrik mini atölye. Hammadde deposu oyun başında bir kez; her 30 sn bir
  vardiya dalgası: gelen siparişleri hangi sırayla karşılayacağın ve **hangilerini reddedeceğin**
  asıl karar. Ret = itibar maliyeti ama hammadde tasarrufu; yanlış sipariş = stok erimesi.
- **Meta:** vardiyalar arası tezgâh iyileştirmeleri (daha hızlı istasyon, yanılma payı).
- **Kitle:** karar-yoğun oyun sevenler; A'dan bir tık daha sert çekirdek.
- **K1:** 13+; reklam K3'tekiyle aynı çerçeve, ilk gün yok. **K2:** (i) boş tezgâhlar + dolu depo
  sayacı, (ii) üç kuyruklu sipariş dalgası, (iii) ret düğmesi anı + itibar göstergesi, (iv) vardiya
  özeti. **K3:** 1 izleme = 1 "ek çay molası" (ret itibar kaybını bir tur siler). HAMMADDE YOK.
- **Bant beyanı:** DEĞİL — renkli atölye, takım ruhu; karamsarlık yok.
- **Hipotez:** "ret hakkı" kararlarının ağırlığı, salt hız testine göre 5. vardiyaya ulaşma oranını
  yükseltir (ölçüm: ret kullanan kullanıcıların tutuş farkına karşı kullanmayanlarla karşılaştırma).
- **Rakipler (2026-08-15, sorgu: "isometric production orders time pressure strategy mobile
  workshop"):** 1) Builderment (aynı üretim çekirdeği; fark: sonsuz, uzun oturum). 2) Idle
  Furniture Tycoon (fark: idle). 3) Voxel Tycoon (PC; fark: lojistik ölçeği). Atlananlar:
  They Are Billions/Cities:Skylines II (PC/AAA), Dyson Sphere (PC), otomasyon OT zinciri (forum).
- **8 eksen:** strateji / sipariş seçme-ret / izometrik / 30 sn vardiya / istasyon-yükseltme meta /
  `duz-geometrik` stil adayı / karar-yoğun kitle / opsiyonel ödüllü reklam. **Yasak kesişim:** boş.
- **UI/ikon/reklam tohumu:** A ile aynı paket adayları (aile ortak kullanır — Ek A: aile ≤2 canlı).

## KART C — "Kovan" (çalışma adı)

- **Çekirdek döngü:** izometrik bahçe + arı kovanı. İşçi arı ömrü tükenen TEK kaynaktır (yeni
  işçi yoktur). Her 30 sn'lik tur = bir gün: hangi çiçek adasına kaç işçi göndereceğin kararı;
  uzak ada çok nektar ama daha çok işçi ömrü yer. Hedef: mevsim bitmeden kışlık bal kotası.
- **Meta:** mevsimler arası kalıcı bahçe deseni (bir sonraki mevsimin haritasına etki).
- **Kitle:** sakin ama hesaplı oyun sevenler; A/B'den daha yumuşak tempo, aynı karar yoğunluğu.
- **K1:** 9+ (şiddet yok; arı ölümleri soyut — sayaç olarak). **K2:** (i) kovan + işçi sayacı,
  (ii) ada seçimi anı (yakın az / uzak çok), (iii) işçi ömrü eriyen çubuğu, (iv) kış kota ekranı.
  **K3:** 1 izleme = 1 gün "bulutsuz gökyüzü" (işçi kaybı %te azalır). İŞÇİ VERİLMEZ.
- **Bant beyanı:** DİKKAT — "yalnız figür + solmuş dünya" bandına en yakın kart. Çıkış: bahçe
  canlı ve kalabalıktır, arılar toplu hareket eder; hüzün değil mevsim telaşı. Beyan şartıyla
  geçer; sanat turunda banda kayış izlenir.
- **Hipotez:** görünür son (kış kotası), sonsuz toplama döngüsüne göre gün başına karar sayısını
  artırır; ölçüm: gün başına ortalama ada-seçim kararı.
- **Rakipler (2026-08-15, sorgu: "mobile game beehive colony management strategy"):
  ** 1) Bee Colony (seeles.ai; fark: sonsuz skor + savunma). 2) Hive Time (desktop; fark: açık
  uçlu sim). 3) Everbee (Steam EA; fark: yarı-otomatik toplayıcı, hedefsiz). Atlananlar:
  hiçbiri 30 sn tur + tükenen işçi kullanmıyor; mobil ücretsiz listede beehive yok (fark kanıtı).
- **8 eksen:** strateji / işçi-ömrü tahsisi / izometrik / 30 sn gün / mevsim-deseni meta /
  `duz-organik-bahce` stil adayı / sakin-hesaplı kitle / opsiyonel ödüllü reklam.
  **Yasak kesişim:** boş (idle-sim değil: kaynak yenilenmez, tur sınırlı).
- **UI/ikon/reklam tohumu:** UI `yumusak-kose-acik-zemin`; ikon `kalin-kontur-tek-nesne`;
  reklam matrisi `menu-sonu-tek-dugme`.

---

**Mimarın tek seçimi:** KART A ("Tezgâh") — üretim riski en düşük (tek sahne, dalga simülasyonu),
kısıt oyuncuya en okunur biçimde yansıyor (stok sayacı her karenin kahramanı), yasak listeye uzaklığı
en net, K2 çekim listesi tek açıdan en kolay. B en yakın ikinci. C'nin bant riski kayıtlıdır.
