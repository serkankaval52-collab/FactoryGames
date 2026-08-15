# 0A / Adım 2a — Unity CI lisanslama: resmî doküman özeti

**Özet tarihi:** 2026-08-15 · **Okuyan:** executor · **Pin:** Unity 6000.3.16f1

**Sonuç — KARAR: C+ (kullanıcı onaylı, 2026-08-15).** Bulgu değişmedi: Personal plan
CI'da (GUI'siz) resmî olarak lisanslanamıyor. Bu bulgu üzerine H4 kapısı **DUR ile
değil, mimari kararla** kapandı: **hiçbir CI runner'ında Unity koşmaz.** Unity işleri
yerelde koşar, kanıtı metin olarak repoya girer (0A.md "Makine ilkesi", v1.4.0).

Kararın iki dayanağı:
1. **Bu belgede ölçülen:** Personal'ın ekransız (headless) aktivasyon yolu kapalı —
   üç resmî sayfanın birbirini doğrulayan ifadeleri (aşağıda alıntılı).
2. **Mimarın eklediği kanıt — YERİNDE DOĞRULANDI (2026-08-15, executor):** Xcode projesi
   Windows'tan üretilebiliyor; yani iOS ayağı Unity'yi runner'a sokmadan kurulabilir.
   Ölçüm: geçici boş projede `BuildPipeline.BuildPlayer(target: iOS)` → `Succeeded`,
   0 hata / 0 uyarı, çıkış kodu 0, ve dosya sisteminde **`Unity-iPhone.xcodeproj`**
   bulundu (2 670 dosya / 465.9 MB proje ağacı). Ayrıntı ve ham çıktı:
   `verification/02-ios-uretim.md`. Bu satır artık **beyan değil ölçümdür**.

Hat **durmuyor**; 0A adım 2 yeni tanımıyla (iOS ayağı yerel kanıtı) sürüyor. Bu belge
kararın gerekçe kaydı olarak kalır.

Kanıt biçimi metindir (Sözleşme-4); alıntılar resmî Unity dokümanındandır.

## Okunan kaynaklar

| kaynak | neden |
|---|---|
| `docs.unity3d.com/6000.3/Documentation/Manual/LicenseActivationMethods.html` | **pinli sürümün kendi sayfası** — birincil kanıt |
| `docs.unity3d.com/Manual/ManualActivationGuide.html` | manuel aktivasyonun kapsamı |
| `docs.unity3d.com/Manual/ManualActivationCmdWin.html` | Windows komut satırı adımları + kısıt |
| `docs.unity.com/en-us/build-automation` + `docs.unity.com/en-us/devops/pricing/free-plan` + `unity.com/products/compare-plans` | Personal için kalan resmî yol (alternatif) |

## Bulgu 1 — Personal'da GUI'siz aktivasyon yolu YOK (birincil kanıt)

Pinli sürümün "License activation methods" sayfası üç yöntem tanımlıyor:

| yöntem | desteklenen planlar | alıntı |
|---|---|---|
| Unity Hub | tümü (Personal dahil) | *"For Unity Personal, the Unity Hub is the **only** method for activating and returning licences."* |
| Komut satırı | Personal **hariç** | kullanım gerekçesi: *"You have internet access, but you use Unity in headless mode (without a GUI) for automated tasks, such as builds and tests."* — ama prosedür Personal'a uygulanmaz |
| Manuel aktivasyon (`.alf`/`.ulf`) | Personal **hariç** | *"This method isn't supported for Unity licenses under a Personal plan."* |

Manuel aktivasyon sayfası aynı kısıtı bağımsız olarak tekrarlıyor:
*"The manual activation method doesn't work with floating license subscriptions or
Unity Personal."* — ve Personal için Hub'a giriş, iade için Hub'dan çıkış diyor.

Komut satırı aktivasyonunun biçimi de bunu doğruluyor: `-serial SB-XXXX-…-username
-password`. **Personal planda seri numarası yoktur**, dolayısıyla komut zaten
uygulanamaz.

**Sonuç:** 0A.md adım 2(b)'nin tarif ettiği akış — `.alf` üret → `license.unity3d.com`
→ `.ulf` → `UNITY_LICENSE` secret → CI'da activation — **Personal planda resmî olarak
mümkün değildir.** Adım 2(c)'nin canary'si de bu akışa dayandığı için kurulamaz.

## Bulgu 2 — Adım 2a'nın diğer başlıkları konusuz kalıyor

0A.md bu adımda beş başlık istiyordu; Personal'da manuel aktivasyon olmadığı için
dördü **konusuzdur** ve "veri yok" olarak kaydedilir (beyan değil, yokluğun kanıtı
yukarıdaki alıntılardır):

| başlık | durum |
|---|---|
| `.ulf` yeniden kullanımı | **konusuz** — Personal `.ulf` üretilemiyor |
| makine değişimi | **konusuz** — aynı gerekçe |
| yerel lisansa etkisi | **konusuz** — aynı gerekçe |
| web'den seat silme | **konusuz** — Personal iadesi Hub'dan çıkışla yapılır (dokümanın kendi ifadesi) |
| seat limiti | **ÖLÇÜLEMEDİ** — okunan sayfalar Personal Editor lisansının eşzamanlı makine sayısını yazmıyor. Tahmin YAZILMADI (kural 6) |

Manuel aktivasyonla ilgili tek ek not (Personal dışı planlar için geçerli): manuel
aktive edilmiş bir lisans *"can't be returned by using the other license management
methods"* — iade için Unity desteğine başvurulur.

## Bulgu 3 — Personal için kalan resmî yol: Unity Build Automation

Unity'nin kendi CI hizmeti (**Build Automation**, eski Cloud Build) Personal planla
ücretsiz katmanda kullanılabiliyor; lisanslama sorununu ortadan kaldırır çünkü build
Unity'nin kendi altyapısında koşar ve Editor lisansını Unity yönetir. Git ile çalışır.

Ücretsiz katman (okunan değerler):
- 3 seat / organizasyon
- **200 Windows build dakikası** (Micro), **100 Mac dakikası** (Standard),
  **100 Linux dakikası** (Micro)
- 5 GB proje depolama (bazı sayfalarda 25 GB olarak güncellenmiş görünüyor —
  **çelişkili**, ilk gerçek koşuda ölçülmeli)
- Limit bitince kredi kartıyla pay-as-you-go

**Bu bir öneri değil, envanterdir.** Karar insanın/mimarındır (kural 22).

## Değerlendirilen üç seçenek (karar: C+ — aşağıdaki C'nin genişletilmiş hâli)

| seçenek | ne değişir | maliyet / risk |
|---|---|---|
| **A — Unity Build Automation'a geç** | CI omurgası GitHub Actions'tan Unity'ye kayar; lisans sorunu **kökten** biter | Aylık dakika tavanı hattın koşu sıklığını sınırlar (Android build yerelde 3 dk 29 sn ölçüldü; bulutta soğuk build daha uzun). PIPELINE'ın "public runner ücretsiz" CI kararı ve 4 workflow tasarımı yeniden yazılır. iOS için 100 Mac dk/ay ciddi kısıt |
| **B — Unity Pro'ya geç** | `.alf`/`.ulf` ve komut satırı aktivasyonu açılır; 0A.md olduğu gibi yürür | **Para harcaması** — PIPELINE Sözleşme-8: hat standart akışta para harcamaz; bu ancak Aşama 10 yatırım ofisi + kullanıcı onayıyla açılır |
| **C — CI'da Unity'siz kapılar + yerel build** | Lint, secret-scan, test (saf C# katmanı) CI'da koşar; Unity gerektiren build/test **yerelde** koşup kanıtı metin olarak repoya girer | Hello-build'in "yeşil run linki" kanıtı zayıflar; A4 bot/soak kapıları yerel koşuya bağlanır. Sonda bu yolun çalıştığını fiilen gösterdi (tüm kanıtlar yerel batchmode'da üretildi, exit kodlarıyla) |

Seçeneklerin ortak notu: sondanın kanıtladığı üzere **yerel batchmode zinciri
çalışıyor** (EditMode 10/10, PlayMode bot 3/3, Android APK Succeeded). Yani hat
"kanıt üretemiyor" durumunda değil; sorun kanıtın **CI'da** üretilmesidir.

## Hattın durumu (karar sonrası)

C+ ile adım 2 **yeniden tanımlandı**: artık Unity-CI lisans kapısı değil, **iOS ayağının
yerel üretim kanıtı**dır. Kalan tek DUR hakkı oradadır — Xcode projesi Windows'tan
üretilemezse Unity Build Automation'a (seçenek A) düşülür.

C+ mimarisinin bu belgeden doğan bağlayıcı sonuçları:
- CI runner'ında Unity **yok** → `UNITY_LICENSE` benzeri bir Unity hesap secret'ı da
  **yok**; olmayan secret'ın çürümesi de yok, haftalık lisans canary'si **konusuz** kalır
  (0A.md v1.4.0 bunu zaten workflow setinden çıkardı: 3 workflow, hepsi Unity'siz).
- Android kanıtı yerel batchmode + metin; iOS kanıtı yerelde üretilen xcodeproj'un
  macOS runner'da `xcodebuild` ile derlenmesi.
- Sondanın gösterdiği yerel zincir (EditMode 10/10, PlayMode bot 3/3, Android APK
  Succeeded, hepsi exit koduyla) bu mimarinin fiilî ön-kanıtıdır.

Bu belge yazıldığında hiçbir repo açılmamış, hiçbir secret yazılmamış, makinede
değişiklik yapılmamıştı. (Adım 2'nin yeni hâli iOS Build Support modülünü kuracaktır —
makine değişikliği o adımın yetkisindedir ve kanıtı modül listesidir.)
