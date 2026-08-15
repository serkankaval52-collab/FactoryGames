# GEÇİŞ DENETİMİ — aşama çıktısı bir sonrakinin girdisi olarak YETERLİ mi

Tekrar koşulan denetimin KAYDI: her turda yeni tarih + sürüm satırlı tablo eklenir (eskisi silinmez),
fark diff'ten okunur (köprü kararı — bu tablo etiket mesajında DEĞİL, ağaç dosyasında yaşar).
Test soruları (Alan 4): (a) "bir sonraki aşama bu çıktıyı alıp durmadan çalışabilir mi" — VAR MI
değil, YETERLİ Mİ; (b) A1.2: her kapının kullandığı araç kurulum tablosunda mı — canlı sürümü
`tools/arac_suzgec.py`'dir (CI `arac-testleri` işi; A4.1 ile CLAUDE.md kural 30'dan teste çevrildi).

## v1.0.18 — 2026-08-11 (ilk tam tarama; 14 geçiş)

| Geçiş | Yeterli mi | Kanıt |
|---|---|---|
| kurulum → sonda | EVET | sonda Önkoşul 0 "KAPALI" + satır birebirliği; gcloud sondada gerekmiyor |
| sonda → 0A | EVET | `scene-baseline.json`, `presets/unity-<pin>`, `unity-pin.txt`, Ek B A4 satırı, T_build — adıyla 0A/0B girdisi |
| 0A → 0B | EVET | 0B önkoşul satırı; halka v0 (0A-7); sosyal hesaplar (0A-8); lisans canary cron'lu |
| 0B → 1 | EVET | fikir standardı/defter/hesap envanteri 0A-6 ürünü; yasak liste + kura ön-adımlar üretir |
| 1 → 2 | EVET | kart (kura kaydı + K1–K3 + bant + rakip tablosu) + veto + hasat kaydı |
| 2 → 3 | EVET | "araç/SDK gereksinim listesi (Aşama 3 girdisi)" 2.md'de açık adlı |
| 3 → 4 | EVET | yeşil build borusu + sürüm kilidi + MAX/GA init = 4.md girdisi |
| 4 → 5 | EVET | 4 çıktısı Android APK "Aşama 5'in halka paketi" diye açık köprü |
| 5 → 6 | HAYIR → DÜZELTİLDİ | A5 çıktısı A6'yı yönlendiren yapı taşımıyordu (köprü şüphesi doğrulandı) — 5.md'ye halka bulgu listesi (P0/P1/P2; boşsa "bulgu yok" gerekçeli), 6.md girdi + geçiş kriterine bağlandı |
| 6 → 7 | EVET | "içerik-tam build" birebir |
| 7 → 8 | EVET | screenshot paketi + TestFlight paketi 7 çıktısında; R2b/R4 insan bloğu 8'de tanımlı |
| 8 → 9 | EVET | yazılı "yayınla" onayı + P0 zorunlu; ret-düzeltme kaydı |
| 9 → 10 | EVET | yayında oyun + `sosyal_yayin` olayları |

Köprü şüphelerinin ek doğrulaması: A2 GDD → A4 executor YETERLİ (DoD + bot + soak kriterleri plan
alanlarına bağlı); A8 rubrik çıktısı SOMUT (eksen→aşama haritası + P0/P1/P2 + P0 zorunluluğu).

## A1.2 süzgeci (v1.0.18 anlık görüntü — canlısı `tools/arac_suzgec.py`)

Kapıların kullandığı tüm araçlar kurulum tablosunda: python → satır 4; Unity Hub/Editor → 5–7;
MCP → 8; git/gh → 2–3; winget → 1; FFmpeg → 10; gcloud → 11. robocopy/PowerShell Windows yerleşik;
xcodebuild macOS runner yerleşik; repo-içi scriptler (kura/marker/report) python üzerinden koşar.
Eksik YOK — bir sonraki taramada bu bölüm `arac_suzgec.py` çıktısıyla güncellenir.

## v1.3 — 2026-08-12 (kör-nokta turu; GG1–GG10 ilk tam geçiş)

Üçlü düzenin dağılışı (kullanıcı kararı) sonrası kalıcı saldırı sistemi kuruldu:
`docs/kor-nokta-analizi.md` (KN1–KN10, kanıt etiketli) + `docs/standards/gozden-gecirme.md`
(GG1–GG10). İlk tam tur bulguları:

| Mercek | Bulgu | Aksiyon |
|---|---|---|
| GG1 | Uyumlu: Ek C etiketleri tam; açık borç tek kalem (ses_* — kayıtlı) | izleme sürer |
| GG2 | SANAT TETİKLEYİCİ EKSİK: paket kapısı 2.md'de ama sürecin ne zaman AÇILDIĞI yazılı değildi | v1.3.1: sanat-yonu'na tetikleyici cümlesi |
| GG3–GG4 | Uyumlu: G8 (parametreli manifest + örneklem) ve 6.md yetki kapanışı v1.2'de işlendi | — |
| GG5 | Uyumlu: V3 sağlaması 0A'ya girdi (kullanıcı onayı koşuluyla) | — |
| GG6 | Uyumlu: sanat yönü satırı insan-yuku §1'de (v1.2) | — |
| GG7 | Erteleme taraması temiz: bekleyen her kalem şerhli (Ek B/C sonda kalibrasyonu; ÖLÇEK borçları) | — |
| GG8 | Sanat kapısı üç-durum kapsamı dışı: paket önkoşuldur, ölçüm kapısı değil (gerekçe: paket yoksa üretim başlamaz) | kayıt |
| GG9 | Uyumlu: canlı süpürmeler yeşil (arac_suzgec 33 dosya; esik kapsama 55/55) | — |
| GG10 | Bu turun kendisi; yürütücü değişikliği PIPELINE/kurulum/sonda/BRIEF'e işlendi | — |

1 → 2 geçişi güncellendi (v1.2 sonrası): Aşama 2 kapısı artık ailenin ONAYLI sanat yönü
paketini ister (koşullu insan kapısı; sanat-yonu.md) — tablodaki "1 → 2 EVET" satırı
buna göre okunur (paket yoksa kapı kırmızı; bu bir eksik değil, tasarımdır).

## SONDA → 0A GEÇİŞ NOTU (v1.3.8, 2026-08-15)

**Sonda Deneme-1 (soğuk) BAŞARILI kapandı** — karar report.py ürünü; Deneme-2 gerekmedi.
Ölçümler: T_uretim 1247,8 sn (0,35 sa; eşik ≤6 sa) · insan kapısı 0 · EditMode 10/10 ·
PlayMode bot 3/3 döngü (tur 76,98–77,00 sn; brief bandı 60–90 sn) · P1 temiz (2=2) ·
T_build 382,3 sn (0A CI takvim girdisi). Kanıt: `raporlar/2026-08-15-sonda.md`;
artefaktlar: `presets/unity-6000.3.16f1/` (Revizyon 1), `unity-pin.txt`,
`scene-baseline.json`, `kaynak/`. Ek B Aşama-4 satırı ölçümle yazıldı; sonda KAPALI.

**Sonda sonrası uygulanan düzeltmeler:** v1.3.7 — unity-pin.txt repoya geri (mimarın
v1.3.4 hatasının düzeltmesi) + ham `rapor.md` yerel (lockfile yolu kimlik izli).
v1.3.8 — report.py çapraz-kontrol sayacı diriltildi (sonda §7.1: content her zaman
liste; text-blok sayımı + uretim-start penceresi; beklenen ≈ 1 başlangıç + kapı kadar;
test 14–16 önce-kırmızı kanıtlı); sonda.md — kaynak beyaz listesine `*.asmdef *.asmref`
(§7.4); lockfile kalıntı ayrımı (§7.5: süreç YOK + exclusive-açılabilir ⇒ kalıntı).

**0A'ya devredilenler:** P1 per-dosya kapsam (§7.6 — mevcut davranış fail-safe:
yanlış kırmızı üretebilir, yanlış yeşil üretemez; per-dosya baseline 0A'da tasarlanır);
Input System sürüm pini (§7.2 borcu — kayıt defteri sorgusu ister; legacy kararı sonda
kapsamlıdır); şablon applicationIdentifier kuralı (§7.3 — rakamla başlayan productName
geçersiz; kimlik build script'inde `com.factorygames.<slug>`); InvariantCulture
ayrıştırma kuralı (§7.5 — süre alanı okuyan her yeni araçta).

**0B'ye devredilen:** Sözleşme-2 MCP gözlemci dayanağı sınanamadı (koşullu tetik hiç
oluşmadı — geçerli bulgu; 0B'de bilinçli sınanacak).

**Şerh kabulü:** §7.7 hazırlık okumaları damga öncesinde (asimetri bilinerek kabul);
§7.8 BRIEF'in ilk 30 satırı kurulum turunda görülmüştü (soğukluk şerhi kayıtlı; 0B'de
brief yeni ve görülmemiş olacak).
