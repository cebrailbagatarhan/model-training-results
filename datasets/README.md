# Datasets

Bu klasör eğitim verisinin kendisini değil, deneylerde kullanılan veri kaynaklarını ve split bilgilerini kaydeder.

## Bigg 50M JEPA pilot

- Dil: Türkçe.
- Gerçek doküman sayısı: 12,000.
- Tokenizer: eğitim belgelerinden öğrenilen 16K byte-level BPE.
- Hazırlanmış token splitleri:
  - train: 6,000,000 token
  - validation: 150,000 token
  - test: 150,000 token

Bir deneyde veri kaynağı/split değişirse, sonuçların aynı benchmark satırında doğrudan karşılaştırılmaması gerekir.

> Veri lisansı ve dağıtım hakkı ayrıca doğrulanmadan ham dataset bu depoya eklenmez.
