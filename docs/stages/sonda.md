# AŞAMA -1 — SONDA (tek seferlik; 0A'dan ÖNCE)

**Amaç:** Executor (kod ajanı), Sözleşme-2 kurallarıyla (tek kaynak; sahne değiştirilmez;
JSON veri; MCP gözlemci) gri kutu döngü üretebiliyor mu — ÖLÇMEK. Ölçmeden 0A'ya girilmez.

## Önkoşullar (raporda her biri tik işaretlenir)

0. `docs/stages/kurulum.md` KAPALI — tüm araçlar kanıtlı kurulu; kurulum
   durakları bu aşamaya taşmaz.
1–4. Hub+lisans, Unity+Android modülü, git+gh, VS Code: önkoşul 0'ın içinde.
   (iOS modülü Windows'ta yok — iOS derlemesi CI'ın işi.)
5. Resmî Unity MCP köprüsü kurulum satır 8'de KANITLI. Koşuda MCP **koşullu
   ZORUNLU**: log/stack trace'in açıklamadığı ilk runtime hatada oturum AÇAR
   (`editor-acik/kapali` damgalı; gözlem + süre rapora — Sözleşme-2'nin dayanağı
   ölçülür). Hata çıkmazsa "MCP tetiklenmedi" — o da bulgu. Batchmode ile OLMAZ.
6. Görev dosyası `docs/probe/BRIEF.md` — başka ipucu yok; Deneme-1 soğuk koşudur.

## Görev (özet; tam tanım BRIEF.md'de)

Tek ekran, tek input (tap/hold), skor + fail + restart, 60–90 sn döngü; sahne
şablon varsayılanı olarak kalır; veri JSON; deterministik zaman adımlı bot ile
3 otomatik döngü; proje URP yapılandırmasıyla ayağa kalkar; batchmode yeşil.

**Proje topolojisi (değişmez):** proje repo DIŞINDA (`../probe-project`,
`-createProject` ile); sahneye elle DOKUNMAZ. URP dahil motor ayarları sürümlü
setten KOPYALANIR (`presets/unity-6000.3/`); elle ayar YOK. Repoya girenler: `unity-pin.txt`, `kaynak/`, `scene-baseline.json`;
raporun maskeli kopyası `raporlar/` kanalından (v1.3.5) — ham `rapor.md` kimlik izlidir (lockfile yolu), YEREL.
`.markers/` YERELDİR, repoya girmez — ham içerikleri raporun "Marker ham kayıtları"
tablosundadır (Sözleşme-10). Kopya BEYAZ LİSTELİ: `robocopy ../probe-project/Assets
docs/probe/kaynak *.cs *.json *.unity *.asset *.meta *.prefab *.asmdef *.asmref /S`.

**Preset çıkarma (ilk koşu):** set, Unity'nin KENDİ şablon paketinden mekanik
çıkarılır (kurulumdaki ProjectTemplates arşivi; yoksa resmî kaynak) — tek kaynak,
elle YAML yok. Komutlar rapora; set `presets/unity-<pin>/` + README commit'lenir.

**Sahne baseline'ı (ilk koşu adımı):** `-createProject` + preset kopyasından
SONRA, oyundan ÖNCE varsayılan sahnenin sha256'sı ve nesne sayısı
`docs/probe/scene-baseline.json`'a yazılır `{pin, dosya, sha256, nesne_sayisi}`.
Lint ve report.py BU KAYDA göre ölçer (kural kendini günceller); baseline
yoksa P1 ölçülemez → SARI.

**İnsan kapısı (sondada var):** tıkanma = tek cümle + `marker.py insan-kapisi`;
fark: kapı süresi T_uretim'e GİRER ve müdahale SAYILIR — tıkanmak saklanamaz.
**Sonda yetkisi:** repo + `../probe-project` alanını kapsar; kurulum yetki sınırı
yalnız kendi aşamasındadır.

## Ölçümün kaydı — beyan yok, iz var (Sözleşme-10)

Raporu executor YAZMAZ; `tools/probe/report.py` artefaktlardan ÜRETİR.

- **T_kurulum:** kurulum damgaları; karar tablosuna girmez.
- **T_uretim:** `uretim-start` (BRIEF okunduğunda İLK iş) ↔ `uretim-end` (bot
  yeşil + test XML yazıldığı an). İnsan kapısı beklemeleri dahildir.
- **T_build:** `build-start` ↔ `build-end` — `uretim-end`'den SONRA yerel Android
  build'i ayrı ölçülür (soğuk Gradle + URP shader dakikalar sürer); tabloya
  girmez, 0A CI takvimini besler. Kırılma = "araç zinciri", üretim kusuru değil.
- **Editor/MCP oturumları:** koşullu tetikle açılır; damgalar `editor-acik/kapali-N`;
  her batchmode öncesi `Temp/UnityLockfile` YOK kanıtı — varsa kalıntı ayrımı: Unity süreci YOK + dosya exclusive açılabiliyorsa hatalı-çıkış kalıntısıdır, silinir (canlı Editor DEĞİLDİR; sonda §7.5).
- **Editor dokunuşu ÖLÇÜLMEZ (H2):** sahne varsayılandan sapmadığı için elle
  kurulum oyuna etki etmez; sayım yok, kör nokta beyanı var.
- **İnsan müdahalesi:** birincil = `insan-kapisi-N` damgaları; çapraz kontrol =
  transkript mesaj sayısı. Uyuşmazlık SARI — uyuşmazlık kendisi bilgidir.
- **P1 ikilisi:** kaynak kopyasındaki her sahnenin nesne sayısı ≤ baseline sayısı;
  prefab'da >0 nesne = ihlal (izinli kök `Assets/Prefabs/` hariç, v1.0.6). + CI lint.
- **Test/bot:** NUnit XML (batchmode `-runTests`; editmode + playmode takımları).

Rapor içeriği: üç kronometre, müdahale iki sayıyla, MCP satırı (veya
"tetiklenmedi"), baseline + P1 sayımları, test özeti, lockfile, kör nokta beyanı.

## Sayısal karar tablosu (ilk sonda bu eşikleri de kalibre eder)

- **BAŞARILI:** döngü + testler yeşil VE T_uretim ≤ 6 sa VE insan-kapisi ≤ 10 VE P1 temiz.
- **SARI:** çalışıyor ama T_uretim 6–12 sa veya insan-kapisi 11–20 veya sayım
  tutarsızlığı → 0A'ya geçilebilir; Ek B Aşama-4 satırı gerçekleşenle yazılır.
- **BAŞARISIZ:** T_uretim > 12 sa veya insan-kapisi > 20 veya bot 3 döngüyü
  geçemiyor veya P1 ihlali → 0A'ya GİRİLMEZ.

## İki denemenin farkı

- **Deneme-1 (soğuk):** yalnız BRIEF + bu ağaç. Engel sınıfı: brief / ortam / prensip.
- **Kural: brief'e insan dokunmaz** — kusur KEŞİFTİR (brief = plan→kod devir
  minyatürü); düzeltme executor'a: "uygulanabilir kıl, sonra uygula"; rapora işlenir.
- **Deneme-2:** değişen tek şey ortam/destek; brief'i değiştiren executor'dır,
  kaydedilir. Otomatik üçüncü deneme YOK.
- **İlk koşu teyitleri (bulgu olabilir):** RuntimeInitializeOnLoadMethod sırası; baseline yazıldı;
  şablon paketi konumu; + raporla ortam kusuru sınıfı taraması (yerel ayar, kodlama, yol ayıracı, satır sonu) — aksi bulgudur.

**Yürüten:** otonom — insan yalnız deklare kapılarda (sayılır) ve nihai BAŞARISIZ kararında; rapor script ürünüdür, beyan yok.
**Geçiş kriteri:** BAŞARILI veya SARI + rapor script ürünü + Ek B Aşama-4 satırı ölçümle.
**Geri kenarı:** BAŞARISIZ → 0A kilitli; max 2 deneme.
