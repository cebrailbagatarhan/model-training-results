# ModernLLM-Large — H100 kısmi eğitim kayıtları

**Durum:** `partial / not a final benchmark`

Bu kayıt, GitHub notebook günlükleri ile Drive'da saklanan artefaktların birlikte envanteridir. Tek bir kesintisiz ve held-out doğrulanmış final koşu olarak yorumlanmamalıdır.

## Kullanılan model ve ortam

- Model: ModernLLM-Large, 1,129,416,704 parametre
- GPU: NVIDIA H100, yaklaşık 79.2 GB görünür bellek
- Mimari: decoder-only; RMSNorm + RoPE + GQA + SwiGLU + KV-cache
- Veri aşamaları metadata'da: 57 pretrain metni, 31 SFT konuşması, 133 CoT örneği

## Kaydedilmiş koşu kanıtları

| Koşu | Durum | Son gözlem |
|---|---|---|
| İlk pre-training | optimizer adımı oluşmadı | `Total steps: 0`; `loss=0/PPL=1` geçerli eğitim sonucu değildir |
| SFT | tamamlanmamış çıktı | final metrik yok |
| CoT | CUDA OOM | final metrik yok |
| Extended run | 18,370 planlanan adımdan ~200'e kadar | ara eval loss 1.4176, PPL 4.13 |
| Optimized 1K | ~600. adımda kesildi | ara train loss 0.0009; ara eval loss 0.0001, PPL 1.00 |

Optimized 1K değerlendirmesinde train/eval seçimlerinin aynı corpus üzerinden bağımsız yapılması nedeniyle veri örtüşmesi mümkündür; çok düşük eval loss **genelleme kanıtı değildir**.

## Drive artefaktı

Drive'da yaklaşık 4.52 GB `model.pt`, tokenizer ve model metadata dosyaları bulundu. Ağırlık public GitHub'a taşınmadı; bu repo yalnızca sonuç/provenance kaydını tutuyor.

Kaynak kod/notebook: `cebrailbagatarhan/yapay-zeka-sistemi`.
