# Google Colab / T4 profile

Bigg 50M pilot notebook'u Google Colab üzerinde NVIDIA T4 sınıfı çalışma için hazırlanmıştır.

## Pilot ayarları

- Sequence length: 256
- Micro batch: 4
- Gradient accumulation: 4
- Mixed-precision/FP32-kritik operasyon politikası: notebook implementasyonuna bağlı
- Karşılaştırma bütçesi: mod başına 600 saniye ölçülen training time

## Tekrarlanabilirlik notu

Yeni run'larda aşağıdakiler çıktı olarak saklanmalıdır:

```text
GPU model
VRAM
Python version
PyTorch version
CUDA version
cuDNN version
precision mode
torch / CUDA deterministic settings
```

Mevcut public sonuçlar performans metriklerini (`token/s`, peak allocated GB) içerir; sonraki deneylerde tam environment manifest'i de kaydedilecektir.
