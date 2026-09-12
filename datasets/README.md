# Datasets

Bu klasör eğitim verisinin kendisini değil, deneylerde kullanılan veri kaynaklarını ve split/ölçek bilgilerini kaydeder. Ham dataset, lisans ve dağıtım hakkı doğrulanmadan bu public repoya eklenmez.

## Bigg 50M JEPA pilot

- Dil: Türkçe
- Gerçek doküman sayısı: 12,000
- Tokenizer: deney belgelerinden öğrenilen 16K byte-level BPE
- Token splitleri: train 6,000,000 / validation 150,000 / test 150,000

## Turkish Qwen2.5-7B QLoRA

- Dataset: `malhajar/alpaca-gpt4-tr`
- Kayıtlı örnek sayısı: 52,002
- Format: instruction/input/output örnekleri ChatML konuşma formatına çevrilmiş
- Held-out değerlendirme split'i kaydedilmedi; bu nedenle training loss model kalitesi olarak kullanılmıyor

## ModernLLM-Large

Drive metadata'sında 57 pretrain metni, 31 SFT konuşması ve 133 CoT örneği kaydedilmiş. Kaynak GitHub reposunda da 133 CoT örneğinin dağılımı belgelenmiş. Bazı deneylerde train/eval aynı corpus üzerinden bağımsız seçildiğinden overlap riski bulunuyor.

## Ouroboros-Mini

Notebook sentetik true/false + kullanıcı baskısı koşullu veri üretiyor. Aynı notebook çıktısında toplam veri sayısı hem 1,592 hem 152 olarak göründüğü için dataset büyüklüğü doğrulanmış sayılmıyor; temiz rerun gerekli.

## Turkmodel 6.08B

Kaydedilmiş public sonuçta toplam işlenen token 13,107,200. Dataset manifesti ve bağımsız held-out eval sonucu sonuç dosyasında yer almıyor; bu koşu kısa PoC olarak sınıflandırılıyor.

## Car Evaluation ML

- UCI Car Evaluation
- 1,728 örnek
- 6 kategorik özellik, 4 sınıf
- %80/%20 train-test split + 5-fold CV

## Turkish BPE Tokenizer 128k

- Kaynak: Hugging Face `wikimedia/wikipedia`, `20231101.tr`
- Yaklaşık 150,000 Türkçe makale
- Eğitim amacı: 128,000 vocab Byte-Level BPE

Bir deneyde veri kaynağı/split değişirse sonuçların aynı benchmark satırında doğrudan karşılaştırılmaması gerekir.
