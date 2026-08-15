# 0A / Adım 9 — MCP + iki-durum teyidi

**Tarih (UTC):** 2026-08-15 · **Yapan:** executor (otonom) · **Sonuç:** **GEÇTİ**
**Proje:** `factorygames-hello` (şablondan türemiş oyun reposu)

İki durum ilkesi (PIPELINE "İki durum"): proje ya **EDITOR OTURUMU**'ndadır (MCP canlı,
batchmode yasak) ya **başsız**dır (Editor kapalı, batchmode koşar). Bekçi
`Temp/UnityLockfile`; geçişleri **executor komutla** yapar, insan kapısı değildir.

## Damgalar (ham)

```
editor-acik-1.ts    → oturum açıldı
editor-kapali-1.ts  → oturum kapandı
```

`.markers/` yereldir; ham içerikler rapora taşınır (Sözleşme-10).

## Geçiş kanıtı

| # | adım | ölçüm | sonuç |
|---|---|---|---|
| 1 | Oturum öncesi | `Temp/UnityLockfile` yok; Unity süreç taraması yapıldı | temiz başlangıç |
| 2 | **Editor oturumu açıldı** (executor komutu: `Unity.exe -projectPath <p> -logFile <l>`) | PID doğrulandı | oturum canlı |
| 3 | Kilit **canlı mı** (FALLBACK yordamı) | `[IO.File]::Open(lockfile,'Open','ReadWrite','None')` → **açılamadı** | **CANLI KİLİT** (kalıntı değil) |
| 4 | **Editor kapatıldı** (executor komutu: `CloseMainWindow`) | süreç 10 sn içinde sonlandı | kapandı |
| 5 | Kapanış kanıtı | `Temp/UnityLockfile` → **KAYBOLDU** | iki-durum geçişi tamam |
| 6 | Başsız duruma geçiş | batchmode `-quit` koşuldu, `return code 0` | başsız durum çalışıyor |

**Kritik ayrım doğrulandı:** aynı yordam (`exclusive open`) canlı oturumda "açılamadı"
verirken, sondada gözlenen kalıntı durumunda "açıldı" veriyordu. Yani FALLBACK'teki
kalıntı ayrımı **her iki yönde de** ölçülmüş durumdadır — yanlış pozitif üretmiyor.

## FALLBACK CLI eşdeğeri (koşuldu)

MCP'nin `Unity_GetConsoleLogs` yüzeyi yerine `FALLBACK.md`'deki komut satırı karşılığı
koşuldu:

```
Unity.exe -batchmode -quit -projectPath <hello> -logFile -
→ Exiting without the bug reporter. Application will terminate with return code 0
→ error CS / Exception taraması: (yok) — konsol temiz
```

Yani MCP kopuk/kapalıyken de konsol-hata gözlemi yapılabiliyor; zorunlu adım MCP'ye
bağımlı değil (Sözleşme-6).

## MCP durumu — TETİKLENMEDİ (bulgu)

`factorygames-hello/Packages/manifest.json` içinde `com.unity.ai.assistant` **yoktur**;
dolayısıyla bu projede MCP köprüsü kurulu değildir ve **hiç tetiklenmemiştir**.

Bu bilinçli bir durumdur, eksiklik değil:

- Resmî köprünün kendisi **kurulum satır 8**'de kanıtlanmıştır (handshake + araç listesi
  + `Unity_RunCommand` kapalı + kilit serbest); o kanıt makine düzeyindedir ve
  `Unity.AI.MCP.ProjectSettings.v2` ayarı **kullanıcı genelinde** kalıcıdır.
- Hello-build bir **ölçüm düzeneğidir**, MCP gözlemine ihtiyaç duyan bir üretim koşusu
  değildir. Paketi buraya eklemek, C+ ilkesinin tersine, projeye gereksiz bir AI yüzeyi
  taşırdı.
- Sondadaki kayıt da aynı yöndeydi: "MCP tetiklenmedi" geçerli bir bulgudur ve
  Sözleşme-2'nin MCP dayanağının **0B'de bilinçli sınanacağı** kararı sürmektedir.

**Kural 30 uyumu:** bu koşuda hiçbir üçüncü taraf MCP köprüsüne bağlanılmadı.

## Kural 26 uyumu — saha kaydı

> **Yerinde düzeltme (v1.4.4, PII-2):** bu bölümün ilk hâlinde dış-proje yolu ve adı
> maskelenmemişti (maske haritası "proje" maddesi ihlali); mimar maskeli düzeltme
> yaptı. Tarih yeniden yazılmadı (PII-1 genelgesi madde 3: denetim dalında zincir
> bozulmaz; ihlal bu kayıtla yaşanır).

Adım koşulurken makinede **kullanıcının kendi Unity projesi açıktı**
(`<ev dışı yol>\<proje>`, ayrı süreç). Bu süreç:

- **tespit edildi** (süreç komut satırından proje yolu okunarak),
- **dokunulmadı** — kapatılmadı, duraklatılmadı, projesine erişilmedi,
- koşu boyunca ve koşu sonunda **çalışmaya devam etti** (doğrulandı).

Kendi oturumum ayrı bir PID ve ayrı bir `Temp/UnityLockfile` üzerinden yürüdü; iki proje
birbirinin bekçisine dokunmadı. Bu, "iki durum" ilkesinin **proje bazlı** olduğunun da
saha kanıtıdır.
