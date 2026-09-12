# Benchmarks

Bu klasör farklı deneylerden gelen sonuçları tek tabloda toplar.

Ana dosya: [`summary.csv`](summary.csv)

## Karşılaştırma kuralları

- `wall_clock`: aynı gerçek eğitim süresi.
- `training_tokens`: aynı işlenmiş token sayısı.
- Seed sayısı farklı deneyler doğrudan "kesin üstünlük" şeklinde yorumlanmaz.
- `pending` satırlar henüz ölçülmemiştir ve sıralamaya dahil edilmez.
- NLL/perplexity için düşük; token/s için yüksek değer daha iyidir.
