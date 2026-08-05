# FactoryGames — Üretim Hattı (PIPELINE)

**Sürüm:** v0.10 (red-team tur 1 uygulandı: B1–B6). v1.0 kilitlenmesi için iki kullanıcı
kararı bekleniyor: Play hesap tipi (Kilit Kararlar) ve `toplam_butce_usd` (Ek C).
**Amaç:** reklam gelirli mobil oyunları tekrarlanabilir, ölçülebilir ve geliştirici
hesabını koruyan bir hatla üretmek. Hattın kendisi üründür; oyunlar hattın çıktısıdır.
**Okuma kuralı:** her oyun reposunun CLAUDE.md dosyası bu belgeye ve standartlara
bağlantıyla başlar; bağlanmamış belge yok sayılır.

## Kilit Teknik Kararlar

| Karar | Seçim | Tek satır gerekçe |
|---|---|---|
| Motor | Unity 6000.3 LTS, `ProjectVersion.txt` pinli | Oyun ortasında yükseltme yasak; LTS Aralık 2027'ye destekli |
| Render | URP + 2D Renderer | Ekosistem/yol haritası URP'de; boyut stripping ile telafi |
| Mediation | AppLovin MAX | ROAS UA kampanyaları yalnız MAX publisher'larına açık |
| Analitik | GameAnalytics; MMP (AppsFlyer) ilk ÖLÇEKLE'de | Ücretsiz, hafif, D1/D7 kohortu hazır |
| Sahne | Bootstrap-only, veri `StreamingAssets` JSON | GUID-YAML kilidi yok; diff insan-okur |
| Repo | FactoryGames = fabrika + `factory.core` UPM paketi; oyunlar ayrı repo | Öldürme/mağaza/sürüm oyun başına |
| CI | Public dönemde hosted runner'lar ücretsiz; ÖLÇEKLE'de private + Linux/macOS bölüşümü | Maliyeti ölçek anına ertele. Bedel: kaynak açık → reskin/klon riski public dönemin fiyatıdır |
| Varlık | T1 çok-kaynaklı CC0 katalog + zorunlu transform; T2 sentez SFX; T3 mağaza yüzeyi (insan vetolu) | Otonomluk + "asset flip" deseninden kaçış |
| Executor | VS Code Claude Code (Opus); Unity MCP yalnız gözlemci | Kod-öncelikli kural |
| iOS | GitHub Actions macOS runner + xcodebuild + App Store Connect API key | Mac sahipliği yok; test: TestFlight internal (iPhone 15) |
| Play hesap tipi | Hedef: organizasyon — **kullanıcı kararı bekleniyor** (tüzel kişilik + D-U-N-S + org web sitesi) | Kişisel→org dönüşümü Play Console içinde mümkün ve tek yönlüdür (org→kişisel yok). Kişisel hesapta (13.11.2023 sonrası) üretim erişimi her uygulama için ≥12 testçi × 14 gün kesintisiz kapalı test ister; sayaç 12 altına düşerse sıfırlanır; açık test dahi üretim erişimine bağlıdır — fabrika takvimi kişisel hesapta yaşamaz (kural 20→12 olarak değişti, tekrar değişebilir) |

## EXECUTOR SÖZLEŞMESİ — her koşuda, tüm aşamalarda geçerli

1. **Telemetri:** her aşama giriş/çıkışında `.factory/telemetry.jsonl` satırı:
   `{ts, aşama, olay: giris|cikis|geri_kosusu, sure_dk, kapi_sonucu, factory_core_surumu, build_hash, ci_dakika}`.
   İnsan-kapısı bekleme süresi elle yazılmaz; PR/issue yorum zaman damgalarından hesaplanır.
2. **Kod-öncelikli sahne:** sahneler bootstrap-only; hiyerarşi saf C# fabrikalarından;
   tunable veri JSON; ScriptableObject üretilmez; MCP ile sahne düzenlemek yasak
   (MCP: konsol okuma, play-mode, durum doğrulama, build tetikleme).
   Zorlama: CI lint (`.unity`/`.prefab` nesne eşiği + Bootstrap dışı MonoBehaviour yasağı)
   + PR kapısı; pre-commit hook yalnız hızlı uyarıdır.
3. **Normatif yük disiplini:** CLAUDE.md en fazla 30 kural (her koşuda tam yüklenir;
   tavan CI satır sayımıyla zorlanır; her kural kaynak PR/incident no taşır; her
   koşunun kapanışında en az bir prose maddesi teste/lint'e dönüştürülür ya da
   silinir). PIPELINE.md ve standartlar için sınır **satır değil okuma kapsamıdır**:
   executor her koşuda yalnız bu Sözleşme + aktif aşamanın satırları + ilgili eki
   yükler; belge toptan okunmaz. Şişme telemetriye girer: Aşama 11 hat bakım raporu
   normatif satır delta'sını yazar; tek koşuda +50 satır üstü Sözleşme-5 yükseltme
   adayıdır. Tavanın hedefi bağlam maliyetidir, korpus boyutu değil.
4. **Sır kuralı:** repoya hiçbir sır girmez (sertifika, keystore, token); hepsi
   Actions secrets. CI secret-scan kırmızısı merge'i engeller. Public dönemde
   döndürülemeyecek sır yok (private'a geçiş fork'ları geri almaz).
5. **Hata→test yükseltmesi:** her kapı reddi ve her post-mortem bulgusu üç basamaktan
   birine yükseltilir: (a) otomatik kontrol — PR'da önce-kırmızı kanıtıyla;
   (b) kontrol listesine tek satır; (c) CLAUDE.md kuralı (son çare, tavana tabi).
6. **MCP kopması:** hiçbir zorunlu adım MCP'ye bağımlı değildir; `FALLBACK.md`'deki
   CLI eşdeğerleriyle aynen otonom devam. "MCP canlı" yalnız insan-masada debug
   oturumlarında şarttır.
7. **Öğrenme akışı:** post-mortem/öğrenme PR'ı oyun reposuna değil **FactoryGames**'e;
   PR, kullanılan `factory.core` sürümünü ve telemetri özetini içerir.
   Oyun reposu arşivlenince ders ölmez.
8. **Para kararları insana:** UA harcaması, ölçekleme, satın alma — onaysız olmaz.
   Hat bütçe **üretmez, ölçer**; birim-hedefi dosyasında olmayan sayı hiçbir kapıda
   kullanılamaz.
9. **WIP limiti:** eşzamanlı aktif oyun ≤ 2 (Aşama 1 girişinden Aşama 11 kararına
   kadar sayılır; ölçüm penceresinde bekleyen oyun WIP'i işgal eder ama insan-kapısı
   kuyruğunu işgal etmez). İnsan kapısı kuyruğunda aynı anda ≤ 2 oyun. WIP doluyken
   Aşama 1 kapısı açılmaz. Başlangıç değeri 2; telemetride insan beklemesi büyürse
   düşürülür — değer uydurma değil, ölçümden gelir.

## AŞAMALAR

Format: Girdi / Çıktı / Yürüten / Geçiş kriteri / Geri kenarı.

---

### AŞAMA 0 — Kurulum + Pilot (tek seferlik; sonraki koşularda atlanır)

**Girdi:** boş fabrika deposu; kullanıcının tavan rakamları (birim-hedefi alanları, Ek C).
**0A çıktı (hat kurulumu):** şablon repo (`factory.core` iskeleti; CI: lint, secret-scan,
test, Android build); CLAUDE.md iskeleti; FALLBACK.md; telemetry şeması; PR şablonları
(post-mortem/öğrenme); pre-mortem risk taksonomisi; rubrik şablonu; çeşitlilik defteri +
hesap-deseni envanteri iskeleti; birim-hedefi dosyası (**kullanıcı doldurur**);
başvurular (Apple Developer, Play Console, MAX/AdMob, ASC API key); Unity CI lisansı
(.alf → license.unity3d.com → .ulf → secret; gh CLI ile oyun repolarına basılır);
hesap tipi kararı (org: D-U-N-S + org web sitesi doğrulaması başlatıldı — kritik yol;
kişisel: 12-testçi kapalı test halkası kurma görevi — bu halka Aşama 9'un dış gözüdür);
dış göz halkası ≥ 2 kişi (org yolunda sabit test halkası; kişisel yolda kapalı testçi
grubundan süzülür).
Doğrulamalar (kilitleme anında): GitHub billing sayfası (public = hosted ücretsiz),
Unity güncel LTS numarası, MCP sunucusu canlı, Play 12×14 kuralının güncel testçi
sayısı ve kapsamı (kural 20→12 değişti; tekrar değişebilir — Play Console Help'ten
yazılı teyit).
**0A geçiş:** hello-build iki platformda CI'da yeşil; kasıtlı ihlal testi kanıtlı
(lint ve secret-scan gerçekten yakalıyor); tüm başvuru numaraları repo'da.
**0B önkoşul:** `toplam_butce_usd` kullanıcıdan alınmadan pilot başlamaz (Ek C).
**0B çıktı (pilot koşu):** Aşama 1–11'i yarı-elle geçen ilk oyun, iki mağazada
review'a **gönderildi** (kabul şart değil); aşama bazında darboğaz kaydı; standartlar
pilottan damıtılıp v1.0 etiketlendi; öğrenme PR'ı FactoryGames'e açıldı.
**0B geçiş:** gönderim kanıtı + darboğaz PR'ı merge + belgeler v1.0.
**Yürüten:** karma (insan yoğun: hesap/sertifika/onay insan; iskelet inşası otonom).
**Geri kenarı:** kurulum tıkanırsa (hesap reddi, lisans, fatura değişimi) bekleyen iş
insana eskalasyon olarak yazılır ve hat duraklar; limit yok — tek seferlik aşama.
Pilot oyun ölürse hat ölmez: dersler işlenir, yeni pilot Aşama 1'den başlar.

### AŞAMA 1 — Kısıtlı Fikir Üretimi ve Seçim

**Girdi:** fikir standardı; çeşitlilik defteri; hesap-deseni envanteri; o ayın yasak
listesi (üretimin ilk zorunlu adımı: top-listelerden 10 klişe mekaniği yaz → yasakla).
**Çıktı:** 3 konsept kartı (tür, çekirdek döngü, meta, kitle, **test edilebilir hipotez**,
3 en yakın rakip + benzerlik %, ≥3 eksen farkı beyanı, stil ailesi + UI kit + ikon +
reklam-matrisi seçimleri); modelin tek seçimi; insan veto kaydı (24 sa sessizlik = onay);
reddedilen kartlar sebep gösterilerek defterde.
**Yürüten:** otonom üretim + otonom ön kontrol; seçim model, veto insan (karma).
**Geçiş kriteri:** her kartın zorunlu alanları dolu; yasak listesiyle kesişim boş;
benzerlik <%40; çeşitlilik defteri (≥3 eksen) ve Ek A rotasyonu sağlanıyor;
hipotezsiz kart kapıdan düşer; yazılı seçim var.
**Geri kenarı:** kartlar geçemezse / veto gelirse → aynı aşamada yeni üretim, **max 3 tur**;
sonra insana eskalasyon (standart mı dar, havuz mu dolu — Ek A katalog görevi tetiklenir).

### AŞAMA 2 — Pazar Sinyali Testi

**Girdi:** onaylı konsept; testten **önce** birim-hedefi dosyasına yazılmış IPM/CTR
eşiği ve kapalı test bütçesi.
**Çıktı:** 2–3 reklam varyantı (veya mağaza sayfası taslağı); kampanya kurulumu;
ölçüm raporu (eşik–gerçekleşen tablosu); GEÇ/KAL kaydı.
**Yürüten:** karma — kurulum otonom; reklam hesabı ve harcama onayı insan.
**Geçiş kriteri:** bütçe aşılmadan veri penceresi kapandı; tablo yazıldı; karar kayıtlı.
**Geri kenarı:** KAL → konsept "ölü" deftere işlenir, Aşama 1'e dön; aynı konsept ikinci
kez test **edilemez**. Arka arkaya 3 KAL → hat duraklar, insana (eşik gerçekçi mi,
katalog dar mı). Pilot turda atlanabilir; atlama kararı deftere yazılır.

### AŞAMA 3 — Eksiksiz Plan

**Girdi:** sinyali (veya pilot istisnasını) geçmiş konsept.
**Çıktı:** plan belgesi — MVP kapsamı, iş kalemleri, varlık listesi + T1 aile/transform
manifesti, reklam yerleşim planı, analitik olay şeması, "bitmiş" tanımı (DoD);
**önce pre-mortem**: 10 "bu oyun nasıl batar" maddesi, taksonomi etiketli, her biri ya
planda önlem bağlantılı ya "kabul edilmiş risk + gerekçe"; önceki pre-mortem'lerle
tekrar taramasının yazılı sonucu (etiket eşleşmesi; N koşuda üst üste kabul edilen
etiket otomatik olarak Sözleşme-5 yükseltmesine gider).
**Yürüten:** otonom.
**Geçiş kriteri:** TBD sayısı **0**; her iş kaleminin ölçülebilir kabul kriteri var;
pre-mortem dört koşulu tam (10 madde, bağlantı/kabul, etiket, tekrar taraması).
**Geri kenarı:** plan kapanamıyorsa → 1. tur aynı aşamada revizyon; 2. turda konsept
belirsizliği varsayılır → Aşama 1'e dön veya insana; **max 2**.

### AŞAMA 4 — Ortam ve Araç Envanteri

**Girdi:** planın araç gereksinim listesi.
**Çıktı:** envanter raporu; eksikler kuruldu; sürüm kilidi tablosu; oyun reposu
şablondan üretildi; secrets gh CLI ile basıldı; **hello-build** (iskelet oyun) iki
platformda CI'da yeşil; MAX SDK test modunda init.
**Yürüten:** otonom (yalnız lisans/şifre/hesap anlarında insan).
**Geçiş kriteri:** tek komutla iskelet build Android + iOS yeşil; sürümler dosyada;
CI tam takım (lint, secret-scan, test) koşuyor.
**Geri kenarı:** build kırılması → aynı aşamada düzeltme, **max 5 deneme**; sonra
FactoryGames'e arıza issue'su + insana eskalasyon. Şablon/araç arızası oyunun değil
hattın hatasıdır; Sözleşme-5 yükseltme adayı otomatik açılır.

### AŞAMA 5 — Kaba Üretim: Çekirdek Döngü (gri kutu)

**Girdi:** onaylı plan; yeşil build borusu.
**Çıktı:** oynanabilir çekirdek döngü (gri görsellik); analitik olayları bağlı;
EditMode + PlayMode testleri; scripted-bot smoke testi (N tam döngü).
**Yürüten:** otonom.
**Geçiş kriteri:** DoD çekirdek maddeleri tik; bot N döngüyü hatasız oynadı;
15 dk soak'ta çökme 0, exception 0; boot testinde hiyerarşi imzası doğru.
**Geri kenarı:** kırmızı test → aynı aşamada düzeltme, **max 3 tur**; hâlâ kırmızıysa
plan hatası varsayılır → Aşama 3'e; ikinci dönüşte de kapanmazsa konsept
yaşayabilirliği insana sorulur (erken-öldür adayı).

### AŞAMA 6 — D1 Kapısı (sınırlı yayın ölçümü)

**Girdi:** çökmezliği kanıtlı gri kutu; **önkoşul: üretim veya açık test erişimi
mevcut** — kişisel Play hesabında bu, uygulama başına ≥12 testçi × 14 gün kapalı test
demektir (kapalı teste UA koşulamaz; erişim yoksa bu aşama koşulamaz, hat Aşama 5'te
bekler); Google Play sınırlı listeleme taslağı; D1 eşiği ve kapı bütçesi
(birim-hedefinden); minimum kohort büyüklüğü.
**Çıktı:** Google Play'de sınırlı yayın + küçük UA kohortu; D1/D2 tutunma raporu;
GEÇ/ÖLDÜR kararı — **öldürme yetkisi kalibrasyona tabidir**: ilk 3 koşuda
(kalibrasyon dosyası dolmadan) bu aşama ÖLDÜRMEZ, yalnız ölçer ve raporlar. Gerekçe:
gri-kutu D1'i bitmiş oyunun D1'i değildir; kalibresiz eşik iyi konseptleri öldürür
ve bu hata karşı-olgu bırakmadığı için telemetride görünmez.
**Yürüten:** karma — listeleme gönderimi ve harcama insan onaylı; kurulum + ölçüm otonom.
**Geçiş kriteri:** kohort ≥ minimum kurulum; D1 gerçekleşeni eşik tablosunda yazıldı;
karar kayıtlı (kalibrasyon öncesi "karar" = GEÇ veya insan-onaylı istisna).
**Geri kenarı:** kalibrasyon sonrası eşik altı → konsept ölür: vaka post-mortem'i
(Sözleşme 5–7) + defter güncellemesi, Aşama 1'e dön. "İyileştir" istisnası yalnız
insanda, konsept başına **1 kez**, hedefi Aşama 5. Not: iOS bu kapıda yok
(TestFlight'a UA koşulamaz); sinyal tek mağazadan alınır, Apple review riski
Aşama 10'dadır.

### AŞAMA 7 — İnce Üretim: İçerik, Görsel, Ses, Ekonomi

**Girdi:** D1'i geçmiş çekirdek.
**Çıktı:** içerik-tam build — varlık listesi %100 ve transform manifestiyle birebir
(palet dönüşümü + silüet düzeni + 1 imza öğe işli), T2 sentez SFX seti, tüm ekranlar,
ekonomi, reklam yerleşimi + ATT/GDPR rıza akışı; yaş derecesi uygunluk beyanı.
**Yürüten:** otonom.
**Geçiş kriteri:** varlık listesi eksiksiz, manifestle birebir; reklam + rıza akışı
test cihazında uçtan uca; `ad_impression` olayları telemetriye düşüyor.
**Geri kenarı:** iş kalemi/varlık yetişmiyorsa → kapsam küçültmeyle Aşama 3'e (plan
revizyonu), **max 2**; sonra insana.

### AŞAMA 8 — Kontrol ve Temizlik

**Girdi:** içerik-tam build.
**Çıktı:** hata raporu (açık kritik = 0); min-spec cihaz performans raporu; politika
ön kontrol listesi PASS — 4.3 oyun seviyesi **ve** hesap-deseni envanteriyle
karşılaştırma; analitik şema kanıtı (şemadaki her olay ≥1 kez loglandı);
screenshot paketi (yalnız Aşama 9 raporu içindir, **kapı değil**).
**Yürüten:** otonom.
**Geçiş kriteri:** kontrol listesinin tamamı yeşil; CI kapısı (lint, secret-scan,
testler, boot imza) yeşil.
**Geri kenarı:** kırmızı madde kaynak düzlemine döner: oyun kodu → Aşama 5/7;
şablon/CI → FactoryGames arıza issue'su + Sözleşme-5 yükseltmesi; **max 4 tur**;
sonra insana.

### AŞAMA 9 — İnsan Oynanış Kapısı (rubrik)

**Girdi:** QA-yeşil build; TestFlight internal + Play internal track paketi;
screenshot paketi.
**Çıktı:** 5 eksen rubrik (ilk-60-sn anlaşılırlık*, ilk-başarı hissi*, kontrol
tepkiselliği, ses-görsel doygunluk, tekrar oynama isteği — her eksen 1–5, eşikler
birim-hedefinden). \* işaretli iki eksen **kullanıcı tarafından puanlanamaz**: konsepti
Aşama 1'de onaylayan kişi ilk izlenimi ölçemez — kirlenme tekrar değil ön bilgidir.
Bu eksenler ≥ 2 dış gözden gelir (org: Aşama 0A test halkası; kişisel: kapalı testçi
grubu); kayıt `tester_id + build_hash` ile tutulur. Dış göz yoksa rubrik 3 eksene iner
ve kapı öyle işler — sahte nesnellikle 5 eksen puanlanmaz. P0/P1/P2 etiketli geri
bildirim; yazılı "yayınla" onayı.
**Yürüten:** insan kapısı (düzeltmeler otonom).
**Geçiş kriteri:** aktif eksenler (dış göz varsa 5, yoksa 3) eşik üstü VE yazılı
onay; rubrik satırı build hash'iyle telemetry'ye yazıldı.
**Geri kenarı:** eşik altı eksen ilgili aşamaya döner: işlev/tepkisellik → 5;
görsel-işitsel → 7; anlaşılırlık/akış → 3. Max **3 tur**; P0 zorunlu, P1 bütçeye tabi,
P2 sonraki sürüme ertelenir. 3. tur sonunda hâlâ eşik altı → erken-öldür kararı
insana gider (Aşama 11 ekonomisine girmeden).

### AŞAMA 10 — Mağaza Paketi ve Gönderim

**Girdi:** "yayınla" onaylı build.
**Çıktı:** imzalı AAB/IPA; T3 mağaza yüzeyi (ikon, screenshot seti, feature graphic —
insan vetolu); listeleme metinleri; yaş derecelendirme, App Privacy, Data Safety
formları gönderildi; ASC API key ile yükleme; iki mağazada review; ret-düzeltme kaydı.
**Yürüten:** insan kapısı (hesap, sertifika, "gönder" butonu, T3 veto insan;
taslaklar otonom ürer).
**Geçiş kriteri:** her formun gönderim kanıtı (kayıt no/ekran görüntüsü) repo'da;
iki mağazada "yayında" — veya 3. ret sonrası eskalasyon raporu.
**Geri kenarı:** ret → otonom analiz + düzeltme ilgili aşamaya (içerik → 7; form → 10);
**max 3 ret**. Ret sebebi 4.3/şablon şüphesiyse **hesabı koru**: gönderimler durur,
defter + envanter revizyonu + insana eskalasyon, sessizce yeniden gönderim yok.

### AŞAMA 11 — Ölçüm, Karar ve Geri-Besleme

**Girdi:** yayında oyun; birim-hedefi eşikleri; ölçüm penceresi (örn. 14 gün veya
N kurulum — birim-hedefi dosyasında).
**Çıktı:** karar raporu — **ÖLÇEKLE / TEK TUR İYİLEŞTİR / ÖLDÜR** + eşik–gerçekleşen
tablosu; kalibrasyon dosyası (gri-kutu D1 ↔ yayın D1 eşleşmeleri; 3 koşu dolunca öneri
offset = medyan fark; `d1_kalibrasyon_offset` yazımı kullanıcı onaylı — Sözleşme-8);
hat bakım raporu (telemetri: aşama süreleri, kapı ret oranları, insan beklemeleri,
CI dakikası, tavan–gerçekleşen bütçe farkı, **normatif satır delta'sı**);
çeşitlilik defteri +
hesap-deseni envanteri güncellemesi; öğrenme/post-mortem PR'ı FactoryGames'e
(factory.core sürümü + telemetri özeti içerir); ÖLDÜR'de: repo arşiv + mağazadan
çekme planı, hücre serbestliği Ek A'ya işlenir.
**Yürüten:** karma (veri ve tablolar otonom; para ve karar insan).
**Geçiş kriteri:** tek kelimelik karar + tablo + her iki rapor yazıldı; PR açıldı.
"Beklemede" kararı yoktur.
**Geri kenarı:** terminal aşama; tek geri yol **TEK TUR İYİLEŞTİR** → Aşama 7 mini
döngüsü, oyun başına en fazla 1 kez. ÖLÇEKLE aynı koşuda üç borcu da kapatır:
repo private'a geçer, MMP kurulur, CI Linux/macOS bölüşümüne döner.

---

## EK A — 4.3 Rotasyon Aritmetiği

**Eksenler:** çeşitlilik defteri 8 eksen (tür, çekirdek mekanik, kamera, oturum
uzunluğu, meta, görsel stil ailesi, kitle, reklam deseni) + hesap-deseni envanteri
4 öğe (UI kit ailesi, ikon dili, reklam yerleşim matrisi, menü akışı).

**Kurallar:**
- Yeni konsept, defterdeki her kayıttan **≥3 eksende** farklı.
- (tür × stil ailesi) hücresinde canlı oyun **≤ 1**.
- Aynı stil ailesinde canlı oyun **≤ 2** (X = 2).
- Aynı UI kit / ikon dili / reklam matrisi **arka arkaya en fazla 2 oyunda**;
  sonra soğuma: 2 oyun ara verilir.

**Havuz tabanı ve tavan:** katalogda ≥ 6 stil ailesi, ≥ 3 UI kit, ≥ 3 reklam matrisi.
Ölçek tavanı buradan doğar: 6 aile × 2 = eşzamanlı ~12 canlı görsel hücre; tür ve
mekanik çeşitlenmesiyle kaba tavan **~20 canlı oyun**.

**Havuz tükenmesi protokolü:** rotasyonu sağlayan konsept üretilemiyorsa Aşama 1
kapısı açılmaz; otomatik "katalog genişletme" görevi açılır (FactoryGames backlog
issue'su + insan onaylı T1/T3 kürasyonu); hat duraklar — kural sessizce esnetilmez.
Öldürülen oyun mağazadan çekilirse hücresi serbest kalır; defter kaydı kalıcıdır,
çekilmiş oyunun hesap-izleri rotasyon sayımında "tüketilmiş" kabul edilir.

## EK B — Kapasite Tahmini (ideal koşu, geri kenarsız)

| Aşama | Takvim |
|---|---|
| 0 Kurulum (tek seferlik) | 4–8 hafta — kritik yol: org doğrulama/D-U-N-S; kişisel yolda 1–2 hafta + her oyun için +14 gün kapalı test |
| 1 Fikir+seçim | 1 gün (veto penceresi dahil) |
| 2 Sinyal testi | 2–3 gün |
| 3 Plan+pre-mortem | 1 gün |
| 4 Envanter | 0,5 gün |
| 5 Çekirdek | 1–2 gün |
| 6 D1 kapısı | 4–5 gün (review + kohort) |
| 7 İnce üretim | 2–4 gün |
| 8 QA | 1 gün |
| 9 İnsan kapısı | 2–3 gün (tur ≤ 24 sa varsayımı) |
| 10 Mağaza+gönderim | 2–3 gün |
| 11 Ölçüm penceresi | 14 gün |

**Toplam: yayına ~14–21 gün; karara ~28–35 gün.** Kişisel Play hesabı senaryosunda
her oyuna **+≥14 gün** eklenir (12×14 kapalı test; üretim *ve* açık test erişimi buna
bağlı, kapalı teste UA koşulamaz) — takvim bu yüzden organizasyon hesabını hedefler.
**İnsan-saat/oyun ≈ 4–6 sa** (veto 0,1 + harcama onayları 0,3 + form/listeleme
inceleme 1,5 + üç tur oynama 1,5 + yayınla/karar 0,5).

Bu sayı birim-hedefi "gün/oyun" tavanıyla kıyaslanır; gerçekleşen telemetriden
okunur. Tahmin uydurma varsayılır, ölçüm gerçektir; Aşama 11 hat bakım raporu
her koşuda ikisini karşılaştırır.

## EK C — Birim-Hedefi Dosyası Şeması

**Sahibi: kullanıcı.** Hat yalnız ölçer; dosyada olmayan sayı hiçbir kapıda
kullanılamaz; değişiklik yalnız kullanıcı onayıyla.

| Alan | Anlam |
|---|---|
| `takvim_tavan_gun` | Oyun başına azami takvim günü |
| `insan_saat_tavan` | Oyun başına azami insan-saat |
| `ua_tavan_usd` | Oyun başına toplam UA tavanı |
| `sinyal_test_butcesi` | Aşama 2 kapalı bütçe |
| `d1_kapi_butcesi` | Aşama 6 kapalı bütçe |
| `ipm_esik`, `ctr_esik` | Aşama 2 GEÇ eşikleri |
| `d1_esik` | Aşama 6 GEÇ eşiği |
| `min_kohort_kurulum` | Aşama 6/11 geçerli ölçüm için asgari kurulum |
| `olcum_penceresi_gun` | Aşama 11 pencere |
| `ollekle_esik`, `oldur_esik` | Aşama 11 karar eşikleri (D7, ROAS göstergeleri) |
| `rubrik_esik` | Aşama 9 eksen bazında asgari puan |
| `toplam_butce_usd` | Fabrika toplam UA tavanı — Aşama 0B önkoşulu; yoksa pilot başlamaz |
| `paralel_ua_tavan` | Aynı anda açık tutulabilecek UA harcaması (WIP limitiyle uyumlu) |
| `d1_kalibrasyon_offset` | Gri-kutu D1 düzeltmesi; 3 koşu sonrası, kullanıcı onaylı |
| `iyilestir_hakki` | Konsept başına 1 (Aşama 6) + oyun başına 1 (Aşama 11) |
