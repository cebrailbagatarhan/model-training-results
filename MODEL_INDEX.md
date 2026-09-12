# Model Index

| Model | Sürüm/ölçek | Durum | Ana fikir | Sonuç / artefakt |
|---|---|---|---|---|
| Bigg | 50M baseline / JEPA off | completed | Causal LM, JEPA kapalı | Test NLL **5.607873**, PPL **272.563981** |
| Bigg | 50M legacy JEPA | completed | Causal LM + legacy JEPA auxiliary objective | Test NLL 5.837443, PPL 342.901316 |
| Bigg | 50M V4.1-Flash-inspired | pending benchmark | JEPA kaldırılmış CED/Engram-style altyapı | Kontrollü sonuç henüz yok |
| [Turkish Qwen2.5 QLoRA](models/turkish-qwen2.5-7b-qlora/) | 7B base / 20.2M trainable | completed training, no eval | 4-bit QLoRA + Türkçe Alpaca SFT | Train loss 0.9459; final adapter Drive'da |
| [ModernLLM-Large](models/modernllm-large/) | 1.129B | partial | Özel decoder-only GQA/SwiGLU LM | Kısmi H100 koşuları; 4.52GB model artefaktı Drive'da |
| [Ouroboros-Mini](models/ouroboros-mini/) | Qwen2.5 1.5B base | experimental | GRPO + epistemik-bütünlük reward | Mini eval EIS 0.950; notebook provenance tutarsız |
| [Turkmodel TR-EN](models/turkmodel-6.08b/) | 6.083B | short PoC | Llama-style dense causal LM | 400 step, train loss 4.78736; 12.17GB final ağırlık Drive'da |
| [nanochat Windows CPU](models/nanochat-windows-cpu/) | 17M/61M/92M presetler | self-reported | CPU uyarlaması | Medium README sonucu 5.79 → 2.37 loss |
| [Car Evaluation ML](models/car-evaluation-ml/) | 7 klasik model | completed | UCI Car Evaluation sınıflandırma | En iyi test accuracy: Decision Tree %98.55 |
| [Turkish BPE Tokenizer](models/turkish-tokenizer-128k/) | 128k vocab | trained tokenizer | Türkçe Byte-Level BPE | ~150k Wikipedia makalesi; benchmark yok |

## Kayıt kuralı

Her model sürümünde mümkün olduğunca parametre ölçeği, mimari farklar, tokenizer, veri, seed, optimizer, eğitim bütçesi, donanım, yazılım ortamı, değerlendirme metrikleri ve ilgili deney klasörü tutulur. Drive'da bulunan büyük binary ağırlıklar public repoya otomatik kopyalanmaz; varlık/boyut/checkpoint envanteri kayda geçirilir.
