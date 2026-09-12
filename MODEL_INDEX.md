# Model Index

| Model | Sürüm/ölçek | Durum | Sonuç / artefakt | Kaynak |
|---|---|---|---|---|
| Bigg | 50M baseline / JEPA off | completed | Test NLL **5.607873**, PPL **272.563981** | [GitHub](https://github.com/cebrailbagatarhan/bigg) |
| Bigg | 50M legacy JEPA | completed | Test NLL 5.837443, PPL 342.901316 | [GitHub](https://github.com/cebrailbagatarhan/bigg) |
| Bigg | 50M V4.1-Flash-inspired | pending benchmark | Kontrollü sonuç henüz yok | [GitHub](https://github.com/cebrailbagatarhan/bigg) |
| [Turkish Qwen2.5 QLoRA](models/turkish-qwen2.5-7b-qlora/) | 7B base / 20.2M trainable | completed training, no eval | Train loss 0.9459; adapter Drive'da | [Drive/Colab](https://drive.google.com/drive/folders/1VQmfjLOYuUbEpMFXD2vUQjEnnfYoqGRm) · [GitHub kodu](https://github.com/cebrailbagatarhan/yapay-zeka-sistemi) |
| [ModernLLM-Large](models/modernllm-large/) | 1.129B | partial | Kısmi H100 koşuları; model artefaktı Drive'da | [Drive](https://drive.google.com/drive/folders/1p5Qb6y53WBHlpR0qN5R6phcJpg6-RM0c) · [GitHub](https://github.com/cebrailbagatarhan/yapay-zeka-sistemi) |
| [Ouroboros-Mini](models/ouroboros-mini/) | Qwen2.5 1.5B base | experimental | Mini eval EIS 0.950; notebook provenance tutarsız | [Colab](https://colab.research.google.com/drive/1n8sVpfzwGwNgH_dAG4dlf8cyB6jzrdAk) |
| [Turkmodel TR-EN](models/turkmodel-6.08b/) | 6.083B | short PoC | 400 step, train loss 4.78736; final ağırlık Drive'da | [Drive](https://drive.google.com/drive/folders/164kK-Jk7hR5AkC2bSeJbJtqkH1CPZFA7) · [GitHub](https://github.com/cebrailbagatarhan/turkmodel) |
| [nanochat Windows CPU](models/nanochat-windows-cpu/) | 17M/61M/92M presetler | self-reported | Medium README sonucu 5.79 → 2.37 loss | [GitHub](https://github.com/cebrailbagatarhan/nanochat-windows-cpu) |
| [Car Evaluation ML](models/car-evaluation-ml/) | 7 klasik model | completed | En iyi test accuracy: Decision Tree %98.55 | [GitHub](https://github.com/cebrailbagatarhan/car-evaluation-ml) |
| [Turkish BPE Tokenizer](models/turkish-tokenizer-128k/) | 128k vocab | trained tokenizer | ~150k Wikipedia makalesi; benchmark yok | [GitHub](https://github.com/cebrailbagatarhan/TurkishTokenizer) |

## Kayıt kuralı

Bu sonuç deposuna model ağırlıkları/checkpoint binary'leri kopyalanmaz. Burada yalnızca deney özeti, doğrulanmış metrikler ve asıl model/notebook/checkpoint kaynağına bağlantı tutulur. Drive bağlantıları erişim izinlerini değiştirmez; özel dosyalar özel kalır.
