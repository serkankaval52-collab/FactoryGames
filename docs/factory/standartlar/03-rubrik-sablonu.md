# Rubrik şablonu — Aşama 8 insan kapısı

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** eksenlerin tanımı, kimin puanlayabileceği, dış göz kuralı ve
geçiş/geri-kenar mantığı `docs/stages/8.md`'dedir; red-flag insan blokları
`docs/standards/red-flag.md`'de (R2b, R4); görsel tutarlılık beyanı
`docs/standards/gorsel-sozlesme.md` G5'te. Bu dosya yalnız **doldurulacak formun
biçimidir** — kural metni taşımaz.

## Form

```
oyun_id: ..............   build_hash: ..............   tarih: ..........
dis_goz_var_mi: EVET/HAYIR      aktif_eksen_sayisi: 5 veya 3
```

| # | eksen | puan (1–5) | puanlayan | not |
|---|---|---|---|---|
| 1 | ilk-60-sn anlaşılırlık | | **dış göz** (`tester_id`) | kullanıcı puanlayamaz |
| 2 | ilk-başarı hissi | | **dış göz** (`tester_id`) | kullanıcı puanlayamaz |
| 3 | kontrol tepkiselliği | | kullanıcı | |
| 4 | ses-görsel doygunluk | | kullanıcı | |
| 5 | tekrar oynama isteği | | kullanıcı | |

**\*'lı iki eksen (1–2) kullanıcı tarafından puanlanamaz** — gerekçesi 8.md'dedir
(ön bilgi kirlenmesi). Dış göz yoksa rubrik **3 eksene iner** ve kapı öyle işler;
sahte nesnellikle 5 eksen puanlanmaz.

## İkili bloklar (EVET/HAYIR — hepsi zorunlu)

| madde | kaynak | yanıt |
|---|---|---|
| R2b içerik ↔ yaş beyanı uyumu | `red-flag.md` | |
| R4 karanlık desen yokluğu | `red-flag.md` | |
| G5 görsel tutarlılık beyanı (perspektif/çizgi/gölge) | `gorsel-sozlesme.md` | |

## Geri bildirim

```
P0 (yayını engeller) : ...
P1 (bütçeye tabi)    : ...
P2 (sonraki sürüm)   : ...
```

## Karar

```
yazili_yayinla_onayi: EVET/HAYIR        tarih: ..........
```

## Eşik

`rubrik_esik` (Ek C Bölüm-1) — **FORM-BEKLIYOR (L8)**. Kullanıcının 0A adım 6 form
dönüşüne kadar eşik yazılmaz; `ilk-kosu.md` §2 bu satırı **ŞERHLİ** işaretler
(karar geçerlidir, eşik geçicidir ve pencere sonunda revize edilirse **geriye dönük
değişmez**).

## Kayıt

Rubrik satırı `build_hash` ile telemetriye yazılır (red-flag yanıtları dahil) —
alan adları için `04-telemetri-semasi.md`. `tester_id` takma addır; gerçek ad yalnız
private ikizin eşleme dosyasındadır (`halka-standardi.md` §8).
