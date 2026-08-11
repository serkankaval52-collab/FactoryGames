# RED-FLAG KONTROL LİSTESİ — Aşama 7 politika ön denetimi (9 ikili madde)

Her madde EVET/HAYIR'dır; tek HAYIR kapıdan döndürür (Aşama 7 geri kenarı
kaynak düzlemine yollar). **Kontrol** sütunu soruyu KİMİN yanıtladığını yazar:
**OTOMATİK** = CI/bot (Aşama 7 içinde sessiz akar), **İNSAN** = Aşama 8'in ikili
kontrol listesinde yaşar — Aşama 7 otonomdur, içine insan işi konmaz.

| # | Madde | İkili soru | Kontrol |
|---|---|---|---|
| R1 | Reklam sıklığı | Sınırlar içinde mi: oturum başına tam-ekran ≤ Ek C `reklam_siklik_tavan`; iki tam-ekran arası ≥ Ek C `reklam_arasi_min_sn`; açılışta reklam YOK; kaybın hemen ardından reklam YOK; ödüllü reklam isteğe bağlı + etiketli; tür kırılımı: Ek C `reklam_ilk_gun_sifir_turler`'deki türlerde (vars. bulmaca/mantık) ilk gün tam-ekran YOK | OTOMATİK (config lint + bot oturumunda olay-sayı/sıra kontrolü) |
| R2a | Yaş sınıfı SDK yapılandırması | K1 beyanı Families ise çocuk-yönelimi/içerik-sınırı bayrakları AÇIK, genel kitle ise KAPALI mı (SDK manifest/config) | OTOMATİK (manifest/config assertleri) |
| R2b | İçerik ↔ yaş beyanı uyumu | Görsel/işitsel içerik, beyan edilen yaş sınıfıyla mağaza gözüyle uyumlu mu | İNSAN (Aşama 8) |
| R3 | Lisans defteri | Her üçüncü-taraf varlığın defter kaydı var mı (kaynak URL, lisans tipi, indirme tarihi, lisans metni kopyası); fontlarda gömme izni açıkça işaretli mi | OTOMATİK (CI defter↔dosya paritesi; **yeni lisans AİLESİ ilk kez geliyorsa insana** — beyaz liste defterdedir) |
| R4 | Karanlık desen yokluğu | Sahte aciliyet yok; yapay bekleme yok; kaybı zorla reklamla kurtarma yok; çocuğu hedefleyen manipülasyon yok | İNSAN (Aşama 8 — R1 sayısalları devrede ama niyet yargıdır) |
| R5 | Gizlilik paketi | Politika URL'si CANLI mı; Play Data Safety + Apple App Privacy beyanları SDK manifest'inden türetilmiş şablonla DOLU mu; EEA rıza akışı (CMP/UMP) entegre mi | OTOMATİK (URL probe + dosya varlığı + config bayrağı) |
| R6 | Fabrika içi örtüşme | Diğer fabrika oyunlarıyla varlık-hash örtüşmesi ve palet/UI eşleşmesi Ek C `ortusme_esik_yuzde` altında mı | OTOMATİK (CI karşılaştırması — repo/defter ikilisinden) |
| R7 | Görsel kaynağı | Mağaza/screenshot görselleri aynı koşunun GERÇEK build artefaktından otomatik mi (elle kompozisyon/render/mockup YASAK) | OTOMATİK (artefakt kökeni: aynı koşu çıktısı kaydı) |
| R8 | Uygulama boyutu | APK/IPA boyutu Ek C `uygulama_boyut_tavan_mb` içinde mi | OTOMATİK (CI boyut kapısı) |
| R9 | Ekran uyumu | B7 matrisinin her hücresinde hiçbir UI öğesi güvenli alan dışında veya üst üste mi — değil mi | OTOMATİK (bot ekran görüntüsü + RectTransform ∩ güvenli-alan asserti) |

Notlar:
- R2 iki parçadır: yapılandırma (R2a) otomatik, içerik-beyan uyumu (R2b) insan
  yargısıdır. İkisini tek maddede otomatiğe yazmak sahte yeşil üretir.
- İnsan satırları (R2b, R4) Aşama 7'nin çıktısı DEĞİL, Aşama 8'in çıktıdır;
  Aşama 7 PASS = tüm OTOMATİK satırlar yeşil demektir.
- Sayısal sınırlar Ek C'de yaşar (Sözleşme-8); bu dosya yalnız ikili soruları
  ve kontrol sahibini tanımlar.
