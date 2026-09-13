# RUN 001 — Qwen3.8-27B / bitsandbytes NF4 / Colab T4

## Sonuç özeti

İlk gerçek Colab koşusunda `Qwen/Qwen3.8-27B`, `bitsandbytes` 4-bit NF4 ile tek NVIDIA T4 üzerinde **inference aşamasına ulaşamadı**.

`device_map="auto"` modelin bazı modüllerini CPU veya diske dispatch etmeye çalıştı ve model yükleme aşaması `ValueError` ile durdu. Bu nedenle bu koşuda tokens/s, TTFT, context ve çıktı kalitesi ölçülemedi.

Bu koşu, **4-bit NF4 + doğrudan/otomatik device placement konfigürasyonunun 14.56 GiB görünen T4 VRAM'i için yeterli headroom bırakmadığını** gösteren negatif bir deployment sonucu olarak kaydedildi.

## Ortam

| Alan | Değer |
|---|---|
| GPU | Tesla T4 |
| Colab tarafından görülen VRAM | 14.56 GiB |
| PyTorch | 2.11.0+cu128 |
| Transformers | 5.17.0 |
| bitsandbytes | 0.50.2 |
| Model | `Qwen/Qwen3.8-27B` |
| Quantization | 4-bit NF4 |
| Compute dtype | FP16 |
| Double quant | enabled |
| Device map | `auto` |

## Teorik ağırlık belleği

Notebook'taki 28B parametre varsayımıyla:

| Hassasiyet | Yalnızca ağırlıklar |
|---|---:|
| FP16 | ~52.15 GiB |
| INT8 | ~26.08 GiB |
| 4-bit | ~13.04 GiB |
| 3.5-bit | ~11.41 GiB |
| 3-bit | ~9.78 GiB |

T4'te görülen 14.56 GiB VRAM ile 4-bit ideal ağırlık alt sınırı arasındaki teorik fark yalnızca **~1.52 GiB**. Bu alan; quantization metadata'sı, quantize edilmeyen katmanlar, multimodal bileşenler, CUDA çalışma alanı ve daha sonra inference sırasında KV cache gibi ek maliyetler için çok sınırlı.

> Bu 1.52 GiB değeri teorik ağırlık hesabı ile görülen toplam VRAM'in farkıdır; gerçek çalışma sırasında kullanılabilir serbest VRAM olarak yorumlanmamalıdır.

## Çalıştırılan quantization ayarı

```python
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForMultimodalLM.from_pretrained(
    MODEL_ID,
    quantization_config=bnb_config,
    device_map="auto",
    low_cpu_mem_usage=True,
)
```

## İndirme / yükleme gözlemi

Colab çıktısında:

- `Download complete`: **47.7 GB**
- `Reconstruction complete`: **55.6 GB / 55.6 GB**
- `Fetching 18 files`: **30:34**

Bu süre yalnızca logda görülen fetch/download aşamasıdır; Python tarafındaki `load_seconds` değişkeni model yükleme exception ile kesildiği için final model-load süresi olarak kaydedilemedi.

## Hata

Ana hata:

```text
MODEL YÜKLENEMEDİ:
ValueError('Some modules are dispatched on the CPU or the disk. ...')
```

Yani `device_map="auto"`, modelin tamamını seçilen konfigürasyonla GPU üzerinde tutamadı ve bazı modülleri CPU/disk tarafına yerleştirmeye yöneldi. Yükleme bu noktada tamamlanmadı.

Sonraki hücrede görülen:

```text
NameError: name 'model' is not defined
```

ayrı bir temel problem değildir. İlk `from_pretrained(...)` çağrısı tamamlanmadığı için `model` değişkeni hiç oluşturulmamıştır; memory-footprint hücresi bu yüzden zincirleme hata vermiştir.

## Ölçülebilen / ölçülemeyen metrikler

| Metrik | Sonuç |
|---|---|
| GPU | Tesla T4 |
| Görülen VRAM | 14.56 GiB |
| NF4 model load | başarısız |
| CPU/disk dispatch | tetiklendi |
| Inference | başlamadı |
| Peak inference VRAM | ölçülemedi |
| TTFT | ölçülemedi |
| tokens/s | ölçülemedi |
| Maksimum context | ölçülemedi |
| Kalite değerlendirmesi | yapılamadı |

## Teknik yorum

Bu koşu **"Qwen3.8-27B hiçbir şekilde T4'te çalışmaz"** sonucunu kanıtlamaz. Kanıtladığı daha dar sonuç şudur:

> Mevcut `bitsandbytes` NF4 + FP16 compute + double quant + `device_map="auto"` konfigürasyonu, Colab'ın 14.56 GiB görünen tek T4 GPU'sunda modeli tamamen yükleyip inference'a geçemedi.

Sonraki deneyler için daha düşük-bit GGUF/IQ quantization, açık CPU offload veya daha düşük bellekli deployment yolu ayrı koşular olarak test edilmelidir.

## Durum

`partial` — yükleme testi gerçek çıktı üretti ancak inference benchmarkına ulaşılamadı.
