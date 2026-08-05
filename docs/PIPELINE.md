# FactoryGames — Üretim Hattı (PIPELINE)

**Sürüm:** v0.12 — K4 kullanıcı kararı (çapraz tanıtım tamamen yasak), D1 halka
standardı, D2 organik kit zorunluluğu, Aşama -1/0 mikro adımları.
**Dosya düzeni:** bu dosya yalnız sözleşme + kilit kararlar + indeks içerir. Aşama
metinleri `docs/stages/`, ekler `docs/appendix/` altındadır. Bu dosyaya aşama metni
yazmak yasaktır. `docs/_full.md` insan okuması için CI tarafından üretilir; elle
düzenlenmez.
**Okuma kapsamı:** executor her koşuda bu dosyayı + `docs/stages/<aktif>.md` +
gerekli eki yükler. Başka dosya açmaz. Oyun repolarının CLAUDE.md'si bu dosyaya
bağlantıyla başlar.

## Çerçeve (G1/G2 sonrası)

Hesaplar hazır (her iki mağazada bireysel, yayında oyun, AdMob aktif) ve düzenli UA
bütçesi yok. Hattın sermayesi para değil: **takvim, insan-saat ve dış-halka dikkati**.
Amaç: sıfıra yakın maliyetle çok deneme üretmek, hızlı rafa kaldırmak, organik tutanı
görünce — yalnız o zaman — istisnai yatırım sormak. Para standart girdi değildir;
Aşama 10'daki yatırım ofisinin konusudur. Pahalı hata "iyi konsepti öldürmek" değil,
"kötü konsepti parlatmak"tır; kapılar pahalı artefaktın önüne konur. "Öldür" ikiye
ayrılır: **raf** (varsayılan, geri alınabilir) ve **mağaza ölümü** (yalnız
4.3-deseni/marka/yasal sebep). Tek büyüme kanalı organiktir (sosyal medya +
mağaza keşfi); tek kontrollü ölçüm kanalı dış halkadır — ikisi de tükenen kuyudur,
envanterleri Ek C'de izlenir.

## Kilit Teknik Kararlar

| Karar | Seçim | Tek satır gerekçe |
|---|---|---|
| Motor | Unity 6000.3 LTS, `ProjectVersion.txt` pinli | Oyun ortasında yükseltme yasak |
| Render | URP + 2D Renderer | Ekosistem/yol haritası; boyut stripping ile telafi |
| Mediation | AppLovin MAX (AdMob hesabı adaptörle bağlanır) | ROAS UA yalnız MAX'te; mevcut oyunun AdMob kurulumuna DOKUNULMAZ |
| Analitik | GameAnalytics; MMP (AppsFlyer) istisnai UA durumunda | Ücretsiz, hafif, D1/D7 hazır |
| Sahne | Bootstrap-only, veri `StreamingAssets` JSON | GUID-YAML kilidi yok; diff insan-okur |
| Repo | FactoryGames = fabrika + `factory.core` UPM; oyunlar ayrı repo | Raf/mağaza/sürüm kararı oyun başına |
| CI | Public dönemde hosted runner ücretsiz; ÖLÇEKLE'de private | Bedel: kaynak açık → reskin/klon riski public dönemin fiyatı |
| Varlık | T1 çok-kaynaklı CC0 + zorunlu transform; T2 sentez SFX; T3 mağaza yüzeyi (insan vetolu) | Otonomluk + "asset flip" deseninden kaçış |
| Executor | VS Code Claude Code (Opus); Unity MCP yalnız gözlemci | Kod-öncelikli kural |
| iOS | GH Actions macOS runner + xcodebuild + ASC API key | Test: TestFlight internal (iPhone 15) |
| Hesaplar | Mevcut bireysel Play + Apple hesapları (ikisinde de yayında oyun); org dönüşümü = ÖLÇEK borcu | Kişisel→org Console içinde tek yönlü mümkün; aciliyet yok. 0A doğrulaması: yeni uygulamada üretim sekmesi açık mı |
| Mevcut oyun | Hattın dışında, dokunulmaz | Kullanıcı kararı (K4): oyunlar arası çapraz tanıtım her koşulda YASAK; tanıtım yalnız organik |
| Eş-konum bedeli | Fabrika oyunları mevcut oyunla AYNI hesapta yayınlanır; 4.3/spam incelemesi hesaptaki TÜM uygulamaları torbalar | Ayrı hesap kaçış değil — mağazalar aynı kişinin hesaplarını ilişkilendirir, kaçış denemesi riski büyütür; bu yüzden Ek A rotasyon kuralları esnetilemez |

## EXECUTOR SÖZLEŞMESİ — her koşuda, tüm aşamalarda geçerli

1. **Telemetri:** her aşama giriş/çıkışında oyun reposunda `.factory/telemetry.jsonl`
   satırı: `{ts, aşama, olay, sure_dk, kapi_sonucu, insan_saat, factory_core_surumu,
   build_hash, ci_dakika}`. İnsan beklemesi yorum zaman damgalarından hesaplanır.
2. **Kod-öncelikli sahne:** bootstrap-only; hiyerarşi saf C#; veri JSON; MCP ile sahne
   düzenlemek yasak (MCP: konsol, play-mode, doğrulama, build tetikleme). Zorlama:
   CI lint + PR kapısı; pre-commit hook yalnız hızlı uyarı.
3. **Normatif yük:** CLAUDE.md ≤ 30 kural, her koşuda tam yüklenir, satır sayımı CI'da;
   her koşu kapanışında ≥1 prose maddesi teste döner ya silinir. Bu ağacın disiplini
   dosya sınırıdır: stage dosyası ≤ 90 satır, PIPELINE.md ≤ 140; aşım CI uyarır ve
   Sözleşme-5 yükseltme adayı açar. Okuma kapsamı yukarıda tanımlı; toptan okuma yok.
4. **Sır kuralı:** repoya sır girmez; Actions secrets + CI secret-scan.
5. **Hata→test yükseltmesi:** her kapı reddi ve post-mortem bulgusu: (a) lint/test
   (önce-kırmızı kanıtlı PR), (b) kontrol listesine tek satır, (c) CLAUDE.md kuralı
   (son çare, tavana tabi). Kayıt kaynak PR no taşır.
6. **MCP kopması:** zorunlu adım MCP'ye bağımlı olamaz; `FALLBACK.md` CLI eşdeğerleri
   geçerlidir.
7. **Öğrenme akışı:** post-mortem/öğrenme PR'ı FactoryGames'e; `factory.core` sürümü
   ve telemetri özeti içerir. Oyun reposu arşivlenince ders ölmez.
8. **Para:** hat standart akışta **para harcamaz**; para yalnız Aşama 10 yatırım
   ofisi + kullanıcı onayıyla, Ek C Bölüm-2 sınırlarında açılır. Oyunlar arası çapraz
   tanıtım her koşulda **yasaktır** (kullanıcı kararı; bu dosyada hiçbir alan bunu
   açamaz). Hat bütçe üretmez, ölçer; Ek C'de olmayan sayı hiçbir kapıda kullanılamaz.
9. **WIP limiti:** eşzamanlı aktif oyun ≤ 2 (Aşama 1 girişinden Aşama 10 kararına);
   insan kapısı kuyruğu ≤ 2; WIP doluyken Aşama 1 açılmaz. Değer telemetriden ayarlanır.

## Aşama İndeksi

| Dosya | Aşama | Amaç (tek satır) |
|---|---|---|
| `docs/stages/sonda.md` | -1 (tek seferlik) | Üretilebilirlik ölçümü; başarısızsa 0A'ya girilmez |
| `docs/stages/0A.md` | 0A (tek seferlik) | Hat kurulumu: teyitler, şablon, CI kanıtları, standartlar |
| `docs/stages/0B.md` | 0B (tek seferlik) | Pilot koşu: standartların damıtıldığı ilk tam tur |
| `docs/stages/1.md` | 1 | Kısıtlı fikir üretimi, seçim, koşullu yorum hasadı |
| `docs/stages/2.md` | 2 | Eksiksiz plan + pre-mortem |
| `docs/stages/3.md` | 3 | Ortam/araç envanteri + hello-build |
| `docs/stages/4.md` | 4 | Gri kutu çekirdek döngü |
| `docs/stages/5.md` | 5 | Halka kapısı: parlatmadan önce nitel kanıt |
| `docs/stages/6.md` | 6 | İnce üretim: içerik, görsel, ses, ekonomi |
| `docs/stages/7.md` | 7 | Kontrol ve temizlik |
| `docs/stages/8.md` | 8 | İnsan rubrik kapısı |
| `docs/stages/9.md` | 9 | Mağaza paketi, standart organik kit, gönderim |
| `docs/stages/10.md` | 10 | Karar (raf/iyileştir/mağaza-öldür) + yatırım ofisi |

Ekler: `docs/appendix/A.md` (4.3 rotasyon aritmetiği), `docs/appendix/B.md`
(kapasite), `docs/appendix/C.md` (kaynak dosyası şeması).

**Numara kayması notu (v0.10 → v0.11):** eski Aşama 2 (paralı sinyal testi) düştü —
G2 + C2: kapı ucuz artefaktın önünde duruyordu; sosyal kanal Aşama 9'un organik
kitine taşındı. Eski 3→2, 4→3, 5→4, 6→5, 7→6, 8→7, 9→8, 10→9, 11→10.
