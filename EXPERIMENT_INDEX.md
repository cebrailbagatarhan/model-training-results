# Experiment Index

| Deney | Model | Bütçe | Seed | Durum | Ana sonuç |
|---|---|---|---:|---|---|
| [`qwen3.8-27b-t4-quantization`](experiments/qwen3.8-27b-t4-quantization/) | Qwen3.8-27B | Colab T4 / 16 GB VRAM | — | planned | 4-bit NF4 ve daha düşük-bit varyantlarla T4 deployment sınırı ölçülecek |
| [`bigg-50m-jepa-vs-off`](experiments/bigg-50m-jepa-vs-off/) | Bigg 50M | 600 s / mod | 42 | completed | JEPA off, eşit wall-clock'ta daha iyi NLL/PPL ve throughput verdi |
| [`bigg-50m-v41-flash`](experiments/bigg-50m-v41-flash/) | Bigg 50M V4.1-Flash-inspired | plan: 600 s | 42 | pending | JEPA-off baseline'a karşı kontrollü kıyas yapılacak |
| [`turkish-qwen2.5-7b-qlora-200step`](experiments/turkish-qwen2.5-7b-qlora-200step/) | Qwen2.5-7B-Instruct | 200 step / 9,042 s | 42 | completed training / no eval | Ortalama train loss 0.9459; final adapter Drive'da |
| [`modernllm-large-h100-partial`](experiments/modernllm-large-h100-partial/) | ModernLLM 1.129B | çeşitli/kesintili H100 koşuları | — | partial | Final geçerli benchmark yok; ara metrikler + model artefaktı arşivlendi |
| [`ouroboros-mini-grpo`](experiments/ouroboros-mini-grpo/) | Qwen2.5-1.5B + GRPO | 200 step | 42 | experimental | Baskılı 70%, baskısız 65%, EIS 0.950; dataset-size çıktısı tutarsız |
| [`turkmodel-6.08b-h100-400step`](experiments/turkmodel-6.08b-h100-400step/) | Turkmodel 6.083B | 400 step / 66.0 dk | — | short PoC | Train loss 4.78736; held-out eval yok; final weights Drive'da |
| [`nanochat-windows-cpu`](experiments/nanochat-windows-cpu/) | nanochat CPU presetleri | 30 sn–dakikalar | — | self-reported | Medium README loss 5.79 → 2.37; ham log doğrulaması yok |
| [`car-evaluation-7-models`](experiments/car-evaluation-7-models/) | 7 klasik ML modeli | 80/20 + 5-fold CV | — | completed | Decision Tree test accuracy %98.55 ile en yüksek |

## Durum etiketleri

- `planned/pending`: protokol var, sonuç yok.
- `completed`: kaydedilmiş koşu/metrik mevcut.
- `completed training / no eval`: eğitim tamamlanmış ama held-out değerlendirme yok.
- `partial`: kesintili/başarısız aşamalar nedeniyle final benchmark sayılamaz.
- `experimental`: küçük veya provenance sorunu olan çalışma; temiz tekrar gerekli.
- `self-reported`: kaynak README'de sonuç var, ham log ile ayrıca doğrulanmamış.
- `invalid`: protokol ihlali veya teknik hata nedeniyle karşılaştırmaya dahil edilmez.
