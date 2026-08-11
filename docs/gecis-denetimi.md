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
