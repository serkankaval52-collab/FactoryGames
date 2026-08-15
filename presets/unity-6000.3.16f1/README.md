# Preset seti — Unity 6000.3.16f1 (2D / URP)

> **KANONİK DEĞİL — ham çıkarım (0A adım 4 kaydı, 2026-08-15):** bu dizin, şablon
> paketinin Unity'den çıktığı **ham** hâlidir; tarihsel kanıt olarak saklanır (sonda
> ölçümleri bu setle yapıldı, değiştirilmez). Ham şablonun asset şemaları 6000.1
> hedeflidir; pinli 6000.3.16f1 projeyi ilk açılışta şemaları yükseltir (PRESET-SAPMA
> bulgusu, factory.core v0.1.8). Oyun iskeletlerinin kullandığı **kanonik preset**
> `factory.core` reposunda `templates~/` altındadır (yükseltilmiş hâl). Yeni oyun
> kurulumu bu dizinden DEĞİL, factory.core scaffold adımından yapılır.

Bu set **elle yazılmadı, Editor'de üretilmedi**: pinli Unity sürümüyle gelen kendi
şablon paketinden mekanik olarak çıkarıldı (Sözleşme-2, `presets/README.md` "Üretim
yöntemi"). Tek kaynak = pinli sürümle gelen şablon.

## Kaynak

| alan | değer |
|---|---|
| Unity pini | `6000.3.16f1` — changeset `a56f230f6470` (`docs/probe/unity-pin.txt`) |
| Şablon paketi | `com.unity.template.2d-cross-platform-2d-6.1.2.tgz` |
| Paket konumu | `<Unity>\Editor\Data\Resources\PackageManager\ProjectTemplates\` |
| Şablon seçimi | PIPELINE "Kilit Teknik Kararlar" → Render = **URP + 2D Renderer** |
| Çıkarım tarihi | 2026-08-15 (sonda / Aşama -1, ilk koşu) |

Aynı dizindeki diğer şablonlar (`3d-cross-platform-17.0.14`, `3d-high-end-17.0.7`)
kullanılmadı — 2D URP kararı gereği.

## Çıkarım komutları (birebir)

```
tar -xzf "<Unity>\Editor\Data\Resources\PackageManager\ProjectTemplates\com.unity.template.2d-cross-platform-2d-6.1.2.tgz" -C _probe-tpl
robocopy _probe-tpl\package\ProjectData~ presets\unity-6000.3.16f1 /E
```

`_probe-tpl/` geçici çıkarım dizinidir (gitignore `_probe-*/`), set üretildikten sonra
silinir. Kopyalanan kök: paketin `package/ProjectData~` dizini — şablonun proje
gövdesinin tamamı.

## Setin kapsamı

- `ProjectSettings/` — 21 `.asset` (grafik, kalite, fizik, input, oyuncu ayarları)
- `Packages/manifest.json` — paket kilidi (URP 17.0.3, Input System 1.12.0,
  Test Framework 1.4.5, 2D araç zinciri)
- `Assets/Settings/` — `UniversalRP.asset`, `Renderer2D.asset`, sahne şablonları
- `Assets/UniversalRenderPipelineGlobalSettings.asset`, `Assets/DefaultVolumeProfile.asset`
- `Assets/InputSystem_Actions.inputactions`
- `Assets/Scenes/SampleScene.unity` — **varsayılan sahnenin kaynağı**; sahne
  baseline'ı (`docs/probe/scene-baseline.json`) bu dosyanın proje içindeki
  kopyasından ölçülür

## Setten okunan bağlayıcı ayarlar

| ayar | değer | sonucu |
|---|---|---|
| `activeInputHandler` | `1` | **Yalnız yeni Input System**; legacy `UnityEngine.Input.*` API'si projede çalışmaz — girdi okuması `UnityEngine.InputSystem` üzerinden yapılır |
| `defaultScreenOrientation` | `4` (AutoRotation) | dikey/yatay bağımsız yerleşim gerekir (kod-standardi §3) |
| `productName` | `2D_URP` | proje adı kopyada değiştirilmez (kaynağı olmayan durum yaratmamak için) |

## Revizyon 1 — şablon/editör paket uyumsuzluğu (2026-08-15, sonda ilk koşu)

**Belirti:** ham şablon seti kopyalanıp paketler çözümlendiğinde batchmode
**return code 1** verdi; 3 derleme hatası (2 paket):

```
com.unity.collab-proxy@2.6.0  → error CS0104: 'ObjectInfo' is an ambiguous reference
                                between 'Codice.CM.Common.ObjectInfo' and 'UnityEditor.ObjectInfo'
com.unity.inputsystem@1.12.0  → error CS0117: 'BuildTarget' does not contain a
                                definition for 'ReservedCFE'
```

**Kök neden (kod-standardi §9):** hatalar oyun kodunda değil, şablonun pinlediği paket
sürümlerinde. Şablonlar editörden **eski** hedefliyor — `package.json` alanları:
2D şablonu `unity: 6000.1`, 3D şablonu `unity: 2023.3`; kurulu editör `6000.3.16f1`.
UPM bazı paketleri otomatik yükseltti (URP `17.0.3→17.3.0`, test-framework
`1.4.5→1.6.0`) ama manifest'te sabitlenmiş `inputsystem`/`collab-proxy` sürümleri
çözülebilir olduğu için yükselmedi ve editörün API yüzeyiyle uyuşmadı.

**Düzeltme (en küçük güvenli adım):**
1. `com.unity.collab-proxy` kaldırıldı — Unity Version Control arayüzü; hat **git**
   kullanıyor, işlevsel karşılığı yok.
2. `com.unity.inputsystem` kaldırıldı — ölçüldü: paket önbelleğindeki **hiçbir paket
   bu pakete bağımlı değil**, kaldırmak bağımlılık grafiğini kırmıyor.
3. `activeInputHandler: 1 → 0` (Input Manager). Girdi katmanı kaldırılan paketle
   birlikte legacy'ye alındı; sonda girdi ihtiyacı tek dokunuştur.
4. `Assets/InputSystem_Actions.inputactions` (+`.meta`) kaldırıldı — importer'ı
   kaldırılan paketten geliyordu, sahipsiz asset bırakılmadı.

**Doğrulama:** revizyon sonrası batchmode **return code 0**, `error CS` **yok**.

**Borç kaydı (mimar kararı gerekir):** Input System'e ihtiyaç duyan oyun projeleri için
editörle uyumlu sürüm tespiti gerekir; bu tespit paket kayıt defteri sorgusu (ağ) ister
ve bu koşuda insan kapısı açmamak için yapılmadı. Legacy Input Manager kararı **sonda
kapsamıyla sınırlıdır**, hat genelinde bağlayıcı değildir.

## Kural

Bu dizin yalnız PR ile değişir. Unity sürümü yükselince **yeni** `unity-<pin>/`
dizini çıkarılır; bu dizine dokunulmaz (oyunlar kendi piniyle yaşar).
