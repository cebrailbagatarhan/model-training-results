# Reproducibility Checklist

Her `completed` deney için mümkün olduğunca aşağıdakiler kaydedilir:

- model ailesi ve sürümü
- kaynak commit SHA / release
- parametre ölçeği
- tokenizer ve vocab boyutu
- dataset kaynağı ve train/validation/test splitleri
- seed(ler)
- sequence length
- batch / micro-batch / accumulation
- optimizer ve learning-rate schedule
- precision modu
- training budget (seconds/steps/tokens)
- GPU ve VRAM
- Python / PyTorch / CUDA sürümleri
- final validation/test metrikleri
- throughput ve memory
- ham sonuç dosyaları (`CSV`/`JSON`)
- başarısız veya protokol dışı koşular için hata notu

## Dosya standardı

Önerilen deney klasörü:

```text
experiments/<experiment-name>/
├── README.md
├── config.yaml
├── results.csv
├── results.json
├── validation_history.csv
├── provenance.md
└── figures/
```

Dosya adları makine tarafından okunabilir tutulur; açıklamalar `README.md` içinde insan-okunabilir biçimde verilir.
