# PR şablonu

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** push protokolünün adımları `docs/probe/raporlar/README.md`'de
(8 adım + PII-1 genelgesi), yükseltme sırası `PIPELINE.md` Sözleşme-5'te, kapı
kapsamı `docs/stages/7.md`'nin CI kapısı satırındadır. Bu dosya yalnız **PR gövdesinin
biçimi**dir.

## Gövde

```markdown
## Ne değişti
<tek paragraf: neyin, neden değiştiği>

## Kanıt (beyan değil, koşmuş komut + çıktı)
- lint        : <run linki / yerel çıktı + exit>
- test        : <run linki / yerel çıktı + exit>
- ilgili ölçüm: <ham satır>

## Kapı etkisi
- [ ] Yeni kapı eklendi   → **önce-kırmızı kanıtı**: <link/çıktı>
- [ ] Mevcut kapı gevşedi → gerekçe + karşı önlem
- [ ] Kapı etkisi yok

## Kontrol listesi
- [ ] Repo-içi kimlik doğrulandı (`git config --local user.email` → noreply)
- [ ] Maske taraması: commit'lenen metinlerde 0 eşleşme
- [ ] Ek C'de olmayan sayı kullanılmadı (kural 28)
- [ ] "Veri yok" satırları artefakt kanıtı taşıyor
- [ ] Sunucuda birleştirme YAPILMADI (PII-1) — merge yerelde
- [ ] Ham artefakt (görüntü/log dökümü) eklenmedi

## Risk / geri alma
<geri alma komutu veya "geri alınabilir: tek commit">
```

## Kurallar

1. **Önce-kırmızı zorunlu.** Yeni bir kapı/lint ekleyen PR, o kapının gerçekten kırmızı
   verdiğini gösteren bir kanıt taşır. Yalnız yeşil gösteren kapı, kapı sayılmaz.
2. **Kapı gevşetme ayrı PR'dır.** Bir PR hem özellik hem kapı gevşetmesi taşımaz;
   gevşetme kendi gerekçesiyle görünür olmalıdır.
3. **Yerel merge.** Birleştirme sunucuda yapılmaz (PII-1): merge yerelde, repo-içi
   kimlikle üretilir, push sonrası üst-3 commit `author/committer` denetlenir.
4. **Yükseltme sırası.** Bir bulgu kural değişikliği öneriyorsa sıra: **lint/test →
   kontrol listesi satırı → CLAUDE.md kuralı** (son çare, tavana tabi).
5. **Tek mantıksal adım = tek commit.** Rapor commit'leri `rapor:`, aşama artefaktları
   `0a:`/`sonda:` önekiyle.
