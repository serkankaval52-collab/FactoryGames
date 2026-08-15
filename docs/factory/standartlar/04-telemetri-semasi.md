# Telemetri şeması — `.factory/telemetry.jsonl`

> **TASLAK** — mimar incelemesi geçmeden "standart" sayılmaz (0A adım 6, v1.4.3).

**Tek kaynak uyarısı:** alan listesinin normatif tanımı `docs/PIPELINE.md`
**Sözleşme-1**'dedir; `kapi_sonucu` değer kümesi ve `serhli` işareti
`docs/standards/ilk-kosu.md` §1'dedir. Yazıcı uygulaması `factory.core`
`Runtime/TelemetryWriter.cs`'tir. Bu dosya yalnız **biçim + örnek + doğrulama
kuralları** verir.

## Biçim

Append-only **JSONL**; her aşama giriş/çıkışında bir satır. Dosya oyun reposundadır.

| alan | tip | not |
|---|---|---|
| `ts` | ISO-8601 UTC | `TelemetryWriter` üretir |
| `asama` | metin | `0A`, `1`, `4`, `10` … |
| `olay` | metin | `giris`, `cikis`, `kapi` … |
| `sure_dk` | sayı | **InvariantCulture** |
| `kapi_sonucu` | `gecti` \| `kaldi` \| `veri_yok` \| `null` | küme `ilk-kosu.md` §1'den |
| `insan_saat` | sayı | insan yükü |
| `factory_core_surumu` | metin | UPM `#tag` |
| `build_hash` | metin | artefakt kimliği |
| `ci_dakika` | sayı | koşu tüketimi |
| `serhli` | bool (opsiyonel) | ŞERHLİ karar işareti — **sonuç değil işarettir** |

## Örnek satır

```json
{"ts":"2026-08-15T14:07:52Z","asama":"0A","olay":"kapi","sure_dk":6.8,
 "kapi_sonucu":"gecti","insan_saat":0,"factory_core_surumu":"v0.1.8",
 "build_hash":"520f29e","ci_dakika":68.0}
```

## Doğrulama kuralları

1. **Kültür bağımsızlığı zorunlu.** Tüm sayılar `InvariantCulture` ile yazılır; ondalık
   ayıracı `.`'tır. (Saha bulgusu: tr-TR virgülü ölçüm alanlarına sızıyordu.)
2. **"veri yok" geçti sayılmaz.** `kapi_sonucu` üç değerlidir; Aşama 10 özeti geçti /
   kaldı / veri-yok'u **ayrı sütunlarda** sayar.
3. **ŞERHLİ bir sonuç değildir.** `gecti`/`kaldi` satırında `serhli:true` işaretidir.
4. **Beyan yasak.** Her satırın kaynağı bir artefakttır (damga, CI çıktısı, XML, dosya);
   `insan_saat` dışındaki alanlar elle yazılmaz (Sözleşme-10).
5. **Sır girmez.** Token/anahtar/kimlik alanı yoktur; `build_hash` kısa SHA'dır.

## Ölçülemeyen alan davranışı

Alan ölçülemiyorsa **uydurulmaz**: `kapi_sonucu` `veri_yok` olur ve satır, yokluğun
artefaktını taşıyan bir kanıt satırıyla birlikte rapora düşer (ör. "billing API `user`
scope istiyor; scope istenmedi"). `ci_dakika` gibi alanlarda ölçüm türetilebiliyorsa
**yöntem raporda yazılır**.
