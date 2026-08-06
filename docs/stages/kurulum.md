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
  çıktı + gerçekleşen çıktı ile düşer. Doğrulama ÇALIŞIR HALİ ölçer: dosya/liste
  çıktısı tek başına kanıt değildir, araç gerçekten koşturulur (Unity'de gate =
  batchmode çıkış kodu 0; listeleme yalnız ara kanıttır).
- **Yarım kurulum kalamaz:** doğrulama çalışır hali ölçtüğü için yarım kurulum
  bir sonraki koşuda "kurulu" sayılamaz. BAŞARISIZ'da rapora **"makinede bırakılan
  durum"** bölümü eklenir: ne kuruldu, ne yarım kaldı, temizlik gerekiyorsa hangi
  komutla.
- **Kapı ön-bildirimi:** koşunun ilk işi, beklenen TÜM insan kapılarını tek mesajda
  saymak (kesin: ≥2 UAC onayı; koşullu: hesap oturumları). Sürpriz kapı YOK.
- **Bekleme disiplini:** ≥2 dk sürebilecek iş tek bloklayıcı komutla koşulmaz
  (terminal zaman aşımı): desen = başlat → 60 sn'de bir durumu yokla → azami süre
  aşımında İNSAN KAPISI. Unity Hub'ın headless install'ı ASENKRON döner; "kurulu"
  kararı yalnız yoklama döngüsünün sonundaki doğrulamayla verilir.
- **İki durum:** proje ya EDITOR OTURUMU'ndadır (MCP canlı, batchmode YASAK) ya
  başsız (Editor kapalı, batchmode koşar). Eşzamanlılık yok; bekçi
  `Temp/UnityLockfile`. Editor'ü açan/kapatan executor'dır (komut, insan değil).
- Başlangıç/bitiş `tools/probe/marker.py` ile `.markers/kurulum-start.ts` /
  `kurulum-end.ts` damgalanır (T_kurulum buradan hesaplanır).

## Yetki sınırı ("tam yetkili kur" SADECE bunu kapsar)

- **İZİN VERİLEN:** tablodaki 9 satırın kurulumu ve doğrulanması; pin dosyası ve
  geçici doğrulama projeleri dahil yalnız **fabrika dizini altında** dosya/klasör
  oluşturmak.
- **YASAK (insan onayı olmadan, her koşulda):** tabloda olmayan yazılım kurmak;
  herhangi bir yazılımı kaldırmak veya sürüm düşürmek; sistem ortam değişkenlerini
  kalıcı değiştirmek (yükleyicinin kendi yaptığı hariç); Defender / güvenlik
  yazılımı ayarına dokunmak; yükleyicinin kendi yazdığı dışında kayıt defteri
  düzenlemek; fabrika dizini dışında dosya silmek ya da değiştirmek; kullanıcının
  mevcut Unity projelerine ve mevcut oyununun kaynağına erişmek.
- **Tabloda olmayan bir araç gerekirse:** kurulMAZ. İnsan kapısı açılır, öneri
  rapora düşülür; tabloya ancak insan ekler.
- **GitHub yetkisi scope'ları:** `gh auth login` yalnız `repo, workflow`; mümkünse
  bu repoyla sınırlı fine-grained token. Tam hesap yetkisi (org/admin silme vb.
  scope'lar) istenmez; varsayılan hiçbir koşulda tam yetki değildir.

## Araç tablosu (Windows)

| # | Araç | Kurulum yöntemi | Doğrulama komutu | Beklenen çıktı | Olası insan kapısı |
|---|---|---|---|---|---|
| 1 | winget (App Installer) | Genelde kurulu | `winget --version` | `v1.*` | Microsoft Store girişi |
| 2 | Git | `winget install --id Git.Git -e --silent` | `git --version` | `git version 2.*` | — |
| 3 | GitHub CLI | `winget install --id GitHub.cli -e --silent` | `gh --version`; `gh auth status` | `gh version 2.*`; "Logged in" | Tarayıcıda `gh auth login` (scope: Yetki sınırı) |
| 4 | Python 3.12+ | `winget install --id Python.Python.3.12 -e --silent` | `py -3.12 --version`; yoksa `%LOCALAPPDATA%\Programs\Python\Python312\python.exe --version` | `Python 3.12.*` | İkisi de yok → insan. NOT: `python` komutu Windows'ta Microsoft Store stub'ına gidebilir; doğrulamada KULLANILMAZ |
| 5 | Unity Hub | `winget install --id UnityTechnologies.UnityHub -e --silent` | Hub ikilisi var + `Unity Hub.exe -- --headless help` | yardım metni | UAC onayı KESİN (yükleyici yönetici ister) |
| 6 | Unity LTS pini | Unity'nin resmî sürüm arşivinden güncel 6000.3 yaması + changeset okunur; `docs/probe/unity-pin.txt`'e `6000.3.xfN — <changeset>` olarak yazılır. **Dosya varsa sayfaya tekrar GİDİLMEZ** (tek seferlik kilit) | pin dosyası okunur (satır 7 bu değerle kurar) | dosya mevcut + format doğru | Ağ erişimi yoksa pini insan girer |
| 7 | Unity 6000.3 LTS + Android modülü + Personal lisans | Hub headless: `--headless install --version <pin> --changeset <cs> --module android` (pin satır 6'dan) — **asenkron döner**: 60 sn'de bir yokla, azami 90 dk (10–15 GB iner); lisans genelde Hub oturumundan akar, akmazsa Hub GUI | ARA KANIT: `--headless editors --installed` çıktısında pinli sürüm + android modülü. GATE: fabrika dizini altında geçici boş projede `Unity.exe -batchmode -quit -logFile -` (proje silinmez — satır 8 de kullanır) | gate çıkış kodu **0** + lisans satırı (log) | Hub oturumu/UAC; Unity hesap oturumu (ilk sefer) |
| 8 | Resmî Unity MCP köprüsü | Unity'nin **güncel resmî dokümanındaki** adımlar (executor dokümanı okur, her komutu rapora yazar); sahne-düzenleme araçları KAPALI yapılandırılır; **Editor'ü executor başlatır** — satır 7'nin geçici projesinde deklare edilmiş EDITOR OTURUMU (insan kapısı DEĞİL, komut) | Editor açıkken köprü uç noktası canlı + araç listesi sorgusu (dokümandaki yöntem); sonra Editor kapatılır, `Temp/UnityLockfile`'ın kaybolduğu doğrulanır, geçici proje silinir | handshake + **araç listesinde sahne-düzenleme araçları kapalı/yok** (liste çıktısı rapora) + kilit-kayboldu kanıtı | Hesap/kabul ekranı varsa |
| 9 | VS Code + Claude Code | Kurulu varsayılır (bu oturum orada koşuyor) | `code --version` | sürüm satırı | — |

## Alanlar

**Girdi:** Windows 10/11; bu dosya; kullanıcının bir kerelik "tam yetkili kur"
komutu + UAC onayları için makine başında durması (kesin kapılar ön-bildirilir).
**Çıktı:** `docs/probe/kurulum-raporu.md` — her satır: komut, beklenen, gerçekleşen,
durum. Başlıkta makine kimliği = hostname + Windows sürümü + mimari
(`PROCESSOR_ARCHITECTURE`). BAŞARISIZ satır yok; varsa "makinede bırakılan durum".
**Yürüten:** otonom (işaretli insan kapıları hariç).
**Geçiş kriteri:** tablodaki 9 satırın tamamı "doğrulandı" (satır 7'nin gate'i
batchmode çıkış kodu 0); rapor dosyada.
**Geri kenarı:** üç durum yukarıda; kapı beklemesinin limiti yok ama her açık kapı
raporda "bekleyen iş" olarak durur — sessizce unutulamaz; BAŞARISIZ'da hat durur,
sonda kilitli kalır.
