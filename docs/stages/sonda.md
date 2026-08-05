# AŞAMA -1 — SONDA (tek seferlik; 0A'dan ÖNCE)

**Girdi:** Unity kurulu Windows makine + VS Code Claude Code. Hesap, para, CI YOK.
**Çıktı:** Sözleşme-2 kurallarıyla (bootstrap-only, JSON veri, MCP yalnız gözlemci)
üretilmiş oynanabilir gri kutu döngü + ölçüm raporu: toplam süre, insan müdahalesi
sayısı, Editor'e elle dokunma sayısı, engel listesi. Ek B'nin Aşama-4 satırı BU
ölçümle yazılır (tahmin değil).
**Yürüten:** karma — üretim otonom; insan gözlemci, müdahaleleri sayar.
**Geçiş kriteri:** döngü çökmeden oynandı VE rapor `docs/appendix/B.md` içine
işlendi.
**Geri kenarı:** üretim sağlanamazsa 0A'ya GİRİLMEZ; engel listesiyle Sözleşme-2
(bootstrap-only) ve/veya motor kararı yeniden açılır. Max 2 deneme; ikinci de
başarısızsa karar tamamen insana + fabrikaya.
