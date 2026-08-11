# MODEL-KLİŞE DEFTERİ — modelin kendi çekim merkezleri (M2)

**Güvenilirlik etiketi:** bu dosyanın ilk içeriği dış kaynaklıdır — paralel
motorun ~10 koşuluk gözlemi; sistematik loglama yok, DÜŞÜK GÜVEN. İlk üç kendi
koşumuzdan sonra gözden geçirilir; kendi bulgularımız (koşu no + kanıt) üste
yazılır. Tahminle klişe yazılmaz — yeni satır gözlem ister.

**İşlev:** Aşama 1 havuz kontrolü (M5): `havuz.json`'a yazılan her değer bu
defterle çaprazlanır; defterdeki hiçbir şey havuza değer olarak girmez. Kura
script'i (tools/kura.py) süzgeci mekanik uygular; bölüm boşsa süzgeç boş geçer
ve bu durum çıktıya kaydedilir.

**Kapsam notu (paralel motor mutabakatı):** duygu/atmosfer ekseni havuzda YOK —
model bu eksende kendi çekim merkezine düşüyor (paralel gözlem: üretilen 6
temanın 5'i modelin kendi yasak listesindeydi). Tür ekseni dış kaynaklıdır
(mağaza kategorileri). Özgünlük çarpımdan gelir: doymuş tür × alışılmadık kısıt.

## Klişeler

> Sıfırıncı sürüm bekleniyor: paralel motorun gözlem listesi buraya `- <ad> —
> not (kaynak: paralel motor)` satırlarıyla işlenecek. Dolana dek kura çıktıları
> "defter: boş" işareti taşır; bu, hatayı değil kayıt durumunu gösterir.

## Kendi bulgularımız (ilk üç koşudan sonra dolar)

> Boş. Format: `- <ad> — gözlem (koşu no, kanıt: kart/rapor yolu)`.
