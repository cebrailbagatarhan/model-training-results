# Benchmarks

Bu klasör farklı deneylerden gelen sonuçları tek tabloda toplar.

Ana dosya: [`summary.csv`](summary.csv)

## Karşılaştırma kuralları

- `wall_clock`: aynı gerçek eğitim süresi.
- `training_tokens`: aynı işlenmiş token sayısı.
- Seed sayısı farklı deneyler doğrudan "kesin üstünlük" şeklinde yorumlanmaz.
- `pending` satırlar henüz ölçülmemiştir ve sıralamaya dahil edilmez.
- NLL/perplexity için düşük; token/s için yüksek değer daha iyidir.

## Çevrimdışı model envanterini sıralama

`benchmarks/model_inventory.csv` içindeki kayıtları değiştirmeden arama sonuçlarını
model adı, aile veya durum alanına göre sıralayabilirsiniz:

```bash
python -m benchmarks.inventory --sort-by model
python -m benchmarks.inventory --status completed --sort-by status --descending --json
```

Sıralama büyük/küçük harf duyarsızdır; eşit değerlerde CSV sırası korunur.
`--descending` yalnızca `--sort-by` ile kullanılabilir. Varsayılan çıktı sırası değişmez.
