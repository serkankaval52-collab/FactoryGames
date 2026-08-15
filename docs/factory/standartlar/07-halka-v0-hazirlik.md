# Adım 7 hazırlık — private ikiz + halka v0

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).
> Bu dosya **hazırlıktır**: düğmeye kullanıcı basar, executor yalnız metni ve tek
> cümlelik kapı tarifini üretir.

**Tek kaynak uyarısı:** davet metinleri, form soruları, huni tanımı ve kayıt disiplini
**burada tekrarlanmaz** — tek kaynakları `docs/standards/halka-standardi.md`'dir
(§1–§2 davet, §4 form, §5 huni, §8 kayıt). Metin kopyalanırsa iki kaynak doğar.

---

## A. `FactoryGames-private` ikizi — insan açar

**Neden executor açmıyor:** private ikiz, `tester_id ↔ gerçek kişi` eşleme tablosunun
tek yeridir (§8); public repodan ona bağ kurulmaz ve depo executor yetkisinin dışındadır
(0A yetki genelgesi: "`FactoryGames-private` İNSAN açar").

**Kullanıcının yapacağı (tek cümlelik kapı tarifi):**

> Halka kaydı için insan gerekli: **github.com/new** sayfasında **Repository name** =
> `FactoryGames-private`, görünürlük **Private** seçili olacak şekilde depoyu oluştur ve
> "Add a README file" kutusunu işaretle — başka hiçbir ayara dokunma. Bitirince 'tamam' de.

**Açıldıktan sonra iki dosya** (içeriklerini executor hazırlar, kullanıcı yapıştırır;
ikisi de **yalnız private** ikizde yaşar):

| dosya | ne tutar |
|---|---|
| `halka/eslesme.md` | `tester_id ↔ gerçek kişi` — kimlik verisi; public repo **hiç görmez** |
| `halka/envanter.md` | anonim birincil kayıt (`tester_id, tarih, rol, tur, yanıt` — isim yok); yerel kopya kaybolursa halkanın yorgunluk/rol geçmişi ölür (§8) |

Public tarafa yalnız **özet/sayım** girer; yerel `halka/` çalışma kopyası gitignore'ludur.
**Executor sınırı:** bu depoya erişmez, içeriğine bağ kurmaz.

---

## B. Halka v0 iskeleti — **≥5 kuran** × 2 tur

**Hedef yapı** (0A adım 7): en az **5 kuran** kişi, **2 tur** kapasitesi. "N" sayısı
**kuran** kişidir, temas eden değil (halka-standardi §5).

### B.1 Davet metni — kaynağı

Davetler `halka-standardi.md` **§1 (TR)** / **§2 (EN)** metinlerinden **olduğu gibi**
kopyalanır; kullanım kuralları §3'tedir (kişiselleştirme yalnız selamlamada; **vaat
eklenemez** — hediye/ücret yasak, karşılık kendi playtest emeğimiz; form dili testçiyi
takip eder: TR üyeye TR, dış göze EN).

**KVKK/anonimlik cümlesi zaten davet metninin içindedir** (anonim kullanım istatistiği,
kişisel veri/rehber/fotoğraf erişimi yok, kayıtlar anonim ve silinebilir). Ayrı onam
metni **yazılmaz** — ikinci kaynak doğar.

### B.2 Kanal planı (halka-standardi §6'ya göre, sayılar burada)

| kanal | v0 hedefi | kural |
|---|---|---|
| Playtest değişimi (r/playmygame, geliştirici Discord'ları) | 2–3 kuran | 30 günde en fazla 1 çağrı |
| Kişisel ağ — **oyuncu olmayan** üye | 1–2 kuran | B1 en sert oyun-dışı gözle sınanır |
| Üniversite kulüpleri | 1–2 kuran | aynı 30-gün limiti |
| **Dış göz** (TR dışı, EN düşünen) | **≥1 zorunlu** | §7; yoksa B1 iddiası düşer — kapı değil, şerh |

Canlı kanal **3'ün altına** düşerse Aşama 10 kanal eskalasyonu açılır (§6).

### B.3 Pencere ve tavan

Davet penceresi **sert tavanlıdır**: `halka_davet_tavan_gun` (Ek C, **kullanıcı yazar** —
**FORM-BEKLIYOR**). Tavan dolarsa eldeki **kuran** sayısıyla devam edilir; N rapora
yazılır, küçük örneklem şerhi eklenir (§5). Tavansız bekleme en kötü tıkanmadır: hiçbir
kapı kırmızı yanmaz, hat sessizce durur.

**v0'da yapılmayacaklar:** form doldurulmaz, huni ölçülmez (Aşama 5'in işi; v0 yalnız
iskelettir). Ajan/persona/sentetik panel **yasak** — dış halka insandır; ücretli
panel/servis kullanılmaz.

---

## C. Kapı cümleleri (executor sunar, mimar duyurur)

1. **Depo:** A bölümündeki tek cümle.
2. **Davet:** *Halka v0 için insan gerekli: `docs/standards/halka-standardi.md` §1 (TR)
   ve §2 (EN) metinlerini olduğu gibi kopyalayıp B.2 tablosundaki kanallara gönder,
   hedef en az 5 kuran kişi; kimlik bilgisini yalnız private ikizdeki `halka/eslesme.md`
   dosyasına yaz. Bitirince 'tamam' de.*

## D. Executor'ın payı

Metin **üretmez** (atıf yapar), private ikize **dokunmaz**, public tarafa yalnız sayım
yazar (kuran / kanal / dış göz); `halka_davet_tavan_gun` gelene dek pencere hesabı
**FORM-BEKLIYOR** (L8).
