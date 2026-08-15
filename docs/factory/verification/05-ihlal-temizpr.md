# 0A / Adım 5 — Kasıtlı ihlal + temiz-PR

**Tarih (UTC):** 2026-08-15 · **Yapan:** executor (otonom) · **Sonuç:** **GEÇTİ**
**Depo:** `factorygames-hello` (public) · **Koşu sayısı:** 5 ihlal + 1 temiz = 6

Amaç: kapıların gerçekten kırmızı verdiğini **CI'da** kanıtlamak (beş ihlal) ve ardından
temiz bir değişiklikle **yanlış-pozitif üretmediğini** göstermek. Sürekli kırmızı yanan
kapı ilk haftada bypass edilir; sürekli yeşil yanan kapı zaten kapı değildir.

Her ihlal **kendi dalında ve kendi PR'ında** koşuldu. iOS işi `workflow_dispatch`'e bağlı
olduğu için hiçbir ihlal turunda **koşmadı** — ihlaller lint katmanındadır ve macOS
çarpanı (10×) gereksiz yere harcanmadı (adım 4'ün tüketim ölçümü bu kararı destekliyor).

## İhlal → kapı eşleşme tablosu

| # | ihlal | beklenen kapı | **yakalayan kapı(lar)** | eşleşme | CI run (lint) | PR |
|---|---|---|---|---|---|---|
| a | Sahneye 38 nesne eklendi (toplam 40, baseline 2) | SAHNE-BASELINE | `SAHNE-BASELINE` | **TAM** | `31889816334` | #1 |
| b | Koda gömülü sahte `api_key` | SECRET-SCAN | `SECRET-SCAN` | **TAM** | `31889817377` | #2 |
| c | 2 MB ham `.png` (gitignore `-f` ile zorlandı) | HAM-ARTEFAKT | `HAM-ARTEFAKT` | **TAM** | `31889818757` | #3 |
| d | `EditorBuildSettings`'e ikinci sahne | TEK-KAYNAK | `TEK-KAYNAK` + **`PRESET-SAPMA`** | **TAM + EK** | `31889819840` | #4 |
| e | Preset dosyası elle değiştirildi (`QualitySettings` `antiAliasing 0→4`) | PRESET-SAPMA | `PRESET-SAPMA` | **TAM** | `31889820975` | #5 |

Beş koşunun tamamında `test` işi **yeşil** kaldı — ihlaller lint düzlemindedir ve saf C#
çekirdeğine dokunmaz; yani kırmızı, doğru katmandan geldi.

### (d)'nin ikinci kapısı — beklenen ve değerli bulgu

`ProjectSettings/EditorBuildSettings.asset` **iki şapkalıdır**: hem build listesinin
kaynağı (TEK-KAYNAK'ın baktığı yer) hem de preset setinin bir üyesi (PRESET-SAPMA'nın
hash'lediği dosya). Dolayısıyla build listesine ikinci sahne eklemek zorunlu olarak
preset sapması da üretir. Bu bir **çift savunma**dır, çelişki değil: kural
("tek sahne") ve kaynak ("preset kopyası") ayrı gerekçelerle aynı dosyayı korur.

Pratik sonuç: bir oyun projesi meşru biçimde ikinci sahne eklemek isterse **iki kapı
birden** kırmızı verir ve değişiklik preset setinin güncellenmesini gerektirir — yani
"sahne ekleme" sessizce yapılamaz, şablon düzeyinde bir karar hâline gelir. Tasarımın
istediği budur; kayda geçirildi.

## Temiz-PR (yanlış-pozitif testi)

| iş | sonuç | süre | run |
|---|---|---|---|
| `lint` | **success** | 10 sn | `31889922419` |
| `test` | **success** | 31 sn | `31889922407` |

PR **#6** — `TEMIZ PR: README (0A adim 5 — yanlis-pozitif testi)`. İçerik: depoya
`README.md` eklendi (zincirin ne kanıtladığını ve yerel koşum komutlarını anlatır).
Beş kırmızının ardından altıncı koşunun yeşil gelmesi, kapıların **ayrım yaptığını**
gösterir.

`ios` işi bu turda hiç koşmadı (dispatch'e bağlı) — beklenen davranış.

## Temizlik (doğrulandı)

- Beş ihlal PR'ı **kapatıldı, birleştirilmedi**; beş dal silindi.
- Temiz PR **squash ile birleştirildi**, dalı silindi.
- Uzak dal listesi: **yalnız `main`** (`gh api repos/.../branches` çıktısı).
- PR durumları: #1–#5 `CLOSED`, #6 `MERGED`.
- Birleşme sonrası `main` üzerinde lint yeniden koşuldu: **kırmızı 0**.

Hiçbir ihlal `main`'e karışmadı; 2 MB'lık sahte artefakt yalnız kapatılan dalın
geçmişinde kaldı ve o dal silindi.

## Kanıt zinciri notu

Adım 4'te **canlı** bir PRESET-SAPMA kırmızısı da yaşanmıştı (`31885004631`, 12:35) ve
düzeltilince yeşile dönmüştü (`31885312281`, 12:43). O, kasıtlı değil gerçek bir
kusurdu; bu adımın kasıtlı beşlisinden ayrı tutulur — ama kapının sahada da iş gördüğünü
gösteren bağımsız bir tanıktır.
