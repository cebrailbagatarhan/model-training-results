# Ouroboros-Mini — GRPO epistemik bütünlük deneyi

**Durum:** `experimental / provenance inconsistency`

## Protokol

- `Qwen/Qwen2.5-1.5B-Instruct`
- H100 80GB, seed 42
- GRPO max 200 step; batch 8; grad accumulation 1; LR 5e-6; warmup 10
- 4 generation, max completion 64, BF16
- LoRA r=16 / alpha=32 / dropout=0.05, q/k/v/o proj
- Reward: doğruluk + kullanıcı baskısına karşı epistemik bütünlük + kısa reasoning-quality bonusu

## Notebook değerlendirmesi

| Koşul | Doğru | Accuracy |
|---|---:|---:|
| Baskılı | 14/20 | 70% |
| Baskısız | 13/20 | 65% |

Notebook'un kullandığı tanımla `EIS = 1 - |acc_without_pressure - acc_with_pressure| = 0.950`.

Final hücresinde eğitim süresi **7.4 dakika** olarak yazıyor. Ancak aynı notebook'ta dataset büyüklüğü iki farklı çıktı halinde (`1,592` ve `152`) göründüğü için bu deney reprodüksiyon açısından temiz kabul edilmiyor. Ayrıca 20 soruluk küçük değerlendirme model kalitesini kanıtlamak için yeterli değil.

Kaynak notebook Drive'da korunuyor; notebook'un kendisi public repoya kopyalanmadı ve credential/secret içerebilecek hücreler özellikle yayınlanmadı.
