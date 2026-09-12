# Turkish Qwen2.5-7B — 200-step QLoRA/SFT

**Durum:** `completed training / no held-out evaluation`

## Protokol

- Base: `Qwen/Qwen2.5-7B-Instruct`
- Dataset: `malhajar/alpaca-gpt4-tr`, 52,002 örnek, ChatML formatı
- QLoRA: 4-bit NF4 + BF16 compute
- LoRA: r=8, alpha=16, dropout=0.05
- Batch 1, gradient accumulation 8
- Max sequence length 1,024
- Max steps 200, warmup 10
- LR 2e-4, cosine scheduler
- Optimizer `paged_adamw_8bit`
- Weight decay 0.01, seed 42

## Sonuç

| Metrik | Değer |
|---|---:|
| Notebook ortalama training loss | 0.9459 |
| Runtime | 9,042 s (~2s 30d 42s) |
| Final global step | 200 |
| Final logged loss (step 200) | 0.836867 |
| Final logged mean token accuracy | 0.781749 |
| Trainer'da görülen token sayacı | 318,805 |
| Held-out eval | Yok |

Training loss ve token accuracy yalnızca eğitim akışına aittir; model kalitesi veya genelleme iddiası için held-out değerlendirme gerekir.

Drive'da checkpoint-50/100/150/200 ve final LoRA adapter bulundu. Ağırlık dosyaları public repoya kopyalanmadı.
