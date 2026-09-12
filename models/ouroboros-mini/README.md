# Ouroboros-Mini

**Durum:** `experimental / notebook-only evidence`

Qwen2.5-1.5B-Instruct tabanında, epistemik bütünlük ve kullanıcı baskısına direnç fikrini GRPO ile denemek için hazırlanmış Colab çalışması.

## Kullanılanlar

- Base: `Qwen/Qwen2.5-1.5B-Instruct` (~1.54B)
- GPU: NVIDIA H100 80GB HBM3
- Seed: 42
- GRPO: 200 step, batch 8, LR 5e-6, BF16
- LoRA: r=16, alpha=32, dropout=0.05; q/k/v/o proj
- 4 generation/örnek, max completion 64
- Reward ağırlıkları: accuracy 1.0, epistemic-integrity 0.8, reasoning-quality 0.4

Notebook çıktılarında veri sayısı konusunda tutarsızlık var: veri oluşturma çıktısı **1,592 örnek (%37 baskılı)** derken final özet hücresi **152 örnek** yazıyor. Bu nedenle deney temiz bir yeniden çalıştırma yapılana kadar kesin/reprodüksiyon-ready sayılmıyor.

Ayrıntılar: [`../../experiments/ouroboros-mini-grpo/`](../../experiments/ouroboros-mini-grpo/)
