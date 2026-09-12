# ModernLLM-Large

**Durum:** `partial / artifact-preserved`

Özel PyTorch decoder-only Transformer deneyi. Kaynak çalışma `cebrailbagatarhan/yapay-zeka-sistemi` deposunda; ayrıca Google Drive'da model artefaktları korunuyor.

## Mimari

| Alan | Değer |
|---|---:|
| Parametre | 1,129,416,704 |
| Hidden size | 2,048 |
| Katman | 24 |
| Attention head | 32 |
| KV head | 8 |
| Intermediate | 5,504 |
| Maks. context | 4,096 |
| Mimari | Decoder-only causal LM |
| Özellikler | RMSNorm, RoPE, GQA, SwiGLU, SDPA/attention, KV cache, CoT veri aşaması |

## Artefakt durumu

Drive'da `trained_model` altında yaklaşık **4.52 GB `model.pt`**, model/config JSON'ları, tokenizer ve training metadata bulundu. Bu büyük ağırlık dosyası bu public sonuç deposuna kopyalanmadı.

Drive metadata'sı `pretrain`, `sft`, `cot` aşamalarını kaydediyor; ancak commit edilmiş notebook günlüklerinde kesintiler, OOM ve tamamlanmamış koşular bulunduğu için bu modeli **tamamlanmış/validasyonu yapılmış final model** olarak etiketlemiyoruz.

Ayrıntılı deney kaydı: [`../../experiments/modernllm-large-h100-partial/`](../../experiments/modernllm-large-h100-partial/)
