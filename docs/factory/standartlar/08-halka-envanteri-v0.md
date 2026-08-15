# Halka envanteri v0 — kayıt biçimi

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** davet metinleri (§1–§2), kullanım kuralları (§3), form soruları
(§4), huni/pencere (§5), kanallar (§6), dış göz (§7) ve kayıt disiplini (§8)
`docs/standards/halka-standardi.md`'dedir. Rol/rotasyon kısıtları `docs/stages/5.md`
D1'dedir. Açılış adımları `standartlar/07-halka-v0-hazirlik.md`'dedir. Bu dosya yalnız
**envanterin alanlarını** ve **nerede yaşadığını** tanımlar.

## Nerede yaşar (üç katman — karıştırılamaz)

| katman | ne tutar | yer |
|---|---|---|
| **Eşleme** | `tester_id ↔ gerçek kişi` | **yalnız** `FactoryGames-private` · public repo **hiç görmez** |
| **Birincil kayıt** | anonim satırlar (aşağıdaki alanlar) | `FactoryGames-private` |
| **Çalışma kopyası** | aynı satırların yerel kopyası | yerel `halka/` — **gitignore'lu** |
| **Public** | yalnız **özet/sayım** | koşu raporu (isim, iletişim, serbest metin yok) |

## Satır alanları (anonim)

| alan | tip | not |
|---|---|---|
| `tester_id` | takma ad | gerçek ad **yalnız** eşleme dosyasında |
| `tarih` | tarih | temas/kurulum tarihi |
| `rol` | `kuran` \| `oynayan` \| `form` \| `dis_goz` | huni basamağı (§5) |
| `tur` | sayı | 1 veya 2 (v0 iskeleti iki tur taşır) |
| `kanal` | metin | §6 kanal adı |
| `oyun_id` | metin | hangi oyunda |
| `yorgunluk_notu` | metin | rol/rotasyon kısıtı için (5.md D1) |

**Rotasyon kısıtları** (5.md D1'e atıf): aynı oyunda iki rol yok; arka arkaya iki oyunda
aynı rol yok. Seçim sonrası satırlar güncellenir (8.md dış göz seçimi bunu şart koşar).

## v0 hedefi ve sayım

- **≥5 kuran × 2 tur** iskeleti (0A adım 7).
- **≥1 dış göz** zorunlu (§7) — yoksa metinsizlik iddiası o koşu düşer; **kapı değil**,
  şerhli satır.
- "N" **kuran** sayısıdır, temas eden değil (§5).

## Public'e çıkan özet biçimi

```
halka v0: kuran=<n>  kanal=<k>  dis_goz=<var|yok>  tur_kapasitesi=2
```

İsim, iletişim bilgisi, form serbest metni ve ham yanıt **çıkmaz** (Sözleşme-4 + §8).

## FORM-BEKLIYOR (L8)

| alan | durum |
|---|---|
| `halka_davet_tavan_gun` | **FORM-BEKLIYOR** — davet penceresinin sert tavanı; kullanıcı yazar (§5, A6.4) |
| `dis_halka_havuzu`, `halka_hakki` | **FORM-BEKLIYOR** — havuz büyüklüğü ve oyun başına oturum hakkı |

Tavan gelene kadar pencere hesabı yapılmaz. Tavan dolduğunda eldeki **kuran** sayısıyla
devam edilir; N rapora yazılır, küçük örneklem şerhi eklenir. Tavansız bekleme en kötü
tıkanmadır: hiçbir kapı kırmızı yanmaz, hat sessizce durur (§5).

## Executor sınırı

Executor bu envanteri **doldurmaz** ve private ikize **erişmez**; yalnız public özet
satırını üretir ve rol/rotasyon kısıtlarının ihlal edilip edilmediğini **sayımla**
kontrol eder.
