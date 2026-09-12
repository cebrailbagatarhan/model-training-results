# Bigg

Bu klasör Bigg model ailesinin deneysel sürümlerini ve karşılaştırma kayıtlarını toplar.

## Mevcut sürümler

### 50M baseline / JEPA off
- Yaklaşık 48.1M eğitilebilir parametre.
- Causal language modeling.
- JEPA auxiliary objective kapalı.
- Kontrollü 600 saniyelik pilotta en iyi sonuç.

### 50M legacy JEPA
- Aynı backbone + legacy JEPA auxiliary objective.
- Frozen/EMA teacher nedeniyle resident parametre ve compute maliyeti artıyor.
- 600 saniyelik pilotta throughput ve final test metriği baseline'ın gerisinde kaldı.

### 50M V4.1-Flash-inspired
- JEPA kaldırılmış deneysel yeni altyapı.
- Causal encoder–decoder yaklaşımı, compressed global KV, Engram-style n-gram memory, sparse MoE ve gated residual mixing fikirlerini Bigg ölçeğine uyarlıyor.
- Bu sürüm bir **adaptasyondur**, birebir DeepSeek implementasyonu değildir.
- Kontrollü benchmark henüz tamamlanmadı.

Ayrıntılı deney kayıtları için [`../../EXPERIMENT_INDEX.md`](../../EXPERIMENT_INDEX.md) dosyasına bakın.
