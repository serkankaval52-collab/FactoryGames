# FALLBACK — MCP koptuğunda CLI eşdeğerleri

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Dayanak:** PIPELINE Sözleşme-6 — *zorunlu adım MCP'ye bağımlı olamaz.* Bu dosya,
MCP köprüsü koptuğunda/kapalıyken hattın durmaması için her gözlem yüzeyinin komut
satırı karşılığını verir. Metin kopyalanmaz: kural metinleri kendi dosyalarında yaşar,
burada yalnız **eşdeğer komut** ve **kanıt biçimi** vardır.

## İlke

MCP bu hatta **yalnız gözlemcidir** (kök `CLAUDE.md` kural 10 ve 30; sahne/ayar
düzenleme yasağı orada tanımlıdır). Dolayısıyla her MCP yüzeyinin bir CLI karşılığı
zorunludur ve karşılığı olmayan yüzey **zorunlu adımda kullanılamaz**.

## Eşdeğer tablosu

| gözlem | MCP yüzeyi | CLI eşdeğeri | kanıt biçimi |
|---|---|---|---|
| Konsol/hata okuma | `Unity_GetConsoleLogs` | `Unity.exe -batchmode -projectPath <p> -logFile -` çıktısını dosyaya yönlendirip `error CS`/`Exception` taraması | log satırı + çıkış kodu |
| Test koşumu | (MCP yüzeyi yok) | `Unity.exe -batchmode -projectPath <p> -runTests -testPlatform EditMode|PlayMode -testResults <xml>` | NUnit XML `total/passed/failed` |
| Derleme/build | (MCP yüzeyi yok) | `Unity.exe -batchmode -quit -projectPath <p> -executeMethod <Sınıf.Metot>` | `BuildReport` özeti + artefaktın dosya sisteminde **aranması** |
| Sahne/kamera görüntüsü | `Unity_SceneView_Capture*`, `Unity_Camera_Capture` | **Eşdeğeri yoktur** — batchmode ekran üretmez (premium-sozlesme "Ölçüm yeri", A2.2) | render kanıtı yalnız cihaz koşusundan; batchmode'da **VERİ-YOK** |
| Editor oturumu durumu | köprü el sıkışması | `Temp/UnityLockfile` varlığı + **kalıntı ayrımı** (aşağıda) | süreç listesi + dosya kilidi denemesi |
| Keyfi kod çalıştırma | `Unity_RunCommand` | **Kullanılmaz** — bu araç kapalıdır (kurulum satır 8 kanıtı) | — |

## Lockfile kalıntı ayrımı (zorunlu alt yordam)

Batchmode **hata ile** çıktığında `Temp/UnityLockfile` geride kalabilir (sonda §7.5
saha bulgusu). "Dosya var → Editor açık" varsayımı yanlış pozitif üretir ve sonraki tüm
koşuları bloke eder. Ayrım şudur:

```powershell
$u = Get-Process -Name Unity -ErrorAction Ignore          # 1) süreç var mı?
try { $fs=[IO.File]::Open($lf,'Open','ReadWrite','None'); $fs.Close(); $kalinti=$true }
catch { $kalinti=$false }                                  # 2) exclusive açılıyor mu?
```

**Süreç YOK + exclusive açılabiliyor ⇒ kalıntıdır**, silinebilir. Aksi hâlde canlı
kilittir; batchmode koşulmaz.

## Ortam tuzakları (saha kaydı)

| tuzak | belirti | önlem |
|---|---|---|
| `ELECTRON_RUN_AS_NODE` sızıntısı | Hub headless `Cannot find module '--headless'` | çağrı öncesi süreç düzeyinde `Remove-Item Env:ELECTRON_RUN_AS_NODE` (kurulum satır 5) |
| Kültür ayıracı | ölçüm alanlarında `76,00` | sayı/tarih ayrıştıran her yerde `InvariantCulture` |
| Yol ayıracı | zip'te ters bölü → macOS `unzip` çözemez | arşiv Python `zipfile` ile, yollar `/` |
| BOM | `json.load` kırılır | okuyucular `utf-8-sig`, yazıcılar BOM'suz |

## Kapsam dışı

Cihaz koşusu (Firebase Test Lab) yüzeyleri bu dosyanın konusu değildir; ölçüm yeri
ayrımı `docs/standards/premium-sozlesme.md`'dedir ve oradan değişir.
