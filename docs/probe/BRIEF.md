# SONDA BRIEF'İ — tek ekranlık döngü

Bu dosya sondada Claude Code'a verilen TEK görev tanımıdır. Amaç, fabrika
standartlarının metin olarak tek başına yeterli olup olmadığını da ölçmektir.

## İstenen

- Tek ekranlık hiper-casual döngü, 60–90 saniyelik tur.
- Tek input: ekrana dokun/bırak (tap veya hold — seçimi brief metni belirlemez,
  üreten karar verir ve gerekçesini rapora yazar).
- Skor sayacı, fail durumu, fail sonrası tek dokunuşla restart.
- Android'e derlenebilirlik (APK üretimi CI dışı, yerel build yeterli).

## Kurallar (Sözleşme-2 uygulaması)

- Sahne bootstrap-only: tek sahne ≈ tek GameObject (Bootstrap bileşeni);
  tüm hiyerarşi saf C# kodundan kurulur.
- Ayarlanabilir değerler (hız, skor, eşikler) `StreamingAssets` altında JSON.
- Editor'de elle sahne/prefab kurulumu YOK.
- En az bir EditMode test takımı (çekirdek mantık) + bot ile 3 otomatik döngü
  (PlayMode veya scripted input) hatasız geçmeli.

## Kabul kanıtı

Play mode'da çökme/exception yok; bot çıktı logları dosyada; rapor
`docs/probe/rapor.md`'ye işlendi.

## Devir testi notu

Bu brief aynı zamanda fabrikanın plan→kod devir mekanizmasının minyatürüdür:
fabrikada planı yazacak olan da uygulayıcıdır (Claude Code). Brief uygulanamaz
bulunursa revizyonu — tasarımcı değil — executor yapar ve revizyon rapora
işlenir. İnsan eliyle brief düzeltmesi ölçümü geçersiz kılar.
