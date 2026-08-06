# AŞAMA -2 — ORTAM KURULUMU (tek seferlik; makine başına; sondadan ÖNCE)

Kullanıcı VS Code'daki Claude Code'a "başla" dediğinde fabrikanın İLK ADIMI budur:
kendi ortamını denetle, eksikse kur, kurduğunu iddia etme — KANITLA. Makine
değişirse yalnız bu dosya tekrar koşulur; 0A değil.

## Çalışma kuralları

- **İdempotent:** her adımın İLK işi doğrulama komutunu koşturmak; beklenen çıktı
  geliyorsa adım "kurulu (önceden)" işaretlenir ve atlanır. Kurulu araç yeniden
  kurulmaz.
- **Üç durumlu bitiş (her adım):**
  - **OTOMATİK TAMAM** — kurulum + doğrulama sessiz geçti.
  - **İNSAN ONAYI GEREKLİ** — executor durur ve TEK cümle söyler:
    `"{ARAÇ} için insan gerekli: {tam pencere/eylem tarifi}. Bitirince 'tamam' de."`
    Kullanıcı yapar, executor doğrulamayı tekrar koşturur. Bu durak "kurulum
    kapısı"dır; sonda T_uretim'ine GİRMEZ, ayrı sayılır. Tek cümle formatı zorunlu:
    hangi pencere, hangi buton, hangi hesap — belirsiz istek YASAK.
  - **BAŞARISIZ** — 3 otomatik denemede doğrulanamadı → insan kapısına döner;
    orada da çözülemezse hat DURUR, karar insandadır.
- **Kanıt disiplini:** "kurulu" iddiası yok. Her satır rapora komut + beklenen
  çıktı + gerçekleşen çıktı ile düşer.
- Başlangıç/bitiş `tools/probe/marker.py` ile `.markers/kurulum-start.ts` /
  `kurulum-end.ts` damgalanır (T_kurulum buradan hesaplanır).

## Araç tablosu (Windows)

| # | Araç | Kurulum yöntemi | Doğrulama komutu | Beklenen çıktı | Olası insan kapısı |
|---|---|---|---|---|---|
| 1 | winget (App Installer) | Genelde kurulu | `winget --version` | `v1.*` | Microsoft Store girişi |
| 2 | Git | `winget install --id Git.Git -e --silent` | `git --version` | `git version 2.*` | — |
| 3 | GitHub CLI | `winget install --id GitHub.cli -e --silent` | `gh --version`; `gh auth status` | `gh version 2.*`; "Logged in" | Tarayıcıda `gh auth login` |
| 4 | Python 3.12+ | `winget install --id Python.Python.3.12 -e --silent` | `python --version` | `Python 3.1*` | Yeni terminal (PATH) |
| 5 | Unity Hub | `winget install --id UnityTechnologies.UnityHub -e --silent` | Hub ikilisi var + `Unity Hub.exe -- --headless help` | yardım metni | Yükleyici UAC istemi |
| 6 | Unity 6000.3 LTS + Android modülü | Hub headless: `--headless install --version 6000.3.<pin> --changeset <cs> --module android` | `--headless editors --installed` | pinli sürüm + android modülü | Hub oturum/lisans ekranı |
| 7 | Unity Personal lisansı | Genelde Hub'dan otomatik; değilse Hub GUI | Boş projede `Unity.exe -batchmode -quit` çıkış kodu | `0` + lisans satırı (log) | Unity hesap oturumu (ilk sefer) |
| 8 | Resmî Unity MCP köprüsü | Unity'nin **güncel resmî dokümanındaki** adımlar (executor dokümanı okur, kullandığı her komutu rapora yazar); sahne-düzenleme araçları KAPALI | Editor açıkken köprü uç noktası canlı (dokümandaki kontrol yöntemi) | yanıt/handshake | Hesap/kabul ekranı varsa |
| 9 | VS Code + Claude Code | Kurulu varsayılır (bu oturum orada koşuyor) | `code --version` | sürüm satırı | — |

## Alanlar

**Girdi:** Windows 10/11; bu dosya; kullanıcının bir kerelik "tam yetkili kur" komutu.
**Çıktı:** `docs/probe/kurulum-raporu.md` — her araç: komut, beklenen, gerçekleşen,
durum (makine kimliği/hostname başlıkta); BAŞARISIZ satır yok.
**Yürüten:** otonom (işaretli insan kapıları hariç).
**Geçiş kriteri:** tablodaki 9 satırın tamamı "doğrulandı"; rapor dosyada.
**Geri kenarı:** üç durum yukarıda; kapı beklemesinin limiti yok ama her açık kapı
raporda "bekleyen iş" olarak durur — sessizce unutulamaz; BAŞARISIZ'da hat durur,
sonda kilitli kalır.
