# Qwen3.8-27B — Colab T4 Quantization

## Durum

`partial`

İlk gerçek Colab koşusu tamamlandı: `bitsandbytes` 4-bit NF4 konfigürasyonu Tesla T4 üzerinde model yükleme aşamasını geçemedi. `device_map="auto"` bazı modülleri CPU/disk tarafına dispatch etmeye çalıştı ve yükleme `ValueError` ile durdu. Bu nedenle ilk koşuda inference benchmarkı üretilemedi.

Detaylı koşu kaydı: [`RUN_001_NF4_T4.md`](RUN_001_NF4_T4.md)

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

## Donanım ve ilk koşu ortamı

- Google Colab
- GPU: Tesla T4
- Colab'ın raporladığı VRAM: **14.56 GiB**
- PyTorch: **2.11.0+cu128**
- Transformers: **5.17.0**
- bitsandbytes: **0.50.2**

## İlk koşuda elde edilen sonuç

Notebook'taki 28B parametre varsayımıyla 4-bit ağırlıkların ideal alt sınırı yaklaşık **13.04 GiB**. Colab'ın raporladığı 14.56 GiB toplam VRAM ile aradaki teorik fark yalnızca **~1.52 GiB**. Bu fark gerçek kullanılabilir serbest VRAM değildir; quantization metadata'sı, quantize edilmeyen katmanlar, multimodal bileşenler ve CUDA çalışma alanı gibi maliyetler de belleğe eklenir.

İlk yükleme denemesinde model dosyaları indirildi ve logda şu değerler görüldü:

- Download complete: **47.7 GB**
- Reconstruction complete: **55.6 GB / 55.6 GB**
- Fetching 18 files: **30:34**

Ardından model yükleme şu hata ile durdu:

```text
MODEL YÜKLENEMEDİ:
ValueError('Some modules are dispatched on the CPU or the disk. ...')
```

Bu sonuç, `bitsandbytes` NF4 + FP16 compute + double quant + `device_map="auto"` konfigürasyonunun bu T4 oturumunda modeli tamamen yükleyip inference'a geçemediğini gösterir.

Sonraki `NameError: name 'model' is not defined` mesajı ayrı bir kök neden değildir; ilk `from_pretrained(...)` çağrısı tamamlanmadığı için `model` değişkeni oluşturulmamıştır.

### İlk koşuda ölçülebilenler

| Metrik | Sonuç |
|---|---|
| GPU | Tesla T4 |
| Toplam görülen VRAM | 14.56 GiB |
| Teorik 4-bit ağırlık alt sınırı | ~13.04 GiB |
| NF4 model load | başarısız |
| CPU/disk dispatch | tetiklendi |
| Inference | başlamadı |
| Peak inference VRAM | ölçülemedi |
| TTFT | ölçülemedi |
| tokens/s | ölçülemedi |
| Maksimum context | ölçülemedi |
| Kalite değerlendirmesi | yapılamadı |

## Deney planı

1. FP16/BF16 tam model için teorik bellek baseline'ı kaydedilecek. ✅
2. `bitsandbytes` ile 4-bit NF4 yükleme denenecek. ✅ İlk koşu: yükleme başarısız / CPU-disk dispatch.
3. Açık CPU offload veya alternatif placement ayrı deney olarak test edilecek.
4. T4'e uygun daha düşük-bit GGUF/IQ varyantları ayrı koşular olarak test edilecek.
5. Başarılı yükleme elde edildiğinde aynı prompt seti ile hız ve kalite karşılaştırılacak.

## Ölçülecek metrikler

| Metrik | Açıklama |
|---|---|
| Peak VRAM | `torch.cuda.max_memory_allocated()` ile GB |
| Load time | Model yükleme süresi |
| TTFT | İlk token gecikmesi |
| Generation time | Toplam üretim süresi |
| Throughput | tokens/s |
| Context | Başarılı maksimum context uzunluğu |
| Çalışma durumu | Başarılı / OOM / load failure |
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

## Sonuç tablosu

| Yöntem | Bit | Peak VRAM | Yükleme gözlemi | tokens/s | Context | Durum | Kalite notu |
|---|---:|---:|---|---:|---:|---|---|
| FP16/BF16 baseline | 16 | ~52.15 GiB yalnızca ağırlık | teorik | — | — | T4'e sığmaz | Referans |
| bitsandbytes NF4 | 4 | inference peak ölçülemedi | 55.6 GB reconstruction; 18 dosya fetch 30:34 | — | — | **load failure** | inference başlamadı |
| 4-bit + explicit offload | 4 | TBD | TBD | TBD | TBD | pending | TBD |
| daha düşük-bit GGUF/IQ | <4 | TBD | TBD | TBD | TBD | pending | TBD |

## Teknik yorum

Bu ilk koşu, "Qwen3.8-27B hiçbir şekilde T4'te çalışmaz" sonucunu kanıtlamaz. Elde edilen daha dar ve tekrarlanabilir sonuç şudur:

> `bitsandbytes` 4-bit NF4 + FP16 compute + double quant + `device_map="auto"` konfigürasyonu, Colab'ın 14.56 GiB görünen tek Tesla T4 GPU'sunda modeli tamamen yükleyip inference'a geçemedi.

Dolayısıyla sonraki adım, aynı model için daha düşük-bit deployment veya açık offload yaklaşımını ayrı deney olarak test etmektir.

## Kaynaklar

- Drive klasörü: https://drive.google.com/drive/folders/1B5IhcOTTa20ZY6O9n8rzRtTm61Q2YYXC
- Proje planı: https://docs.google.com/document/d/1IbLzw2SGat6hmI5AwV_BVEOEC8piAdA-vFjssGfvur0/edit
- Qwen3.8-27B model kartı: https://huggingface.co/Qwen/Qwen3.8-27B

## Not

Ders şartı modelin bizzat quantize edilmesini gerektiriyorsa, 27B model yalnızca deployment/benchmark hedefi olarak kullanılmamalıdır. Aynı quantization pipeline'ı daha küçük bir Qwen modelinde gerçekten uygulanıp doğrulanabilir; 27B model ise T4 üzerindeki deployment sınırını göstermek için kullanılabilir.
