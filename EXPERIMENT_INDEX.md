# Experiment Index

| Deney | Model | Bütçe | Seed | Durum | Ana sonuç |
|---|---|---|---:|---|---|
| [`bigg-50m-jepa-vs-off`](experiments/bigg-50m-jepa-vs-off/) | Bigg 50M | 600 s / mod | 42 | completed | JEPA off, eşit wall-clock'ta daha iyi NLL/PPL ve throughput verdi |
| [`bigg-50m-v41-flash`](experiments/bigg-50m-v41-flash/) | Bigg 50M V4.1-Flash-inspired | plan: 600 s | 42 | pending | JEPA-off baseline'a karşı kontrollü kıyas yapılacak |

## Durum etiketleri

- `planned`: protokol yazıldı, çalışma başlamadı.
- `running`: eğitim/değerlendirme sürüyor.
- `completed`: ham sonuçlar ve değerlendirme mevcut.
- `invalid`: protokol ihlali veya teknik hata nedeniyle karşılaştırmaya dahil edilmiyor.
