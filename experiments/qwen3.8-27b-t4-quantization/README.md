# Qwen3.8-27B — Colab T4 Quantization

## Durum

`planned`

Bu deneyin amacı, yaklaşık 28B parametreli `Qwen/Qwen3.8-27B` modelini düşük-bit quantization ile 16 GB NVIDIA T4 üzerinde çalıştırmanın sınırlarını ölçmektir.

## Notebook

- Colab notebook: `Qwen3_8_27B_T4_Quantization_Colab.ipynb`
- Colab'da doğrudan aç: https://colab.research.google.com/github/cebrailbagatarhan/model-training-results/blob/main/experiments/qwen3.8-27b-t4-quantization/Qwen3_8_27B_T4_Quantization_Colab.ipynb
- Drive kopyası: https://drive.google.com/file/d/1xEuTVwC_xn6EPF5H0fl1aK3EfezGHf2T/view

## Araştırma sorusu

FP16 ağırlıkları teorik olarak yaklaşık 56 GB bellek gerektiren Qwen3.8-27B, 4-bit veya daha düşük quantization ile Colab T4 üzerinde kullanılabilir mi? Kullanılabiliyorsa bellek, hız ve çıktı kalitesi açısından en iyi denge hangi ayarda elde edilir?

## Model

- Model: `Qwen/Qwen3.8-27B`
- Tür: image-text-to-text / multimodal
- Resmî Transformers yükleme sınıfı: `AutoModelForMultimodalLM`
- Model kartı: https://huggingface.co/Qwen/Qwen3.8-27B

## Donanım

- Google Colab
- NVIDIA T4
- 16 GB VRAM

## Deney planı

1. FP16/BF16 tam model için teorik bellek baseline'ı kaydedilecek.
2. `bitsandbytes` ile 4-bit NF4 yükleme denenecek.
3. 4-bit yükleme OOM verirse daha kısa context ve CPU offload ile tekrar test edilecek.
4. Gerekirse T4'e uygun daha düşük-bit (yaklaşık 3–3.5 bit) varyant ile inference testi yapılacak.
5. Her başarılı koşuda aynı prompt seti ile hız ve kalite karşılaştırılacak.

## Ölçülecek metrikler

| Metrik | Açıklama |
|---|---|
| Peak VRAM | `torch.cuda.max_memory_allocated()` ile GB |
| Load time | Model yükleme süresi |
| TTFT | İlk token gecikmesi |
| Generation time | Toplam üretim süresi |
| Throughput | tokens/s |
| Context | Başarılı maksimum context uzunluğu |
| Çalışma durumu | Başarılı / OOM |
| Kalite | Sabit prompt setinde nitel karşılaştırma |

## 4-bit başlangıç konfigürasyonu

```python
from transformers import AutoProcessor, AutoModelForMultimodalLM, BitsAndBytesConfig
import torch

MODEL_ID = "Qwen/Qwen3.8-27B"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

processor = AutoProcessor.from_pretrained(MODEL_ID)
model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
    low_cpu_mem_usage=True,
)
```

## Teknik risk

28B parametre için 4-bit ağırlıkların teorik alt sınırı yaklaşık 14 GB'dır. Quantization metadata'sı, quantize edilmeyen katmanlar, multimodal bileşenler, CUDA çalışma alanı ve KV cache ek VRAM tüketir. Bu nedenle 16 GB T4 üzerinde 4-bit yükleme garanti değildir. OOM sonucu başarısızlık değil, deneyin ölçtüğü donanım sınırının bir parçasıdır.

## Sonuç tablosu

| Yöntem | Bit | Peak VRAM | Load time | tokens/s | Context | Durum | Kalite notu |
|---|---:|---:|---:|---:|---:|---|---|
| FP16/BF16 baseline | 16 | ~56 GB teorik | — | — | — | T4'e sığmaz | Referans |
| bitsandbytes NF4 | 4 | TBD | TBD | TBD | TBD | pending | TBD |
| 4-bit + offload | 4 | TBD | TBD | TBD | TBD | pending | TBD |
| düşük-bit alternatif | ~3–3.5 | TBD | TBD | TBD | TBD | pending | TBD |

## Kaynaklar

- Drive klasörü: https://drive.google.com/drive/folders/1B5IhcOTTa20ZY6O9n8rzRtTm61Q2YYXC
- Proje planı: https://docs.google.com/document/d/1IbLzw2SGat6hmI5AwV_BVEOEC8piAdA-vFjssGfvur0/edit
- Qwen3.8-27B model kartı: https://huggingface.co/Qwen/Qwen3.8-27B

## Not

Ders şartı modelin bizzat quantize edilmesini gerektiriyorsa, 27B model yalnızca deployment/benchmark hedefi olarak kullanılmamalıdır. Aynı quantization pipeline'ı daha küçük bir Qwen modelinde gerçekten uygulanıp doğrulanabilir; 27B model ise T4 üzerindeki deployment sınırını göstermek için kullanılabilir.
