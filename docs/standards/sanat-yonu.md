# SANAT YÖNÜ STANDARDI — paletin ve biçim dilinin karar süreci (Belge 2, v1.2)

**Kapattığı boşluk:** gorsel-sozlesme palete UYUMU ölçer; paletin NEREDEN geldiği bu
dosyadadır. Rotasyon havuzundaki "stil ailesi" bir isimdir, yön değil — yön bu süreçte
doğar. Onaylı paket sözleşmenin girdisidir: palette.json hex'leri + G5 manifest üçlüsü
(perspektif / çizgi kalınlığı bandı / gölge yönü) paketten ALINTILANIR — Aşama 2 kapı
bağı (`docs/stages/2.md`). B0/B8'in görsel karşılığıdır: sayı simülasyondan geliyorsa,
palet de sanat yönü kararından gelir.

**Kapsam (a): aile başına, oyun başına değil.** Ek A aile başına ≤2 canlı oyuna izin
verir; paket iki oyuna hizmet eder, insan maliyeti yarıya iner. Paket dosyası
`docs/standards/sanat-yonu/<aile>.md` — ikinci oyun onu yeniden kullanır, yeni tur koşmaz.

**Yürüten (c): İNSAN KAPISIDIR.** Süreç görsel üretebilen bir model oturumunda koşulur;
araç adı sabit değildir (Belge 2'deki "Claude Design" örnekti — v1.3'ten itibaren kullanıcı
↔ Arena oturumu): yönleri model üretir, seçim/hibrit/final onayı KULLANICININDIR (1.md
hasat hükmüyle aynı sahiplik disiplini). Muhasebe: insan-yuku.md §1 satırı; turlar 1-2
hibrit + 1 final; bekleme tavanı Ek C `insan_yanit_tavan_sanat_gun` (tur başına, taahhüt).

## Beş aşama — her aşama AYRI mesaj (ucuz turlar tekrarlanır; paket bir kez istenir)

1. **İhtiyaç tanımı:** konsept brifi Aşama 1 kartından türer — tür + temel mekanik
   (2-3 cümle, jargonsuz), platform + kitle, ruh hali kelimeleri, ilham alınan 2-3 eser
   ve HER BİRİNDEN alınan özellik (kopya değil), oyunun sahne/ekran listesi.
2. **Referans:** brif + isteğe bağlı 1-2 rakip ekran görüntüsü ("bu değil ama bu HİS" /
   "bu düzen"). Görsel hiç yoksa metin yine somuttur: hangi sahneler var, oyuncu her
   ekranda tam olarak ne görüyor.
3. **Çoklu-yön talebi (b — rotasyon kısıtı içinde):** birbirinden BELİRGİN farklı 3-4
   stil yönü, kategorik ayrışan (ör. sıcak el-yapımı / parlak kartunsu / minimal flat);
   tek yöne erken kilitlenme yok. Talep metnine defter + hesap-deseni envanterinin DOLU
   HÜCRELERİ girdi yazılır — aksi halde kullanıcı Ek A'nın yasakladığı yönü seçer ve
   kapı sonradan reddeder (A5.1 tek-doluluk). Korunacak kimlik unsurları açık yazılır
   (ör. ana özne silüeti tanınır kalsın). Her yön için ekran listesinin örnekleri istenir.
4. **Seçim / hibritleştirme (1-2 tur):** "A'nın menüsü + B'nin oynanışı" doğaldır —
   eşleştirme net yazılır, paletler çelişmez, geçiş ekranlarında kopukluk olmaz. Her
   turda yalnız değişen netleştirilir; önceki kararlar tekrar anlatılmaz.
5. **Final üretim paketi:** karar kesinleşince TEK kapsamlı talep — aşağıdaki tablonun
   tamamı eksiksiz istenir (teknik ekip tahmin yapmadan üretebilmeli).

## Paket içeriği (10 bölümün tamamı zorunlu)

| # | Bölüm | İçerik |
|---|---|---|
| 1 | Renk paleti | her rol için hex + kullanım oranları (roller gorsel-sozlesme G1'dedir) |
| 2 | Kontur kuralı | ölçülebilir kalınlık (ör. obje boyutunun %X'i), renk, URP 2D teknik karşılığı |
| 3 | Gölgeleme | basamak sayısı, parlaklık kuralı, teknik seçim — gölge yönü G5 üçlüsüne akar |
| 4 | Silüet/geometri | biçim dili kuralları: köşe yumuşatma oranı, abartı oranları, ölçek farkı |
| 5 | Doku/yüzey | stilize detay: çizgi sıklığı, kontrast, çözünürlük |
| 6 | Işıklandırma | yön/renk/gradyan hex'leri (2D'de gölgelendirici/gradyan karşılığı) |
| 7 | Obje/ekran tablosu | HER önemli nesne + UI elemanına satır: renk, kontur, özel not |
| 8 | Hibrit köprüsü | yönler birleştiyse nerede/nasıl buluştukları — net kural (Aşama 4 çıktısı) |
| 9 | URP 2D yol haritası | hangi shader/sprite materyali; mobil performans riskleri |
| 10 | Referans eserler | final yöne en yakın 3-5 eser + her birinden alınan somut özellik |

## Kurallar

- **Ölçülebilirlik şart:** pakette "güzel görünsün" yasak — hex, oran, basamak sayısı
  (gorsel-sozlesme ilkesinin aynısı: güzellik ölçülmez, uyum ölçülür).
- **Kapı bağı:** Aşama 2 kapanamaz — palette.json ve manifest üçlüsü onaylı paketten
  alıntı; aile için paket YOKSA veya ESKİYSE (yön kararı yenilendiyse) kapı KIRMIZI.
- **Paket ömrü:** aileye yeni yön kararı = paket yenileme turu (yalnız o zaman);
  değişim kayıtlıdır (Sözleşme-5 rapor disiplini). Paket kendi kaynağıdır — Ek C'ye
  GİRMEZ (Sözleşme-2'ye paralel tek-kaynak: paket `<aile>.md` dosyasıdır).
- **ALINMADI (kayıt, tekrar açılmaz):** Belge 2'nin "mevcut oyunun ekran görüntüleriyle
  teşhis" adımı — ilk oyunda mevcut görsel yoktur; sıfırdan senaryosu (konsept brifi)
  geçerlidir ve brif Aşama 1 kartından türer.
