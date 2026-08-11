# KOD STANDARDI — saha doğrulamalı kod kuralları (v1.0.6)

Kaynak: yayınlanmış Unity projesinden (DayamaOkey) damıtılmış saha çerçevesi; her
madde orada gerçek bir hatayı önlerken doğdu. Mimari çatışanlar açık gerekçeyle
değiştirildi/reddedildi (sessiz atlama yok). Dağıtım iki dosya: bu + kök `CLAUDE.md`.

## 1. Saf mantık ↔ runtime ayrımı + tek kaynak (kaynak §2.1)

Hesap/kural Unity API'sine dokunmaz; sahne tarafı iş kuralı içermez — EditMode
testi ancak böyle koşar. Formül kopyalanmaz (Sözleşme-2'nin kod karşılığı):
türetilen değer kaynağı çağırır; ikinci yazım bug stokudur. Desen:

    public static class SkorKurallari { public static int HamlePuani(int k,int s)=>k*10+s; } // Hesaplayıcı: Unity'siz, saf; EditMode bunu vurur
    public class SkorYazici:MonoBehaviour { public void Goster(int p)=>_metin.text=p.ToString(); } // Uygulayıcı: içinde İŞ KURALI YOK

## 2. Gevşek bağlılık: C# `event`/`Action` (kaynak §2.1)

`UnityEvent` YASAK (GC allokasyonu + Inspector-bağlı kayıt; bizde Inspector'ı
okuyan yok). Abonelik OnEnable/OnDisable çiftiyle simetrik açılır-kapanır.

## 3. Duyarlı yerleşim + hesapla-önce-uygula (kaynak §2.2+§2.3)

- HAM Pos X/Y tek cihazdan asla yazılmaz: ekran↔tasarım farkından ters türetilir,
  formüle çevrilir (girdi: safe area + en-boy; çıktı: konum). R9'un yöntemi budur.
- Her UI ekranına çakışma matrisi testi: B7'nin tüm hücrelerinde öğe↔öğe ve öğe↔güvenli-alan asserti; "bende çalışıyor" kanıt değil.
- Geri dönüşü zor karar (şema/ekonomi/yerleşim sabiti) önce sayısal fizibilite
  tablosuna düşer; uygulama onaydan sonra. Tahminle değişiklik yok.

## 4. ScriptableObject: REDDEDİLDİ (açık gerekçe)

`.asset` yine GUID'li YAML üretir: diff insan-okunamaz, CI yeniden üretemez —
Sözleşme-2 ihlali olurdu. Kaynak gerekçe ("tasarımcı Inspector'dan değiştirir")
geçersiz: Inspector okuyan tasarımcı yok. Yapılandırma `StreamingAssets/*.json`'da
kalır (tek kaynak, diff okunur).

## 5. Bağımlılık çözümü — bizim sıramız daha katı (değiştirilerek alındı)

Tek geçerli yol: **kodda açık bağlama** (kurucu veya fabrika metodu — hiyerarşi
kodda kurulur, referans kurulum anında verilir). `GameObject.Find` ve
`FindFirstObjectByType` ikisi de YASAK: sıra bağımlı, deterministik değil, bot
testini kırar. Kaynağın `[Header]`/`[Tooltip]`/`[RequireComponent]` maddeleri
ALINMADI: Inspector'da okuyan insan varsayar; bu hatta okuyucu yok.

## 6. İsimlendirme + tek dil (kaynak §3.1)

| Tür | Kural | Örnek |
|---|---|---|
| sınıf/struct/enum/metot/property/event | PascalCase | `OyunDongusu.HamleYap()` |
| parametre/yerel değişken | camelCase | `kalanSure` |
| private alan | `_camelCase` | `_skor` |
| const / static readonly | UPPER_SNAKE | `MAX_CAN` |
| dosya adı | içerdiği ana türle aynı | `OyunDongusu.cs` |

Tanımlayıcılar tek dilde (hat dili Türkçe; API/SDK adları hariç); karışık isim lint'e düşer.

## 7. Klasör hiyerarşisi (kaynak §3.2)

`Core/` (MonoBehaviour-bağımsız saf mantık), `AI/`, `Network/`, `UI/`, `Editor/`;
Core Unity bağımlılığı taşımaz, UI iş kuralı içermez, kökte dosya bırakılmaz.

## 8. Performans + loglama (kaynak §3.4+§3.5)

- `Update`'te allokasyon yok (string birleştirme, LINQ, closure dahil);
  `GetComponent*` Awake/OnEnable'da cache'lenir.
- Sık üretilen nesne pooling'den gelir; Instantiate/Destroy döngüsü yok.
- Runtime'da reflection YASAK (IL2CPP stripping geri dönülmez kırar).
- `Debug.Log*` yalnız geliştirmede (`#if UNITY_EDITOR || DEVELOPMENT_BUILD`);
  release build log yazmaz.

## 9. Hata ayıklama — tahmin değil, sınıflandırma (kaynak §6)

1. Belirti + yeniden-üretme adımı yazılır; kök neden üç kategoriye indirilir:
   (a) zamanlama/sıra, (b) durum makinesi varsayımı, (c) referans yaşam döngüsü.
   İndirilemiyorsa yama YAZILMAZ; önce gözlem (log/assert) eklenir.
2. Kök neden bulunmadan "düzeltildi" denmez. (§6.5) aynı desen başka yerde taranır,
   rapora yazılır. (§6.7) uyarı yok sayılmaz: giderilir veya `#pragma`+gerekçeyle bastırılır.

## 10. Prefab disiplini (kaynak §4'ün TAMAMI — varlık prefabına iznin fiyatı)

İzin: prefab yalnız varlık olarak (efekt, tema, UI yaprağı), yalnız `Assets/Prefabs/`
altında; sahne yine şablon varsayılanıdır, örnekleme koddan. Yarısını almak YOK —
otonom executor'da kopan referansı fark edecek göz olmadığından maliyet insanlı
projedekinden YÜKSEK:
- Yeniden adlandırmada `[FormerlySerializedAs]` ZORUNLU.
- Prefab düzenleyen her Editor script'i iki geçişli: salt-okunur Dump → idempotent
  Apply (iki koşu = aynı sonuç).
- Yalnız tema/görünüm değişiyorsa RectTransform/konum hattına DOKUNULMAZ; prefab
  YAML'i elle/kör bul-değiştir ile düzenlenmez (Sözleşme-2 sürer).
- Play Mode değişikliği kaybolur (kalıcı iş Edit Mode'da); silme yerine devre dışı
  bırakılır — silme, "kim kullanıyor" referans taraması raporlandıktan sonra.
