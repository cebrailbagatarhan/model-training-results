# Model Eğitimleri, Deneyler ve Sonuçlar

Bu depo; farklı model sürümlerinin, eğitim deneylerinin, kullanılan veri/ortam bilgilerinin ve ölçülen sonuçların tek yerde, karşılaştırılabilir biçimde tutulması için oluşturulmuştur.

> Amaç: yalnızca en iyi sonucu göstermek değil; **hangi model + hangi veri + hangi ayar + hangi donanım ile hangi sonucun alındığını** açıkça kaydetmek.

## İlk kayıt: Bigg 50M — JEPA legacy vs off

Eşit **600 saniyelik wall-clock bütçesinde**, seed `42` ile yapılan pilotta JEPA kapalı sürüm (`off`) daha iyi sonuç verdi.

| Mod | Süre (s) | Step | Eğitim tokenı | Token/s | Test NLL ↓ | Test PPL ↓ | Peak VRAM (GB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| off | 600.23 | 1258 | 5,152,768 | 8,584.66 | **5.607873** | **272.563981** | **1.470829** |
| legacy JEPA | 600.04 | 968 | 3,964,928 | 6,607.76 | 5.837443 | 342.901316 | 1.679554 |

Özet: `off`, aynı sürede yaklaşık **%30 daha fazla token** işledi; test NLL ve perplexity de daha iyi çıktı. Legacy JEPA erken token bütçesinde kısa süreli sample-efficiency avantajı gösterse de bu avantaj eğitim ilerledikçe kayboldu.

Ayrıntılar: [`experiments/bigg-50m-jepa-vs-off/`](experiments/bigg-50m-jepa-vs-off/)

## Depo düzeni

- [`MODEL_INDEX.md`](MODEL_INDEX.md) — kayıtlı modeller ve sürümler
- [`EXPERIMENT_INDEX.md`](EXPERIMENT_INDEX.md) — deney listesi ve durumları
- [`models/`](models/) — model/sürüm kartları
- [`experiments/`](experiments/) — deney konfigürasyonları, ham sonuçlar ve analizler
- [`benchmarks/`](benchmarks/) — modeller arası karşılaştırma tabloları
- [`datasets/`](datasets/) — kullanılan veri kaynaklarının/splitlerin kaydı
- [`environments/`](environments/) — GPU, CUDA, PyTorch ve çalışma ortamı notları
- [`methodology/`](methodology/) — değerlendirme ve tekrarlanabilirlik kuralları
- [`templates/`](templates/) — yeni deney eklemek için şablonlar

## Yayın ilkeleri

1. Sonuçlar, mümkün olduğunda ham `CSV/JSON` ile birlikte yayınlanır.
2. Aynı deney ailesindeki modeller için veri, seed ve bütçe sabit tutulur.
3. Wall-clock ve token-budget karşılaştırmaları birbirinden ayrılır.
4. Tek-seed sonuçlar "kesin üstünlük" olarak sunulmaz.
5. Henüz çalıştırılmamış mimariler sonuç gibi gösterilmez; `planned`/`pending` olarak işaretlenir.

## Lisans / kaynak kod

Bu depo ağırlıklı olarak **deney sonuçları ve metodoloji** içindir. Model kaynak kodu ayrı geliştirme depolarında tutulabilir. Buradaki sayılar, ilgili deney kayıtlarında belirtilen koşullar için geçerlidir.
