# AŞAMA -1 — SONDA (tek seferlik; 0A'dan ÖNCE)

**Amaç:** Claude Code'un Sözleşme-2 kurallarıyla (bootstrap-only, JSON veri, MCP
yalnız gözlem) gri kutu döngü üretip üretemediğini ÖLÇMEK. Ölçmeden 0A'ya girilmez.

## Önkoşullar (raporda her biri tik işaretlenir)

0. `docs/stages/kurulum.md` KAPALI — tüm araçlar kanıtlı kurulu. Kurulum
   durakları bu aşamaya taşmaz (T_uretim dışı).
1–4. Hub+lisans, Unity+Android modülü, git+gh, VS Code+Claude Code: tamamı önkoşul
   0'ın içindedir, tekrar listelenmez. Not: iOS modülü Windows'ta yok — iOS
   derlemesi CI'ın işi.
5. Resmî Unity MCP köprüsü `kurulum.md` satır 8'de KANITLI (önkoşul 0'ın parçası).
   Koşu içinde MCP kullanımı **SEÇİMLİDİR**: yalnız deklare EDITOR OTURUMU'nda
   (batchmode ile eşzamanlı OLMAZ — iki-durum, PIPELINE); kullanılmazsa rapora
   düşülür. MCP kanıtı kurulumdan geldiğinden MCP'siz sonda hattı eksik test ETMEZ;
   üretim FALLBACK'ı Sözleşme-6.
6. Görev dosyası `docs/probe/BRIEF.md`. Başka ipucu/yol haritası kullanılmaz —
   Deneme-1 soğuk koşudur.

## Görev (özet; tam tanım BRIEF.md'de)

Tek ekran, tek input (tap/hold), skor + fail + restart içeren 60–90 saniyelik
döngü; bootstrap-only sahne; veri JSON; bot ile 3 otomatik döngü; Windows
play-mode'da hatasız.

## Ölçümün kaydı — beyan yok, iz var (Sözleşme-10)

Raporu executor YAZMAZ; `tools/probe/report.py` artefaktlardan ÜRETİR.
Executor'un tek iz görevi: doğru anda `tools/probe/marker.py` koşturmak ve
kanıt koşularını `-batchmode`'da tutmak.

- **T_kurulum:** `.markers/kurulum-start.ts` ↔ `kurulum-end.ts` (kurulum.md
  damgaları). Karar tablosuna GİRMEZ; 0A takvimini besler.
- **T_uretim:** `.markers/uretim-start.ts` ↔ `uretim-end.ts`. Kural: BRIEF'i
  okuyan executor'ın İLK işi `python tools/probe/marker.py uretim-start`;
  son test çıktısı yazıldığında `uretim-end`. Süre = damga farkı.
- **Editor dokunuşu ÖLÇÜLMEZ (H2):** P1 altında sahneler neredeyse değişmediği
  için git izine dayalı sayım kördü — DÜŞÜRÜLDÜ; ölçemediğimizi ölçüyormuş gibi
  yapmayız. Yerine: (a) P1 ikili kapısı (aşağıda); (b) iki-durum — her Editor
  oturumu `marker.py editor-acik/editor-kapali` ile damgalı, her batchmode öncesi
  `Temp/UnityLockfile` YOK kanıtı raporda; (c) kanıt koşuları batchmode'dadır:
  GUI'siz süreçte insan dokunamaz.
- **İnsan müdahalesi:** oturum transkriptinden insan yazılı mesaj sayısı —
  sayımı script yapar, executor saymaz. Kurulum kapısı durakları pencerenin
  dışındadır ve sayıma girmez.
- **P1 ihlali:** CI lint + script'in sahne nesne sayımı (Bootstrap dışı
  GameObject > 3). Beyan gerekmez.
- **Test/bot:** NUnit XML (batchmode `-runTests`). **Kurulum durakları:** T_uretim dışı (F2).

Rapor içeriği: T_kurulum, T_uretim, müdahale, P1 sayımları, test özeti,
iki-durum izleri (Editor oturum damgaları + lockfile kanıtı) ve **kör nokta
beyanı** — Editor GUI dokunuşu ölçülemiyor; ölçülmeyen bu alan beyanla kayıtlı,
P1 ikilisi + iki-durum + batchmode disipliniyle sınırlı.

## Sayısal karar tablosu (ilk sonda bu eşikleri de kalibre eder)

- **BAŞARILI:** döngü + testler yeşil VE T_uretim ≤ 6 sa VE müdahale ≤ 10 VE
  P1 sayımı temiz.
- **SARI:** çalışıyor ama T_uretim 6–12 sa veya 11–20 müdahale → 0A'ya
  geçilebilir; Ek B'nin Aşama-4 beklentisi gerçekleşenle yazılır, P1 sürtünmesi
  Sözleşme-5 kaydı açılır.
- **BAŞARISIZ:** T_uretim > 12 sa veya > 20 müdahale veya bot 3 döngüyü
  geçemiyor veya P1 ihlali (sahne Editor'de kurulmak zorunda kaldı) →
  0A'ya GİRİLMEZ.

## İki denemenin farkı

- **Deneme-1 (soğuk):** yalnız BRIEF + bu doküman ağacı. Başarısızsa engel
  listesi üçe sınıflandırılır: brief kusuru / ortam kusuru / prensip kusuru.
- **Kural: brief'e insan tasarımcı dokunmaz.** BRIEF kusuru bir KEŞİFTİR —
  BRIEF, fabrikanın plan→kod devir mekanizmasının minyatürüdür ve fabrikada
  brief'i (planı) yazan da Claude Code olacaktır. Brief'i elle iyileştirip
  Deneme-2'yi geçmek bu keşfi gizler; ölçülen şey "Claude Code üretebilir mi"
  değil "ben iyi brief yazabilir miyim" olur. Brief kusuru bulunduysa düzeltme
  işi de executor'a verilir: "bu brief'i uygulanabilir hale getir, sonra
  uygula." Revizyon executor ürünü olarak rapora işlenir.
- **Deneme-2:** değişen tek şey ortam/destektir (MCP konfigürasyonu, kurulum
  notları, iskelet desteği). Brief değiştiyse değiştiren executor'dır ve bu
  ayrıca kaydedilir — değişken yine tektir: destek.
- **Deneme-2 de başarısızsa** karar tamamen insana + fabrikaya (motor ve/veya
  Sözleşme-2 yeniden açılır).
- Otomatik üçüncü deneme YOK.

**Yürüten:** otonom — insan yalnız kurulum kapılarında (varsa) ve nihai BAŞARISIZ
kararında; sayım ve rapor script ürünüdür, executor beyan üretmez.
**Geçiş kriteri:** tabloya göre BAŞARILI veya SARI + rapor **script tarafından**
üretildi (`docs/probe/rapor.md`) + Ek B'nin Aşama-4 satırı ölçümle güncellendi.
**Geri kenarı:** BAŞARISIZ → 0A kilitli kalır; max 2 deneme.
