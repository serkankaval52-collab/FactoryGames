# MODEL-KLİŞE DEFTERİ — modelin kendi çekim merkezleri (M2)

**Güvenilirlik etiketi:** ilk içerik dış kaynaklıdır — paralel motorun ~10–12
koşuluk (boş seed testleri) gözlemi; sistematik loglama YOK, sayım kaydı YOK,
DÜŞÜK GÜVEN — motorun kendi ifadesiyle "sıfırıncı sürüm, elle bakımlı".
Tahminle klişe yazılmaz — yeni satır gözlem ister.

**ÖNEMLİ ŞERH:** bu liste BAŞKA BİR MODELİN çekim merkezlerinin gözlemidir,
bizimkilerin değil. İki model aynı aileden olsa da örüntüler birebir aynı
olmayabilir. Dolayısıyla bu satırlar iki riski birden taşır: (a) bizde hiç
görünmeyen bir şeyi yasaklıyor olabiliriz (gereksiz daralma), (b) bizim asıl
tekrarımızı hiç kapsamıyor olabilir (yanlış güven). İlk üç kendi koşumuzdan
sonra: her satır "bizde de gözlendi / gözlenmedi" diye işaretlenir; gözlenmeyen
silinmez ama "(dış gözlem, bizde doğrulanmadı)" etiketine iner ve süzgeçte
ZAYIF AĞIRLIK taşır (eleme yapmaz; seçim çıktısında işaretlenir).

**BANT KURALI (kelime yetmez):** bu liste tek tek kelimeleri değil bir örüntüyü
gösteriyor: dokuz maddenin dokuzu da aynı bantta — sakin, hüzünlü, poetik,
yalnız bir figür, kaybolmuş bir dünya. Yani asıl klişe kelimeler değil, O BANT.
Süzgeç kelime eşleşmesiyle çalışırsa model bandı korur, kelimeyi değiştirir
("fener bekçisi" yerine "deniz feneri kayıtçısı") ve süzgeci atlar. Kural:
eleme kelime eşleşmesine EK olarak bant kontrolü yapar — konsept "yalnız figür +
kaybolmuş/solmuş dünya + hüzünlü sakinlik" üçlüsünü taşıyorsa, kelimeleri farklı
olsa da defter ihlali sayılır. Bu ihlal ikili değil yargı içerir; o yüzden kapı
değil, kartta ZORUNLU BEYANDIR: her konsept kartı "bu konsept şu banda giriyor
mu, neden değil" sorusunu yanıtlar (1.md çıktısı). Yargı gizlenmez; açık yargı,
sayısal görünen yargıdan iyidir.

**İşlev:** Aşama 1 havuz kontrolü (M5): `havuz.json`'a yazılan her değer bu
defterle çaprazlanır; defterdeki hiçbir şey havuza değer olarak girmez. Kura
script'i (tools/kura.py) kelime süzgecini mekanik uygular: güçlü satırlar eler;
zayıf-ağırlık satırları elemez, çıktıda işaretlenir. Bant kontrolü ise script'in
değil kartın işidir (yargıdır).

**Kapsam notu (paralel motor mutabakatı):** duygu/atmosfer ekseni havuzda YOK —
model bu eksende kendi çekim merkezine düşüyor (paralel gözlem: üretilen 6
temanın 5'i modelin kendi yasak listesindeydi). Tür ekseni dış kaynaklıdır
(mağaza kategorileri). Özgünlük çarpımdan gelir: doymuş tür × alışılmadık kısıt.

## Klişeler

- küller / küle dönen dünya — tekrar eden açılış imgesi (paralel motor gözlemi)
- arşivci / anı toplayan — tekrar eden rol arketipi (paralel motor gözlemi)
- fener bekçisi / ışık taşıyan — tekrar eden rol arketipi (paralel motor gözlemi)
- tohum bahçıvanı / bitki büyüten — tekrar eden mekanik-tema eşlemesi (paralel motor gözlemi)
- sisli köy / kaybolan kasaba — tekrar eden mekân (paralel motor gözlemi)
- mektup madencisi — tekrar eden rol arketipi (paralel motor gözlemi)
- gölge mimarı — tekrar eden rol arketipi (paralel motor gözlemi)
- zaman döngüsü (jenerik) — tekrar eden meta yapı (paralel motor gözlemi)
- kayıp ruhlar — tekrar eden tema (paralel motor gözlemi)

## Kendi koşularımız

> Boş. Format: `- <ad> — gözlem (koşu no, kanıt: kart/rapor yolu)`. Kaynak
> karışmaz: kendi gözlemlerimiz yalnız bu bölümde birikir; ilk üç koşu sonrası
> yukarıdaki dış satırlar buradaki bulguyla işaretlenir.
