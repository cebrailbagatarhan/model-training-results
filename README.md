# Model Eğitimleri, Deneyler ve Sonuçlar

Bu depo; farklı model sürümlerinin, Colab/Drive eğitim artefaktlarının, GitHub deneylerinin, kullanılan veri/ortam bilgilerinin ve ölçülen sonuçların tek yerde karşılaştırılabilir biçimde tutulması için oluşturulmuştur.

> Amaç: yalnızca en iyi sonucu göstermek değil; **hangi model + hangi veri + hangi ayar + hangi donanım ile hangi sonucun alındığını** ve sonucun ne kadar güvenilir olduğunu açıkça kaydetmek.

## Envanter özeti

| Model/çalışma | Durum | Öne çıkan kayıt |
|---|---|---|
| Bigg 50M JEPA-off vs legacy | completed | JEPA-off: test NLL 5.607873, PPL 272.56 |
| Bigg V4.1-Flash-inspired | pending | JEPA kaldırıldı; kontrollü benchmark henüz yok |
| Turkish Qwen2.5-7B QLoRA | training completed / no eval | 200 step, train loss 0.9459; adapter Drive'da |
| ModernLLM-Large 1.129B | partial | Kısmi H100 koşuları; ~4.52GB model artefaktı Drive'da |
| Ouroboros-Mini | experimental | Mini eval EIS 0.950; notebook veri sayısı tutarsız |
| Turkmodel TR-EN 6.083B | short PoC | 400 step, train loss 4.78736; ~12.17GB final weights Drive'da |
| nanochat Windows CPU | self-reported | Medium: loss 5.79 → 2.37; ham log doğrulaması yok |
| Car Evaluation ML | completed | Decision Tree test accuracy %98.55 |
| Turkish BPE Tokenizer | trained tokenizer | 128k vocab, ~150k Türkçe Wikipedia makalesi |

Tam liste: [`MODEL_INDEX.md`](MODEL_INDEX.md) · Deneyler: [`EXPERIMENT_INDEX.md`](EXPERIMENT_INDEX.md) · Drive/Colab envanteri: [`DRIVE_ARTIFACT_INDEX.md`](DRIVE_ARTIFACT_INDEX.md) · Makine-okunur envanter: [`benchmarks/model_inventory.csv`](benchmarks/model_inventory.csv)

## Bigg 50M — JEPA legacy vs off

Eşit **600 saniyelik wall-clock bütçesinde**, seed `42` ile yapılan pilotta JEPA kapalı sürüm (`off`) daha iyi sonuç verdi.

| Mod | Süre (s) | Step | Eğitim tokenı | Token/s | Test NLL ↓ | Test PPL ↓ | Peak VRAM (GB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| off | 600.23 | 1258 | 5,152,768 | 8,584.66 | **5.607873** | **272.563981** | **1.470829** |
| legacy JEPA | 600.04 | 968 | 3,964,928 | 6,607.76 | 5.837443 | 342.901316 | 1.679554 |

`off`, aynı sürede yaklaşık %30 daha fazla token işledi; test NLL ve perplexity de daha iyi çıktı. Ayrıntılar: [`experiments/bigg-50m-jepa-vs-off/`](experiments/bigg-50m-jepa-vs-off/)

## Drive/Colab artefakt politikası

Drive'da doğrulanan büyük checkpoint/model dosyalarının varlığı, boyutu ve koşuyla ilişkisi kaydedilir; çok büyük binary ağırlıklar bu GitHub sonuç deposuna otomatik kopyalanmaz. Public repoya yalnızca güvenli config/metric/provenance bilgisi alınır. Credential, erişim anahtarı ve secret içeren notebook hücreleri yayınlanmaz.

## Depo düzeni

- [`MODEL_INDEX.md`](MODEL_INDEX.md) — kayıtlı modeller ve sürümler
- [`EXPERIMENT_INDEX.md`](EXPERIMENT_INDEX.md) — deney listesi ve durumları
- [`DRIVE_ARTIFACT_INDEX.md`](DRIVE_ARTIFACT_INDEX.md) — sanitize edilmiş Drive/Colab artefakt envanteri
- [`models/`](models/) — model/sürüm kartları
- [`experiments/`](experiments/) — deney konfigürasyonları, ham/özet sonuçlar ve analizler
- [`benchmarks/`](benchmarks/) — karşılaştırma ve envanter tabloları
- [`datasets/`](datasets/) — kullanılan veri kaynaklarının/splitlerin kaydı
- [`environments/`](environments/) — GPU, CUDA, PyTorch ve çalışma ortamı notları
- [`methodology/`](methodology/) — değerlendirme ve tekrarlanabilirlik kuralları
- [`templates/`](templates/) — yeni deney eklemek için şablonlar

## Yayın ilkeleri

1. Sonuçlar mümkün olduğunda ham `CSV/JSON` ile birlikte yayınlanır.
2. Training loss ile held-out eval metrikleri açıkça ayrılır.
3. Aynı deney ailesindeki veri, seed ve bütçe farkları belirtilir.
4. Wall-clock ve token-budget karşılaştırmaları birbirinden ayrılır.
5. Tek-seed/küçük eval sonuçları kesin üstünlük olarak sunulmaz.
6. Kesintili, OOM olmuş veya provenance sorunu olan koşular `partial/experimental` olarak tutulur.
7. Henüz çalıştırılmamış mimariler sonuç gibi gösterilmez; `planned/pending` olarak işaretlenir.

## Lisans / kaynak kod

Bu depo ağırlıklı olarak **deney sonuçları ve metodoloji** içindir. Model kaynak kodu ayrı geliştirme depolarında tutulabilir. Buradaki sayılar yalnızca ilgili deney kayıtlarında belirtilen koşullar için geçerlidir.
