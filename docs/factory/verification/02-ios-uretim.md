# 0A / Adım 2 — iOS ayağı yerel kanıtı (C+ mimarisinin ilk kapısı)

**Tarih (UTC):** 2026-08-15 · **Yapan:** executor (otonom) · **Makine:** Windows 10 Pro
**Pin:** Unity 6000.3.16f1 (changeset `a56f230f6470`)
**Sonuç:** **GEÇTİ** — Xcode projesi Windows makinesinde üretildi. DUR koşulu
("Windows'tan çıkmıyor") gerçekleşmedi; UBA'ya düşülmedi.

Bu adım, C+ kararının ikinci dayanağını (mimar beyanı: "Xcode projesi Windows'tan
üretilebiliyor") **yerinde doğrular**. `verification/06-lisans.md`'deki "mimar beyanı"
etiketi bu belgeyle ölçüme dönüşmüştür.

## (a) iOS Build Support modülü — kurulu (önceden)

İdempotent kontrol önce koşuldu; modül **zaten kuruluydu**, dolayısıyla Hub
`install-modules` çağrılmadı ve **makinede değişiklik yapılmadı**.

Kanıt — `<Unity>\Editor\Data\PlaybackEngines` dizin ölçümü:

| modül | boyut |
|---|---|
| `AndroidPlayer` | 9 859 MB |
| **`iOSSupport`** | **1 353 MB** |
| `windowsstandalonesupport` | 968 MB |

`iOSSupport` içeriği (iskelet değil, tam kurulum): `arm64`, `x64`, `il2cpp`,
`Trampoline`, `Variations`, `Tools`, `Data`, `iOSPlayerBuildProgram.exe`, `modules.asset`.

**Not (kurulum tablosuna geri besleme):** iOS modülü `stages/kurulum.md` satır 7'de
yalnız `--module android` olarak yazılıydı; bu makinede iOS modülü zaten mevcut çıktı.
Yani kurulum tablosu ile makinenin gerçek durumu arasında (lehte) bir fark var —
başka bir makinede 0A koşulursa bu adım **kurulum gerektirecektir** ve o zaman Hub
`--headless install-modules --version 6000.3.16f1 --module ios` çalıştırılmalıdır.

## (b) Xcode projesi üretimi — GATE

Geçici **boş** proje fabrika dizini altında oluşturuldu (`_probe-ios/`, gitignore
`_probe-*/`). Sahne preset'ten kopyalanmadı, **kodla üretildi** — kanıt saf iOS ayağına
ait olsun, başka bir bileşenin yan etkisi olmasın diye (`EditorSceneManager.NewScene`
→ `SaveScene`).

**Komutlar (birebir):**
```
Unity.exe -batchmode -quit -createProject <fabrika>\_probe-ios -logFile -
Unity.exe -batchmode -quit -projectPath <fabrika>\_probe-ios \
          -executeMethod FactoryProbe.Ios.IosProbe.BuildXcodeProject -logFile -
```

**Ham çıktı:**
```
[IosProbe] sonuc=Succeeded sure=00:00:40.0466023 hata=0 uyari=0 cikti=.../_probe-ios/Build/ios
[IosProbe] xcodeproj sayisi=1 yollar=Unity-iPhone.xcodeproj
[IosProbe] KANIT TAMAM: Xcode projesi Windows uzerinde uretildi
Exiting without the bug reporter. Application will terminate with return code 0
```

**Çıkarım:** `BuildPipeline.BuildPlayer(target: iOS)` Windows'ta `Succeeded` döndü,
**0 hata / 0 uyarı**, süreç çıkış kodu **0**, ve script yalnız "Succeeded" beyanına
güvenmeyip dosya sisteminde `*.xcodeproj` **aradı** — bulundu. (Script, "Succeeded
denip xcodeproj üretilmemesi" hâlinde bilerek exception atacak şekilde yazıldı;
beyan ile artefakt ayrı doğrulandı.)

## Üretilen Xcode proje ağacı (artefakt kanıtı)

Kök: `Build/ios` — **2 670 dosya, 465.9 MB**

| bileşen | ne |
|---|---|
| `Unity-iPhone.xcodeproj/` | **Xcode proje dosyası** — içinde `project.pbxproj` + `xcshareddata` |
| `Il2CppOutputProject/` | IL2CPP'nin ürettiği C++ kaynak ağacı (iOS zorunlu IL2CPP) |
| `Classes/`, `Libraries/`, `Frameworks/`, `Data/` | trampoline + oyun verisi |
| `UnityFramework/`, `MainApp/`, `Unity-iPhone Tests/` | Xcode hedefleri |
| `Info.plist`, `LaunchScreen-*.storyboard` | uygulama meta/açılış |
| `process_symbols.sh`, `validate-tbd.sh` | Xcode derleme yardımcıları |

Yani Windows tarafı, macOS'ta `xcodebuild`'in ihtiyaç duyduğu **tam proje ağacını**
üretiyor. Derleme (`xcodebuild`) bu adımın konusu değildir — adım 4'te macOS runner'da
koşacaktır.

## C+ mimarisi için anlamı

- iOS ayağı, runner'da Unity çalıştırmadan kurulabilir: **Windows'ta xcodeproj üret →
  zip → geçici Release asset → macOS runner'da `xcodebuild` derleme kanıtı**.
- Unity hesap secret'ı gerekmez; lisans yalnız yerel makinede, Hub oturumuyla yaşar.
- İmza zinciri ve ASC anahtarı bu adımın kapsamı **dışındadır** (0B).

**Uygulama kimliği:** `com.factorygames.iosprobe` — kodda verildi
(`PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.iOS, …)`), sondadaki
Android bulgusunun (şablon `productName`'i geçersiz kimlik üretiyor) iOS karşılığı
önlenmiş oldu.

## Temizlik

Geçici proje ve 465.9 MB'lık çıktı ağacı **silindi** (aşağıdaki komut koşuldu):
```
Remove-Item <fabrika>\_probe-ios -Recurse -Force
```
Repoya hiçbir ham artefakt girmedi (kural 25); bu belge metin kanıttır.
