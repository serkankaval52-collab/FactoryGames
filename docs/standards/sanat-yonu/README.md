# Sanat Yönü Paketleri — `<aile>.md`

`docs/standards/sanat-yonu.md` sürecinin çıktısı; aile başına tek dosya. İçerik:
onaylı paket (10 bölüm: hex paleti + oranlar, kontur, gölgeleme, silüet/geometri,
doku, ışıklandırma, obje/ekran tablosu, hibrit köprüsü, URP 2D yol haritası,
referans eserler).

Üreten: kullanıcı onayı + görsel-model oturumu (v1.3'ten itibaren Arena turları; araç adı
sabit değil — insan kapısı, insan-yuku §1). Tüketen: Aşama 2 — palette.json + manifest üçlüsü buradan
alınır; dosya yoksa veya aile için eskiyse kapı KIRMIZI (sanat-yonu.md "Kurallar").

Ek A aile başına ≤2 canlı oyun aynı paketi kullanır; ikinci oyun yeni tur koşmaz.
Dosya adı = Ek A kataloğundaki stil ailesi adı (küçük harf, tire ile) + `.md`.
Bu dizin satır bütçesine tabi değildir (CI glob'u `docs/standards/*.md`'dir);
paketler yine de kısa tutulur — kural değil, alıntı kaynağıdır.
