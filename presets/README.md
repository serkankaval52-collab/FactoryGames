# PRESETS — Unity motor ayarlarının sürümlü tek kaynağı (Sözleşme-2)

Bu dizin, Unity projelerinin motor ayarlarının tek kaynağıdır. Oyun projeleri
(ve sonda projesi) bu ayarları buradan **kopyalar** — Editor'de elle kurulmuş
ayar "kaynağı olmayan durum"dur ve CI'da kırmızıdır.

## Yapı

- `unity-<pin>/` — Unity `<pin>` sürümüne ait set (`manifest.json`,
  `GraphicsSettings.asset`, `QualitySettings.asset`, URP asset'leri vb.).
- Her setin kendi kaydı: hangi Unity sürümünden, hangi şablon paketinden ve
  hangi komutla çıkarıldığı (set dizinindeki README).

## Üretim yöntemi (ilk seferde bir kez — `docs/stages/sonda.md`)

Set, elle yazılmaz veya Editor'de üretilmez: Unity'nin **kendi şablon
paketinden** (kurulum dizinindeki ProjectTemplates arşivi; yoksa resmî Unity
kaynağından) mekanik çıkarılır. Tek kaynak = pinli sürümle gelen şablon.

## Kurallar

- Preset değişikliği yalnız PR ile; sapma testi CI'da (oyun projesi kopyası
  buradaki setle birebir olmalı — kopya dışı fark = kırmızı).
- Unity sürümü yükselince .asset şeması değişebilir: yeni sürüm için YENİ
  `unity-<pin>/` dizini çıkarılır; eskisi dokunulmaz kalır (oyunlar kendi
  piniyle yaşar).
