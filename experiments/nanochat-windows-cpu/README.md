# nanochat Windows CPU — yerel sonuçlar

**Durum:** `self-reported / needs reproducible logs`

README'de belirtilen yerel sistem: **12 CPU çekirdeği, 15.7 GB RAM**.

| Koşu | Süre | Parametre | Loss |
|---|---:|---:|---|
| Quick test | 30 sn | belirtilmemiş | 11.09 → 3.32 |
| Fast | ~10 dk | ~17M | final loss ayrıca kaydedilmemiş |
| Medium | README'de 1.2 dk | ~61M | 5.79 → 2.37 |
| Max | — | ~92M | test ediliyor |

Bu değerler kaynak repo README'sinden alınmıştır; ayrı ham training log/report ile bağımsız doğrulama yapılmadığı için benchmark tablosuna `verified` olarak sokulmamalıdır. README içinde görülen CORE/ARC/GSM8K/MMLU tablosu upstream nanochat örneğine aittir ve bu CPU koşularının sonucu olarak arşivlenmemiştir.
