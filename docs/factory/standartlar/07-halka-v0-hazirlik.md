# Adım 7 hazırlık — private ikiz + halka v0

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).
> Bu dosya **hazırlıktır**: düğmeye kullanıcı basar, executor yalnız metni ve tek
> cümlelik kapı tarifini üretir.

**Tek kaynak uyarısı:** davet metinleri, form soruları, huni tanımı ve kayıt disiplini
**burada tekrarlanmaz** — tek kaynakları `docs/standards/halka-standardi.md`'dir
(§1–§2 davet, §4 form, §5 huni, §8 kayıt). Aşağıdaki adımlar o dosyaya **atıfla** işler;
metin kopyalanırsa iki kaynak doğar ve biri sessizce eskir.

---

## A. `FactoryGames-private` ikizi — insan açar

**Neden executor açmıyor:** private ikiz, `tester_id ↔ gerçek kişi` eşleme tablosunun
tek yeridir (halka-standardi §8). Public repodan ona **bağ kurulmaz**; deponun kendisi
de executor yetkisinin dışındadır (0A yetki genelgesi: "`FactoryGames-private` İNSAN
açar").

**Kullanıcının yapacağı (tek cümlelik kapı tarifi):**

> Halka kaydı için insan gerekli: **github.com/new** sayfasında **Repository name** =
> `FactoryGames-private`, görünürlük **Private** seçili olacak şekilde depoyu oluştur ve
> "Add a README file" kutusunu işaretle — başka hiçbir ayara dokunma. Bitirince 'tamam' de.

**Açıldıktan sonra kullanıcının koyacağı iki dosya** (içeriklerini executor hazırlar,
kullanıcı yapıştırır; ikisi de **yalnız private** ikizde yaşar):

| dosya | ne tutar | neden private |
|---|---|---|
| `halka/eslesme.md` | `tester_id ↔ gerçek kişi` tablosu (tek dosya) | kimlik verisi; public repo **hiç görmez** |
| `halka/envanter.md` | anonim birincil kayıt: `tester_id, tarih, rol, tur, yanıt` — **isim yok** | yerel kopya kaybolursa halkanın yorgunluk/rol geçmişi ölür (halka-standardi §8) |

Public tarafa yalnız **özet/sayım** girer. Yerel `halka/` çalışma kopyası gitignore'ludur
(şablonun `.gitignore`'unda `halka/` zaten var).

**Executor sınırı:** bu depoya erişmeyecek, adını public dosyalarda referans olarak
kullanmayacak, içeriğine bağ kurmayacaktır.

---

## B. Halka v0 iskeleti — ≥5 kişi × 2 tur

**Hedef yapı** (0A adım 7): en az **5 kuran** kişi, **2 tur** kapasitesi. "N" sayısı
**kuran** kişidir, temas eden değil (halka-standardi §5).

### B.1 Davet metni — kaynağı

Kullanıcı davetleri **`docs/standards/halka-standardi.md` §1 (TR)** ve **§2 (EN)**
metinlerini **olduğu gibi** kopyalayarak gönderir. Kurallar §3'tedir ve özetle:

- kişiselleştirme **yalnız selamlamada**;
- **vaat eklenemez** — hediye/ücret yasak (hat para harcamaz), karşılık kendi playtest
  emeğimizdir;
- form dili **testçiyi** takip eder: TR üyeye TR, dış göze EN.

**KVKK/anonimlik cümlesi zaten metnin içindedir** ("anonim kullanım istatistiği…,
kişisel veri/rehber/fotoğraf erişimi istemez, kayıtlar anonimdir — istersen silinmesini
istersin"). Ayrı bir onam metni yazılmaz; ekleme yapılırsa iki kaynak doğar.

### B.2 Kanal planı (halka-standardi §6'ya göre, sayılar burada)

| kanal | v0 hedefi | kural |
|---|---|---|
| Playtest değişimi (r/playmygame + bağımsız geliştirici Discord'ları) | 2–3 kuran | aynı kanala **30 günde en fazla 1** çağrı |
| Kişisel ağ — **oyuncu olmayan** üye bilinçle aranır | 1–2 kuran | B1'in iddiası en sert oyun-dışı gözle sınanır |
| Üniversite kulüpleri (oyun tasarımı toplulukları) | 1–2 kuran | aynı 30-gün limiti |
| **Dış göz** (TR dışı bağlam, EN düşünen) | **≥1 zorunlu** | metinsizlik doğrulaması (§7); yoksa B1 iddiası o koşu düşer — kapı değil, şerh |

Canlı kanal **3'ün altına** düşerse Aşama 10 kanal eskalasyonu açılır (§6).

### B.3 Pencere ve tavan

Davet penceresi **sert tavanlıdır**: `halka_davet_tavan_gun` (Ek C, **kullanıcı yazar** —
0A adım 6 formunda **FORM-BEKLIYOR**). Tavan dolarsa eldeki **kuran** sayısıyla devam
edilir; N rapora yazılır ve küçük örneklem şerhi eklenir (§5). Tavansız bekleme en kötü
tıkanmadır: hiçbir kapı kırmızı yanmaz, hat sessizce durur.

### B.4 v0'da yapılmayacaklar

- Form **doldurulmaz** ve huni ölçülmez — bunlar Aşama 5'in işidir; v0 yalnız
  **iskelet**tir (kişi + tur kapasitesi + kanal listesi).
- Ajan/persona/sentetik panel **yasak**; dış halka insandır (§ başlık kuralı).
- Ücretli panel/servis kullanılmaz.

---

## C. Kullanıcıya gidecek kapı cümleleri (executor sunar, mimar duyurur)

1. **Depo:** yukarıda A bölümündeki tek cümle.
2. **Davet:** *Halka v0 için insan gerekli: `docs/standards/halka-standardi.md` §1 (TR)
   ve §2 (EN) metinlerini olduğu gibi kopyalayıp B.2 tablosundaki kanallara gönder,
   hedef en az 5 kuran kişi; kimlik bilgisini yalnız private ikizdeki `halka/eslesme.md`
   dosyasına yaz. Bitirince 'tamam' de.*

## D. Executor'ın bu adımdaki payı

- Metin **üretmez**, standarda **atıf** yapar (yukarıdaki gibi).
- Private ikize **dokunmaz**.
- Public tarafa yalnız **sayım/özet** satırı yazar (kaç kuran, kaç kanal, dış göz var/yok).
- `halka_davet_tavan_gun` gelene kadar pencere hesabı **FORM-BEKLIYOR** kalır (L8).
