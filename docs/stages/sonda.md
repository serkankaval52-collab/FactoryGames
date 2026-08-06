# AŞAMA -1 — SONDA (tek seferlik; 0A'dan ÖNCE)

**Amaç:** Claude Code'un Sözleşme-2 kurallarıyla (sahne el değmeden şablon
varsayılanı; tüm kurulum `[RuntimeInitializeOnLoadMethod]` ile kodda; JSON veri;
MCP yalnız gözlem) gri kutu döngü üretip üretemediğini ÖLÇMEK. Ölçmeden 0A'ya
girilmez.

## Önkoşullar (raporda her biri tik işaretlenir)

0. `docs/stages/kurulum.md` KAPALI — tüm araçlar kanıtlı kurulu; kurulum
   durakları bu aşamaya taşmaz.
1–4. Hub+lisans, Unity+Android modülü, git+gh, VS Code: önkoşul 0'ın içinde.
   (iOS modülü Windows'ta yok — iOS derlemesi CI'ın işi.)
5. Resmî Unity MCP köprüsü kurulum satır 8'de KANITLI. Koşuda MCP **koşullu
   ZORUNLU**: log/stack trace'in açıklamadığı ilk runtime hatada oturum AÇAR
   (`editor-acik/kapali` damgalı; ne gözlemlendi + süre rapora — MCP zaman
   kazandırıyor mu ölçülüyor, Sözleşme-2'nin dayanağı). Hata hiç çıkmazsa
   rapora "MCP tetiklenmedi" — o da bulgu. Oturum batchmode ile eşzamanlı OLMAZ.
6. Görev dosyası `docs/probe/BRIEF.md`. Başka ipucu/yol haritası kullanılmaz —
   Deneme-1 soğuk koşudur.

## Görev (özet; tam tanım BRIEF.md'de)

Tek ekran, tek input (tap/hold), skor + fail + restart, 60–90 sn döngü; sahne
şablon varsayılanı olarak kalır (nesne eklenemez); veri JSON; deterministik
zaman adımlı bot ile 3 otomatik döngü; Windows batchmode'da testler yeşil.

**Proje topolojisi (değişmez):** proje repo DIŞINDA, kardeş dizin `../probe-project`
— `-createProject` ile Unity üretir; executor yalnız .cs/.json ekler; sahneye ve
ProjectSettings'e elle DOKUNMAZ. Repoya girenler: `docs/probe/` altında rapor,
`.markers/`, `unity-pin.txt` ve `kaynak/` (.cs/.json/.unity kopyası; rapordan hemen
önce: `robocopy ../probe-project/Assets docs/probe/kaynak *.cs *.json *.unity /S`).

**İnsan kapısı (sondada var):** tıkanma = tek cümle + `marker.py insan-kapisi`.
Kurulum kapılarından farkı: kapı süresi T_uretim'e GİRER ve müdahale SAYILIR —
tıkanmak saklanamaz, ölçülür. Beklenti 0'dır; çıkarsa ölçülmüş bulgudur.

## Ölçümün kaydı — beyan yok, iz var (Sözleşme-10)

Raporu executor YAZMAZ; `tools/probe/report.py` artefaktlardan ÜRETİR.

- **T_kurulum:** kurulum damgaları; karar tablosuna girmez.
- **T_uretim:** `uretim-start` (BRIEF okunduğunda İLK iş) ↔ `uretim-end` (bot
  yeşil + test XML yazıldığı an). İnsan kapısı beklemeleri dahildir.
- **T_build:** `build-start` ↔ `build-end` — `uretim-end`'den SONRA koşulan yerel
  Android build'i ayrı ölçülür (soğuk Gradle/IL2CPP dakikalar sürer); tabloya
  girmez, 0A CI takvimini besler. Build kırılması = "araç zinciri", üretim kusuru değil.
- **Editor/MCP oturumları:** yukarıdaki koşullu tetikle açılır; damgalar
  `editor-acik/kapali-N`; her batchmode öncesi `Temp/UnityLockfile` YOK kanıtı.
- **Editor dokunuşu ÖLÇÜLMEZ (H2):** sahne varsayılandan sapmadığı için elle
  kurulum oyuna zaten etki etmez; sayım metriği yok, kör nokta beyanı var.
- **İnsan müdahalesi:** birincil sayım = `insan-kapisi-N` damgaları; çapraz
  kontrol = transkriptteki insan mesajı sayısı. Uyuşmazlık SARI — uyuşmazlık
  kendisi bilgidir.
- **P1 ikilisi:** kaynak kopyasındaki sahne/prefab GameObject sayımı ≤ 2
  (şablon varsayılanı; report.py) + CI lint. Kopya yoksa P1 ölçülemez → SARI.
- **Test/bot:** NUnit XML (batchmode `-runTests`; editmode + playmode takımları).

Rapor içeriği: T_kurulum/T_uretim/T_build, müdahale iki sayıyla, MCP oturum
satırı (veya "tetiklenmedi"), P1 sayımları, test özeti, lockfile durumu, kör
nokta beyanı.

## Sayısal karar tablosu (ilk sonda bu eşikleri de kalibre eder)

- **BAŞARILI:** döngü + testler yeşil VE T_uretim ≤ 6 sa VE insan-kapisi ≤ 10
  VE P1 temiz. (T_build ve transkript çapraz kontrolü tabloya girmez.)
- **SARI:** çalışıyor ama T_uretim 6–12 sa veya insan-kapisi 11–20 veya sayım
  tutarsızlığı → 0A'ya geçilebilir; Ek B Aşama-4 satırı gerçekleşenle yazılır.
- **BAŞARISIZ:** T_uretim > 12 sa veya insan-kapisi > 20 veya bot 3 döngüyü
  geçemiyor veya P1 ihlali → 0A'ya GİRİLMEZ.

## İki denemenin farkı

- **Deneme-1 (soğuk):** yalnız BRIEF + bu doküman ağacı. Başarısızsa engel
  listesi üçe sınıflandırılır: brief kusuru / ortam kusuru / prensip kusuru.
- **Kural: brief'e insan tasarımcı dokunmaz.** BRIEF kusuru KEŞİFTİR — brief
  fabrikanın plan→kod devir minyatürüdür; fabrikada planı da Claude Code yazar.
  Elle iyileştirilmiş brief "Claude üretebilir mi"yi değil "ben brief yazabilir
  miyim"i ölçer. Kusur varsa düzeltme de executor'a: "brief'i uygulanabilir kıl,
  sonra uygula" — revizyon rapora işlenir.
- **Deneme-2:** değişen tek şey ortam/destek (MCP, kurulum notları, iskelet);
  brief'i değiştiren executor'dır, kaydedilir. Otomatik üçüncü deneme YOK.
- **İlk koşu teyitleri (bulgu olabilir):** RuntimeInitializeOnLoadMethod 6000.3'te
  beklenen sırada; şablon sahnesi = 2 GameObject; bot adımı deterministik — aksi bulgu.

**Yürüten:** otonom — insan yalnız deklare kapılarda (sayılır) ve nihai
BAŞARISIZ kararında; rapor script ürünüdür, beyan yok.
**Geçiş kriteri:** BAŞARILI veya SARI + rapor script tarafından üretildi +
Ek B Aşama-4 satırı ölçümle güncellendi.
**Geri kenarı:** BAŞARISIZ → 0A kilitli; max 2 deneme.
