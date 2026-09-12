# Evaluation Methodology

## Ana metrikler

- **Validation NLL**: eğitim sırasında held-out split üzerinde takip edilir; düşük daha iyi.
- **Test NLL**: deney sonu genel karşılaştırma metriği; düşük daha iyi.
- **Perplexity**: `exp(NLL)`; düşük daha iyi.
- **Tokens/s**: eğitim throughput'u; yüksek daha iyi.
- **Peak allocated GPU memory**: karşılaştırma sırasında ölçülen maksimum ayrılmış GPU belleği; düşük daha verimli.

## Bütçe türleri

### Equal wall-clock
İki varyant aynı gerçek training süresiyle çalıştırılır. Auxiliary objective, teacher veya ek modül compute maliyeti doğrudan sonuca yansır. Deployment/training-ekonomisi açısından ana karşılaştırmadır.

### Equal training-token
İki varyant aynı token sayısını görür. Bu, mimari/objective'in **sample efficiency** etkisini compute maliyetinden ayırmaya yardım eder.

İdeal rapor her iki kıyası da içerir.

## İstatistik

Tek seed yalnız pilot/ön bulgu sayılır. Güçlü model karşılaştırmalarında en az 3 seed (`42, 43, 44` gibi) hedeflenir; ortalama ve standart sapma raporlanır.

## Sonuç dili

- Tek deneyden genel mimari yasası çıkarılmaz.
- Başarısız/negatif deneyler saklanır.
- Henüz çalıştırılmamış model için metrik yazılmaz.
- Veri veya eval protokolü değiştiğinde sonuçlar açıkça ayrı benchmark olarak etiketlenir.
