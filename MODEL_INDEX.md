# Model Index

| Model | Sürüm | Durum | Ana fikir | Sonuç |
|---|---|---|---|---|
| Bigg | 50M baseline / JEPA off | completed | Causal LM + mevcut Bigg backbone, JEPA kapalı | Test NLL **5.607873**, PPL **272.563981** |
| Bigg | 50M legacy JEPA | completed | Causal LM + legacy JEPA auxiliary objective | Test NLL 5.837443, PPL 342.901316 |
| Bigg | 50M V4.1-Flash-inspired | pending benchmark | JEPA kaldırılmış CED/Engram-style deneysel altyapı | Henüz kontrollü eğitim sonucu yok |

## Kayıt kuralı

Her model sürümünde en az şu bilgiler tutulur: parametre ölçeği, mimari farklar, tokenizer, veri, seed, optimizer, eğitim bütçesi, donanım, yazılım ortamı, değerlendirme metrikleri ve ilgili deney klasörü.
