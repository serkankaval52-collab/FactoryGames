# EK A — 4.3 Rotasyon Aritmetiği

**Başlangıç durumu (G1):** envanter boş başlamıyor. Kullanıcının mevcut yayında
oyunu iki mağazanın envanterine de **ilk kayıt** olarak işlenir ve her sayıma
dahildir. Mevcut oyunun stil/UI/reklam deseni hücreleri dolu kabul edilir.

**Eksenler:** çeşitlilik defteri 8 eksen (tür, çekirdek mekanik, kamera, oturum
uzunluğu, meta, görsel stil ailesi, kitle, reklam deseni) + hesap-deseni envanteri
4 öğe (UI kit ailesi, ikon dili, reklam yerleşim matrisi, menü akışı).

**Kurallar:**
- Yeni konsept, defterdeki her kayıttan **≥3 eksende** farklı.
- (tür × stil ailesi) hücresinde canlı oyun **≤ 1**.
- Aynı stil ailesinde canlı oyun **≤ 2** (X = 2).
- Aynı UI kit / ikon dili / reklam matrisi **arka arkaya en fazla 2 oyunda**;
  sonra soğuma: 2 oyun ara verilir.

**İki ölüm fiili:**
- **Raf / yatırım ölümü** (varsayılan): oyun yayında kalır, yatırım durur, ölçüm
  sürer. Hücreyi İŞGAL etmeye devam eder (mağazada görünen desen büyümesin).
- **Mağaza ölümü** (nadir): yalnız 4.3-deseni/marka/yasal sebep. Çekme → hücre
  serbest kalır; defter kaydı kalıcıdır, hesap-izi "tüketilmiş" sayılmaya devam eder.

**Havuz tabanı ve tavan:** katalogda ≥ 6 stil ailesi, ≥ 3 UI kit, ≥ 3 reklam
matrisi. Eşzamanlı ~12 canlı görsel hücre (6 aile × 2); tür/mekanik çeşitlenmesiyle
kaba tavan **~20 canlı oyun**. Raf'taki oyunlar bu tavanı yer; tavan dolunca yeni
konsept için ya mağaza ölümü ya katalog genişlemesi gerekir.

**Bakım borcu ve canlı tavan (F4):** her canlı oyun, Google target-API kuralı
yüzünden yılda en az bir yeniden-derleme bakım turu borcu üretir; raf'taki oyun
yayında kaldığı için borcu SÜRER. Canlı oyun tavanı desen aritmetiği kadar bu
borcun insan-saat toplamıyla da sınırlıdır — borç, kapasiteyi aşacaksa yeni canlı
oyun açmak yerine mağaza ölümü/katalog çözümü insana gider. Aşama 10'un kapasite
hesabına ve yıllık bakım takvimine girdi budur.

**Havuz tükenmesi protokolü:** rotasyonu sağlayan konsept üretilemiyorsa Aşama 1
kapısı açılmaz; otomatik "katalog genişletme" görevi açılır (FactoryGames backlog
issue'su + insan onaylı T1/T3 kürasyonu); hat duraklar — kural sessizce esnetilmez.
Aynı protokol, Aşama 1 kurasının filtrelenmiş uzayı boşaldığında da tetiklenir:
kura yeniden çekilmez (aynı desen).
