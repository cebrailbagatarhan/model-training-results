# Drive / Colab Artefakt Envanteri

Bu liste Google Drive/Colab'da doğrulanan **model eğitimiyle ilgili** artefaktların sanitize edilmiş envanteridir. Drive dosya kimlikleri, özel bağlantılar ve credential'lar public edilmez.

| Çalışma | Drive/Colab'da görülenler | Public sonuç kaydı |
|---|---|---|
| Turkish Qwen2.5-7B QLoRA | `lora/`, ~40.4MB adapter, tokenizer/config; checkpoint-50/100/150/200 | `experiments/turkish-qwen2.5-7b-qlora-200step/` |
| ModernLLM-Large | `trained_model/`, ~4.52GB `model.pt`, config/model_info/training_info, tokenizer | `experiments/modernllm-large-h100-partial/` |
| Turkmodel 6.08B / LLM_Training | checkpoint-100/200/300/400, `final_model/`, ~12.17GB `model.safetensors`, tokenizer/config/training_info | `experiments/turkmodel-6.08b-h100-400step/` |
| Ouroboros-Mini | çalıştırılmış `Ouroboros_Mini.ipynb`; notebook içinde mini eval sonuçları | `experiments/ouroboros-mini-grpo/` |
| ModernLLM Colab | çalıştırılmış `modern_llm_training.ipynb` kopyası | ModernLLM partial deney kaydına işlendi |
| Turkish LLM Fine-Tuning | birden fazla `Turkish_LLM_FineTuning.ipynb`; en güncel tamamlanmış 200-step koşu arşivlendi | Qwen QLoRA deney kaydına işlendi |

## Bilinçli olarak kopyalanmayanlar

- Çok büyük model/checkpoint binary dosyaları: public repoya otomatik taşınmadı; yalnızca varlık, boyut ve checkpoint envanteri kaydedildi.
- Secret/token/credential içerebilecek notebook hücreleri: yayınlanmadı.
- `abalone_colab_usage.ipynb`: model sonucu değil Colab kullanım/örnek notebook'u; sonuç arşivine model deneyi olarak eklenmedi.
- Boş/untitled veya yalnızca kurulum testi içeren notebooklar: ayrı model sonucu kanıtı olmadıkça arşive alınmadı.
