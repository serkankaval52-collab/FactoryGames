# docs/probe/raporlar/ — mimar kopyaları (maskeli koşu raporları)

Her koşunun **commit'lenebilir tek kanıt kanalı**. Ham rapor makinede kalır (`docs/probe/`
altında, gitignore'lu); bu dizine yalnız **maskeli** kopya girer. Kaynak: kurulum kapanış
turu, executor soruları S1–S3 (2026-08-15; mimar genelgeleri, v1.3.5).

## Kanal ve DAR push yetkisi (executor için tek repo-yazma istisnası)

- Yalnız bu dizin (`docs/probe/raporlar/*.md`), yalnız `arena/019fcd97-factorygames` dalı.
- Tek commit = tek rapor dosyası; mesaj öneki `rapor:` (provenance işareti). Etiket YOK,
  force YOK, başka dosya YOK; diğer her repo yazması mimardadır.
- Push öncesi zorunlu kontroller — herhangi biri kırmızıysa DUR, mimara bildir:
  1. `git pull --ff-only` (fast-forward değilse rebase/merge YOK)
  2. repo-içi kimlik (aşağısı) + `--local` doğrulaması
  3. dosya yazıldıktan sonra maske taraması → **0 eşleşme** (desenler: makine adı,
     kullanıcı adı, ev yolu, e-posta, lisans serisi, proje kimlikleri, token önekleri)
  4. commit: tek dosya, `rapor:` öneki
  5. `git log -1 --format="%an <%ae>"` → noreply GÖRÜNMELİ; değilse PUSH YOK — push
     EDİLMEMİŞ commit'te `git commit --amend --reset-author` serbesttir; push edilmiş
     tarih yeniden yazılmaz (mimara bildir)
  6. `py -3.12 tools/arac_suzgec.py` → exit 0
  7. `py -3.12 tools/esik_kapsama.py` → exit 0
  8. push → `git ls-remote origin refs/heads/arena/019fcd97-factorygames` ile teyit
- Repo-içi kimlik HER KOŞUDA, KOŞULSUZ kurulur; "gerekirse" YOK (tuzak 2026-08-15'te
  görüldü: `git config <anahtar>` lokalsiz sorguda sessizce global'e düşer ve gerçek
  e-posta public tarihe sızabilirdi): `git config user.name "FactoryGames Executor"` +
  `git config user.email "serkankaval52-collab@users.noreply.github.com"`
  (public tarihe gerçek e-posta GİRMEZ); doğrulama yalnız `git config --local` ile.
- Kullanıcının kopyala-yapıştırı YEDEK kanal olarak sürer.

## Dosya adı

`YYYY-AA-GG-<asama>.md` (UTC günü; ör. `2026-08-15-kurulum.md`). Aynı aşamanın tekrar
koşusu `-2`, `-3` soneki alır; eski dosya SİLİNMEZ, üzerine yazılmaz.

## Maske haritası (hepsi zorunlu)

| ham değer | maskeli biçim |
|---|---|
| hostname / makine adı | `<makine>` |
| `C:\Users\<ad>` ve türevleri | `<ev>` |
| e-posta adresleri | `<hesap>` |
| lisans serisi / ULF satırı | `<lisans>` |
| GCP / bulut proje kimlikleri | `<proje>` |
| token / anahtar / parola | ASLA giremez (kural 25) |

Notlar (mimar kararları, 2026-08-15): kimlik taşımayan tarih alanları HAM kalabilir — ULF
`StartDate`/`UpdateDate`/`InitialActivationDate` (vade aritmetiğinin kanıtı onlar;
`SerialMasked` maskeli kalır). İkincil hesap adları `<hesap>` sayılır (ihtiyat zorunlu);
aktif repo sahibinin adı repo URL'sinde zaten public olduğu için kalabilir.

Araç sürümleri, komutlar, çıkış kodları, süreler, dal/HEAD maskelenMEZ — kanıt onlardır.

## Biçim (bölüm sırası)

1. Başlık: aşama adı, UTC tarih, `dal@kısa-HEAD` + etiket, executor pini (model + uzantı).
2. SONUÇ tek cümle: OTOMATİK TAMAM / İNSAN KAPISI(açık) / BAŞARISIZ.
3. T süreleri varsa: epoch ms HAM + insan-okur karşılığı.
4. Kapı tablosu: satır | komut (maskeli) | beklenen | gerçekleşen | durum.
5. **Kritik alan çift-kayıt** (S3 genelgesi): lisans, sürüm/pin, çıkış kodu, damga/zaman,
   kimlik alanlarında "ham satır" ve "çıkarım" AYRI yazılır; kaynağı ULF-vade bulgusu
   (2026-08-15). Diğer satırlar kompakt tek satırdır — rapor şişmez.
6. Bekleyen iş / karar bekleyenler (numaralı; mimar kararı gelince durum güncellenir).
7. Yerinde düzeltmeler + şerhler.
8. BAŞARISIZ varsa: makinede bırakılan durum (ne kuruldu, ne yarım, temizlik komutu).

## BAŞARISIZ çerçevesi (S2 genelgesi)

- Kurulum/doğrulama YENİDEN DENEMESİ azami 3'tür; sonra insan kapısı (aşama dosyası başka
  eşik derse o kazanır).
- Teşhis/keşifte sayaç yok: "karar için yeterli kanıt"ta durulur — yeterlilik gerekçesi
  rapora yazılır. Erken durmak meşrudur (ör. resmî köprü aracında 2 denemede "kısıtlı ama
  kapalı değil → kapat" kararı, 2026-08-15 — doğru karardı).
- BAŞARISIZ'da okuma/teşhis SERBEST, DEĞİŞTİRME durur; karar insanın/mimarın (kural 22).

## Uzun koşu günlüğü (run-log — executor önerisi 5.4, v1.3.5 kabul)

Uzun koşularda append-only günlük: `docs/probe/runlog/<asama>.log` (yerel, gitignore'lu).
Her adım tek satır: `damga | komut | beklenen | gerçekleşen`. Bağlam özetlenirse hat bu
dosyadan sürer; özet mimar kopyasına taşınır, ham günlük makinede kalır.

## Aşama yetki genişlemesi — SONDA (2026-08-15 genelgesi)

Sonda koşusu boyunca executor'ün push kapsamı şunlarla genişler (dal/etiket/8-adım
protokolü aynen; maske taraması commit'lenen TÜM metinlerde 0 eşleşme şartıyla):
- `presets/unity-<pin>/` (ilk koşu preset çıkarımı + README), `docs/probe/kaynak/`,
  `docs/probe/scene-baseline.json`, `docs/probe/unity-pin.txt`
- Bu dizin (`docs/probe/raporlar/*.md`) sonda maskeli kopyasıyla: `YYYY-AA-GG-sonda.md`
- Önekler: rapor commit'i `rapor:`; artefakt commit'leri `sonda:` (mantıksal adım başına
  tek commit). Bunların DIŞINDA repo'ya yazmak YOK.
- `docs/probe/rapor.md` (report.py ürünü HAM rapor) repoya GİRMEZ — kimlik izlidir
  (lockfile yolunu içerir); gitignore'ludur, kopyası maskelenerek bu dizine girer.
