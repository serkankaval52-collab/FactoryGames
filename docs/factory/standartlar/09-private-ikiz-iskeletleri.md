# Private ikiz — iki dosyanın iskeleti

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Bu iskeletler public'tir; İÇERİK (gerçek kişiler) yalnız private ikizde yaşar;
public'ten oraya bağ kurulmaz.**

**Tek kaynak uyarısı:** alan tanımları, üç katmanlı kayıt düzeni, rol/rotasyon kısıtları
ve public'e çıkan özet biçimi `08-halka-envanteri-v0.md`'dedir (o da `halka-standardi.md`
§5/§6/§8 ile `5.md` D1'e atıf yapar). Burada yalnız **yapıştırılacak boş biçim** vardır;
tanım tekrarlanmaz.

---

## (a) `halka/eslesme.md` — kimlik tablosu

Bu dosya `tester_id ↔ gerçek kişi` eşlemesinin **tek yeridir**. Executor bu dosyaya
erişmez; içeriği hiçbir public metne, rapora veya commit mesajına girmez.

```markdown
# Eşleme tablosu — YALNIZ PRIVATE

Bu dosya kimlik verisi taşır. Public repoya kopyalanmaz, alıntılanmaz, özetlenmez.
Silme talebi gelirse satır buradan silinir; `envanter.md` satırı `tester_id` ile
anonim kalmaya devam eder.

| tester_id | kişi (ad / erişim) | katılım tarihi | notlar |
|---|---|---|---|
| t01 |  |  |  |
| t02 |  |  |  |
| t03 |  |  |  |
| t04 |  |  |  |
| t05 |  |  |  |
```

`tester_id` takma addır ve sıralıdır (`t01`, `t02`, …); anlam taşımaz — kişiyle
ilişkisi yalnız bu tabloda kurulur.

---

## (b) `halka/envanter.md` — anonim birincil kayıt

Alan başlıkları `08-halka-envanteri-v0.md` "Satır alanları (anonim)" bölümünden gelir;
**isim, iletişim bilgisi ve form serbest metni bu dosyaya girmez.**

```markdown
# Halka envanteri — anonim birincil kayıt

Kimlik YOK. Kişiye çözülebilir hiçbir alan tutulmaz; eşleme ayrı dosyadadır.
Rol/rotasyon kısıtları: aynı oyunda iki rol yok, arka arkaya iki oyunda aynı rol yok.

| tester_id | tarih | rol | tur | kanal | oyun_id | yorgunluk_notu |
|---|---|---|---|---|---|---|
| t01 |  |  |  |  |  |  |
| t02 |  |  |  |  |  |  |
| t03 |  |  |  |  |  |  |
| t04 |  |  |  |  |  |  |
| t05 |  |  |  |  |  |  |

## Koşu özeti (public'e çıkan tek satır)

halka v0: kuran=<n>  kanal=<k>  dis_goz=<var|yok>  tur_kapasitesi=2
```

`rol` değerleri ve özet satırının biçimi `08`'de tanımlıdır; burada tekrarlanmaz.

---

## (c) Kullanıcının yapıştırma yolu

`FactoryGames-private` deposu açıldıktan sonra, GitHub web arayüzünde **Add file →
Create new file** ile önce `halka/eslesme.md`, sonra `halka/envanter.md` dosyalarını
kullanıcı **kendisi** oluşturur ve yukarıdaki kod bloklarının içeriğini yapıştırır
(dosya adını `halka/` önekiyle yazmak klasörü kendiliğinden açar); her iki dosyayı da
**Commit new file** ile kaydeder. Bu depoya executor erişmez, adını public dosyalarda
referans dışında kullanmaz ve içeriğine bağ kurmaz.

## Doldurma sırası

1. Davetler gönderilir (`07` §B.1 — metinler `halka-standardi.md` §1/§2'den).
2. **Kuran** çıktıkça `eslesme.md`'ye kişi, `envanter.md`'ye anonim satır eklenir.
3. Public tarafa yalnız özet satırı geçer; N **kuran** sayısıdır (temas değil).
