# Bigg 50M — V4.1-Flash-inspired follow-up

**Durum:** pending benchmark

Bu deney, JEPA legacy pilotundan sonra hazırlanan JEPA'sız yeni Bigg altyapısını, en iyi mevcut kontrollü baseline olan `JEPA off` ile karşılaştırmak için ayrılmıştır.

## Planlanan karşılaştırma

- Model ölçeği: 50M sınıfı.
- Seed: `42` ile ilk run; ardından mümkünse `42, 43, 44`.
- İlk bütçe: `600 s` wall-clock.
- Aynı tokenizer/veri splitleri kullanılacak.
- Raporlanacak metrikler: validation NLL/PPL, test NLL/PPL, token/s, peak VRAM, training tokens.
- İkinci aşama: eşit training-token bütçesi ile tekrar.

## Yeni altyapıda test edilen fikirler

- JEPA ve EMA teacher kaldırılmıştır.
- Causal encoder–decoder (CED) tarzı ayrıştırma.
- Decoder tarafında compressed global KV.
- Engram-style hashed n-gram memory.
- Sparse MoE.
- Hafif gated residual mixing.

Bu tasarım **V4.1-Flash-inspired bir Bigg adaptasyonudur**; başka bir modelin birebir/ölçek-eşdeğer implementasyonu olduğu iddia edilmez.

## Geçilmesi gereken baseline

Önceki `JEPA off` sonucu:

- test NLL: **5.607873**
- test perplexity: **272.563981**
- throughput: **8,584.660271 tok/s**
- peak allocated memory: **1.470829 GB**

Yeni sonuçlar geldikçe bu klasöre ham `CSV/JSON`, config ve analiz eklenecektir.
