# Eğitim Ortamları

Bu dosya yalnızca kaynak kayıtlarda doğrulanabilen donanım bilgilerini özetler.

| Deney | Donanım | Kayıtlı not |
|---|---|---|
| Bigg 50M JEPA pilot | Google Colab NVIDIA T4 | 600 s eşit wall-clock kıyas; peak allocated VRAM ayrıca sonuçlarda |
| Turkish Qwen2.5-7B QLoRA | Colab sınıfı ~16GB GPU | Notebook'ta model/LoRA bellek kullanımı yaklaşık 5.2/7.3GB; kesin GPU modeli sonuç kaydında ayrıca sabitlenmemiş |
| ModernLLM-Large | NVIDIA H100 ~80GB | Drive metadata'sında ~79.18GB görünür bellek |
| Ouroboros-Mini | NVIDIA H100 80GB HBM3 | Notebook çıktısında GPU ve 85.0GB decimal VRAM görünümü |
| Turkmodel 6.08B | 1× NVIDIA H100 80GB HBM3 | 400-step kısa koşu |
| nanochat Windows CPU | 12 CPU core, 15.7GB RAM | Kaynak README'de yerel sistem olarak raporlanmış |

Yazılım sürümü kaydedilmemiş bir deney için sürüm tahmin edilmez. Yeni koşularda Python, PyTorch, CUDA, driver, Transformers/TRL/PEFT sürümleri ve GPU modeli açıkça kaydedilmelidir.
