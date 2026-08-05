# AŞAMA -1 — SONDA (tek seferlik; 0A'dan ÖNCE)

**Amaç:** Claude Code'un Sözleşme-2 kurallarıyla (bootstrap-only, JSON veri, MCP
yalnız gözlem) gri kutu döngü üretip üretemediğini ÖLÇMEK. Ölçmeden 0A'ya girilmez.

## Önkoşullar (raporda her biri tik işaretlenir)

1. Unity Hub kurulu, Personal lisans oturumu açık.
2. Unity 6000.3 LTS kurulu; Hub'da **Android Build Support** modülü seçili.
   (iOS modülü Windows'ta yok — sorun değil; iOS derlemesi CI'ın işi.)
3. Git ve gh CLI kurulu, oturum açık.
4. VS Code + Claude Code çalışan oturumda.
5. Resmî Unity MCP köprüsü **KURULU ve ZORUNLU** — Sözleşme-2 sınırlarında
   yapılandırılmış (sahne-düzenleme araçları kapalı). Kurulamıyorsa sonda
   KOŞULMAZ: bu durum Deneme-1 bulgusu olarak rapora "MCP kurulamadı" diye
   geçer. FALLBACK yolu üretim koşuları içindir, ölçüm koşusu için değil —
   MCP'siz koşulan sonda, kurmak istediğimiz hattı test etmez ve dokunma
   metriğini karşılaştırılamaz kılar.
6. Görev dosyası `docs/probe/BRIEF.md`. Başka ipucu/yol haritası kullanılmaz —
   Deneme-1 soğuk koşudur.

## Görev (özet; tam tanım BRIEF.md'de)

Tek ekran, tek input (tap/hold), skor + fail + restart içeren 60–90 saniyelik
döngü; bootstrap-only sahne; veri JSON; bot ile 3 otomatik döngü; Windows
play-mode'da hatasız.

## Ölçümün kaydı

Her durak `docs/probe/rapor.md`'ye satır olarak düşer: `{ts, olay, not}`.
Raporun kapandığında içermesi gereken toplam alanlar:
- **T_kurulum** — proje oluşturma, paketler, MCP ayarı, ilk derleme; boş sahne
  + test altyapısı koşar hale gelene kadar. Tek seferliktir, her oyunda tekrar
  etmez. Karar tablosuna GİRMEZ; 0A takvim tahminini besler.
- **T_uretim** — BRIEF'in verildiği andan tüm testler yeşil olana kadar.
  Karar tablosu YALNIZ buna bakar; Ek B'nin Aşama-4 satırı da buradan yazılır.
- **insan müdahalesi sayısı** — tanım: üretim akışının ilerleyebilmesi için
  insandan yazı/onay/elle işlem gereken her durak = 1 (kurulum adımları hariç),
- **Editor'e elle dokunma sayısı** — tanım: insanın Editor UI'ında yaptığı her
  işlem; hedef 0.
- **engel listesi** — her durak 1 satır: sebep + çözüm,
- **test özeti** — EditMode/PlayMode/bot çıktıları, log dosya yollarıyla.

## Sayısal karar tablosu (ilk sonda bu eşikleri de kalibre eder)

- **BAŞARILI:** döngü + testler yeşil VE T_uretim ≤ 6 sa VE müdahale ≤ 10
  VE elle dokunma = 0.
- **SARI:** çalışıyor ama T_uretim 6–12 sa veya 11–20 müdahale veya 1–3 elle
  dokunma → 0A'ya geçilebilir; Ek B'nin Aşama-4 beklentisi gerçekleşenle
  yazılır, P1 sürtünmesi Sözleşme-5 kaydı açılır.
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

**Yürüten:** karma — üretim otonom; insan gözlemci, sayımları tutar.
**Geçiş kriteri:** tabloya göre BAŞARILI veya SARI + rapor dosyalandı + Ek B'nin
Aşama-4 satırı ölçümle güncellendi.
**Geri kenarı:** BAŞARISIZ → 0A kilitli kalır; max 2 deneme.
