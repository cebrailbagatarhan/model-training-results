# Bigg 50M — JEPA legacy vs off

**Durum:** completed  
**Tarih:** 2026-09-12  
**Seed:** 42  
**Karşılaştırma bütçesi:** her mod için yaklaşık 600 saniye wall-clock

## Soru

Legacy JEPA auxiliary objective, aynı wall-clock bütçesinde 50M ölçekli Bigg language-model eğitimini iyileştiriyor mu?

## Protokol

- Model ölçeği: yaklaşık 50M.
- Modlar: `off` ve `legacy`.
- Seed: `42`.
- Bütçe: `time`, yaklaşık `600 s` / mod.
- Sequence length: `256`.
- Vocabulary: `16,384` byte-level BPE.
- Veri: gerçek Türkçe dokümanlar; hazırlanmış token splitleri `train=6,000,000`, `validation=150,000`, `test=150,000`.
- Değerlendirme: held-out Türkçe validation/test NLL ve perplexity.
- Ek ölçümler: training tokens, token/s ve peak allocated GPU memory.

## Final sonuçlar

| Metrik | JEPA off | Legacy JEPA | Daha iyi |
|---|---:|---:|---|
| Eğitim süresi (s) | 600.229693 | 600.040766 | eşit bütçe |
| Step | **1258** | 968 | off |
| Eğitim tokenı | **5,152,768** | 3,964,928 | off |
| Token/s | **8,584.660271** | 6,607.764377 | off |
| Final validation NLL ↓ | **5.6797** | 5.8932 | off |
| Final validation PPL ↓ | **292.87** | 362.56 | off |
| Test NLL ↓ | **5.607873** | 5.837443 | off |
| Test PPL ↓ | **272.563981** | 342.901316 | off |
| Peak allocated GB ↓ | **1.470829** | 1.679554 | off |

## Eğri yorumu

Legacy JEPA, eğitimin erken bölümünde **aynı token sayısında** daha düşük validation NLL gösterebildi. Örneğin 204,800 tokenda `8.4567` (legacy) vs `8.6893` (off); 1,024,000 tokenda `6.8122` vs `6.8712`.

Bu fark ilerleyen eğitimde kapandı. Yaklaşık 2.0–2.5M token civarında iki eğri birbirine yaklaştı ve sonrasında `off` öne geçti. Wall-clock açısından legacy koşu ayrıca daha yavaş olduğu için 600 saniyede belirgin biçimde daha az token gördü.

## Sonuç

Bu tek-seed, kısa pilotta **legacy JEPA kullanılmaması** daha iyi sonuç verdi. Sonuç, "JEPA genel olarak işe yaramaz" iddiası değildir; yalnızca test edilen legacy objective + teacher maliyetinin bu koşullarda faydayı karşılamadığını gösterir.

Takip deneyi: [`../bigg-50m-v41-flash/`](../bigg-50m-v41-flash/)
