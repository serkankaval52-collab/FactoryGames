# 0A / Adım 4 — Hello-build (şablon zincirinin uçtan uca kanıtı)

**Tarih (UTC):** 2026-08-15 · **Yapan:** executor (otonom) · **Sonuç:** **GEÇTİ**
**Depolar:** `factorygames-hello` (public, yeni) · `factory.core` v0.1.5 → **v0.1.8**

C+ makine ilkesi uygulandı: **hiçbir CI runner'ında Unity koşmadı.** Unity gerektiren
her kanıt yerelde üretildi ve metin olarak buraya girdi; CI yalnız lint + saf-C# test +
iOS `xcodebuild` koştu.

## Brief

Adım 4'ün ayrı bir brief dosyası yoktur; görev tanımı `docs/stages/0A.md` satır 42–52'dir
ve bu koşuda o metin brief olarak alınmıştır. (Sonda bulgusu §7.8 kapsamında not: bu
metin daha önce görülmemiştir — 0A.md v1.4.0 ile yeniden yazılmıştı.)

## Süreler (ham damga satırları)

```
uretim-start.ts = 1786795237801
uretim-end.ts   = 1786803029722
build-start.ts  = 1786796534801
build-end.ts    = 1786797012986
```

| metrik | ham hesap | insan-okur |
|---|---|---|
| **T_uretim** | `(1786803029722 − 1786795237801)/1000` | **7791.921 sn = 2.16 sa** |
| **T_build** | `(1786797012986 − 1786796534801)/1000` | **478.185 sn = 0.13 sa** |

**Çıkarım:** T_build, T_uretim'in *içinde* ölçüldü (adım 4'te build üretimin parçasıdır,
sondadaki gibi ardışık değil) — çift sayım yapılmamalıdır. Damgalar sondanın damgalarını
ezmesin diye ayrı köke (`--probe-root docs/factory`) yazıldı; `.markers/` yereldir.

## Zincir — ölçülen adımlar

| # | adım | kanıt | sonuç |
|---|---|---|---|
| 1 | Repo açma + scaffold | `gh repo create` → kardeş dizine klon → repo-içi kimlik ilk iş | ✅ |
| 2 | Şablon kopyası | `templates~/` → hello (55 dosya) | ✅ |
| 3 | UPM çözümleme | `com.factorygames.core@…git#v0.1.8` PackageCache'e indi | ✅ |
| 4 | Derleme | exit 0, `error CS` yok, `FactoryGames.Core.dll` + `Game.Runtime.dll` doğdu | ✅ |
| 5 | EditMode | `total=5 passed=5 failed=0` | ✅ |
| 6 | PlayMode | `total=2 passed=2 failed=0` | ✅ |
| 7 | Saf C# (yerel) | `dotnet test` → 8/8 | ✅ |
| 8 | Android (yerel batchmode) | `Succeeded`, 3 dk 38 sn, **APK 30 035 584 bayt (28.6 MB)**, hata 0 | ✅ |
| 9 | iOS xcodeproj (yerel) | `Succeeded`, 2 dk 47 sn, `Unity-iPhone.xcodeproj` | ✅ |
| 10 | CI `lint` | success, 7 sn | ✅ |
| 11 | CI `test` | success, 35 sn | ✅ |
| 12 | CI `ios` (macOS) | success, 6 dk 48 sn, `** BUILD SUCCEEDED **` | ✅ |

**CI koşu bağlantıları** (public repo, `serkankaval52-collab/factorygames-hello`):
`actions/runs/31885312281` (lint) · `actions/runs/31885312357` (test) ·
`actions/runs/31888775887` (ios).

## iOS düzeneği — kural 25 temiz

Windows'ta `xcodeproj` üretildi → **Python `zipfile`** ile paketlendi (2996 dosya,
225.4 MB) → **geçici** Release asset (`ios-probe-tmp`) → macOS runner indirip
`xcodebuild … CODE_SIGNING_ALLOWED=NO` koştu → `** BUILD SUCCEEDED **` →
**release ve etiketi silindi** (`--cleanup-tag`; doğrulandı: release listesi boş,
uzak etiket yok). Zip git tarihine **hiç girmedi**. İmza zinciri + ASC anahtarı 0B'de.

## Actions tüketimi (adım 1'in bekleyen maddesi — KAPANDI)

8 gerçek koşudan ölçüldü; ayrıntı ve ham tablo `01-02-hesaplar.md`'dedir.
Özet: **9.1 dk gerçek / 73.2 dk çarpanlı**, public repoda tahsilat yok. Kritik sayı:
**macOS çarpanı 10×** — tek `ios` koşusu 6.8 dk gerçek sürede 68 dk çarpanlı tüketim.
Bu, iOS işinin her push'ta değil yalnız `workflow_dispatch` ile koşturulması kararını
sayısal olarak destekler.

---

## Zincirin yakaladığı beş kusur

Hepsi **yalnızca uçtan uca koşuda** görülebilirdi; şablon tek başına test edilirken
hiçbiri ortaya çıkmıyordu. Hello-build'in varlık sebebi budur.

### 1. UPM paketinde `.meta` dosyaları yoktu → paket sessizce yok sayılıyordu

```
error CS0246: The type or namespace name 'FactoryGames' could not be found
Asset Packages/com.factorygames.core/package.json has no meta file,
  but it's in an immutable folder. The asset will be ignored.
```

Paket **indi** (PackageCache'te doğrulandı) ama `.meta` olmadığı için Unity
`Runtime/FactoryGames.Core.asmdef`'i içe aktarmadı; assembly hiç doğmadı. Unity'nin tek
işareti sessiz bir uyarıydı ve CS0246 ile bağı açık değildi. **Düzeltme:** `.meta`
dosyaları elle yazılmadı — geçici bir Unity projesinde paket yerel klasör olarak açıldı,
Unity 9 `.meta` üretti, pakete taşındı (v0.1.5).

### 2. `*.csproj` deseni test projesini yutuyordu → CI kesin kırmızı olurdu

Şablonun `.gitignore`'undaki düz `*.csproj`, `tests/Core.Tests/Core.Tests.csproj`
dosyasını da kapsıyordu; dosya depoya hiç girmezdi ve CI'daki
`dotnet test tests/Core.Tests/Core.Tests.csproj` onu bulamazdı. **Düzeltme:** desen
`/*.csproj` ile köke sınırlandı, `!tests/**/*.csproj` ile test projesi açıkça korundu
(v0.1.6).

### 3. `.utmp/` ignore edilmiyordu → PII sızıntısı riski

Android build geçici ağacı (`metadata_generation_command.txt`, `CMakeCache.txt`,
`.ninja_log`) **makine yolu** içeriyor ve staged olmuştu. **Düzeltme:** `.utmp/`
ignore'a alındı; staged dosya sayısı **128 → 86**. Ayrıca maske tarama yöntemi
düzeltildi: artık yalnız **staged** dosyalar taranıyor (gitignore-farkında), önceden tüm
çalışma ağacı taranıp yanlış alarm üretiliyordu.

### 4. `DIL-KAPISI` 18 yanlış pozitif üretti

Kapı `Assets/Editor/` ve `Assets/Tests/` altındaki dosyaları da kırmızı yakıyordu; ikisi
de oyuncuya **ulaşmaz** (Editor build'e girmez, testler `UNITY_INCLUDE_TESTS` kısıtıyla
derlenmez). `throw` mesajları ve attribute metinleri de geliştirici yüzeyidir.
**Düzeltme:** kapı yalnız çalışma zamanı kodunu arıyor (v0.1.4). Hello tarafında gerçek
tek ihlal (`"DOKUNUS: "` etiketi) giderildi — artık yalnız sayı gösteriliyor.

### 5. `PRESET-SAPMA` CI'da kırmızı — iki aşamalı teşhis, **ilki yanlıştı**

CI 7 dosyada sapma bildirdi; yerelde yeşildi. **İlk teşhisim CRLF/LF farkıydı ve
YANLIŞTI** (v0.1.7'de normalize hash + `.gitattributes` eklendi, sapma **sürdü**).
Gerçek neden diff ile ölçüldü:

```
ProjectSettings.asset      : +androidDisplayOptions +audioSpatialExperience
                             +metalUseMetalDisplayLink, -vulkan* alanlari
DefaultVolumeProfile.asset : +filter +m_Value +m_OverrideState
GraphicsSettings.asset     : +m_ShaderBuildSettings +keywordDeclarationOverrides
```

Unity 6000.3.16f1, **6000.1 hedefli** şablonun asset şemalarını açılışta güncelliyor.
Ham şablondan üretilen preset ile **her oyun projesi ilk açılışta sapardı** → kapı
sürekli kırmızı yanar → 0A adım 5'in kendi uyarısı gerçekleşir ("sürekli kırmızı yanan
kapı ilk haftada bypass edilir"). **Düzeltme:** preset artık **kanonik hâl** — şablon
temiz geçici projeye kopyalanıp pinli Unity ile bir kez açılıyor, çıkan hâl presete geri
yazılıyor (v0.1.8). Yöntem hâlâ mekanik ve tek kaynaklı. `packages-lock.json` presete
alındı; `ProjectVersion.txt` presetten çıkarıldı (oyun pini oyunundur).

v0.1.7'nin normalize hash + `.gitattributes` eklentileri **kalıyor** (ileriye dönük
önlem) ama gerekçeleri düzeltildi — o değişiklik sorunu çözmemişti.

### Ek: iOS zip'inde yol ayıracı (sondanın "yol ayıracı" sınıfının tekrarı)

İlk `ios` koşusu düştü:
`warning: xcodeproj.zip appears to use backslashes as path separators`.
PowerShell `Compress-Archive` Windows ters bölüsüyle yazıyor; macOS `unzip` dizin
yapısını çözemedi ve `*.xcodeproj` bulunamadı. **Düzeltme:** zip Python `zipfile` ile
üretildi, yollar `/` ile normalize edildi (doğrulandı: 2996 giriş, ters bölü **0**).

## factory.core sürüm zinciri (bu adımda)

| sürüm | ne |
|---|---|
| v0.1.5 | UPM `.meta` dosyaları |
| v0.1.6 | `.gitignore`: `/*.csproj` + `!tests/**`, `.utmp/` |
| v0.1.7 | normalize preset hash + `.gitattributes` (gerekçesi sonradan düzeltildi) |
| v0.1.8 | **kanonik preset** + `packages-lock.json`; `ProjectVersion.txt` çıkarıldı |

(v0.1.4 bu adımın başında DIL-KAPISI kapsamı ve eşik testi senkronu için yayınlandı.)

## Kural uyumu

Kural 30: bu koşuda hiçbir üçüncü taraf MCP köprüsüne bağlanılmadı; makinedeki ikinci AI
uzantısına iş yaptırılmadı. Kural 25: depoya sır, ham görüntü/log dökümü girmedi; geçici
iOS asset'i iş biter bitmez silindi. Maske: commit'lenen tüm metinlerde **0 eşleşme**
(yalnız staged dosyalar taranarak).
