# Turkmodel 6.08B — H100 400-step PoC

**Durum:** `completed short training / weights preserved / no held-out eval`

## Kaydedilmiş sonuç

| Metrik | Değer |
|---|---:|
| Parametre | 6,082,670,592 |
| GPU | 1× NVIDIA H100 80GB HBM3 |
| Step | 400 |
| İşlenen token | 13,107,200 |
| Eğitim süresi | 66.0183 dk |
| GPU-saat | ~1.1003 |
| Final training loss | 4.78736 |
| Training perplexity (türetilmiş) | ~119.98 |
| Ortalama throughput (türetilmiş) | ~3,309 tok/s |
| Held-out eval | Yok |

Yaklaşık **0.00215 token/parametre** görüldüğü için bu, 6B ölçekli modelin kalite eğitimi değil kısa bir altyapı/öğrenme PoC'sidir. Final training loss held-out kalite metriği olarak yorumlanmamalıdır.

## Artefakt doğrulaması

GitHub'daki `training_info.json` ile Drive'daki final `training_info.json` aynı temel sonucu kaydediyor. Drive'da checkpoint-100/200/300/400 ile yaklaşık **12.17 GB** final `model.safetensors` bulunuyor. Binary ağırlık public sonuç reposuna taşınmadı.

Kaynak veri: `cebrailbagatarhan/turkmodel/results/training_info.json` + özel Drive artefakt envanteri.
