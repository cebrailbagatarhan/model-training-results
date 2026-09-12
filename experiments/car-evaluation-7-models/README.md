# Car Evaluation — 7 model karşılaştırması

**Durum:** `completed`

Dataset: UCI Car Evaluation, 1,728 örnek, 6 kategorik özellik, 4 sınıf. Preprocessing: label encoding; split: %80/%20; ayrıca 5-fold CV.

| Model | Test accuracy | CV ortalama | CV std |
|---|---:|---:|---:|
| Decision Tree | **98.55%** | 97.10% | 1.41% |
| Random Forest | 98.27% | 96.31% | 1.29% |
| Gradient Boosting | 97.98% | 97.97% | 0.93% |
| SVM | 92.77% | 88.71% | 1.00% |
| KNN | 90.75% | 88.28% | 1.47% |
| Logistic Regression | 69.08% | 69.54% | 0.65% |
| Naive Bayes | 64.16% | 64.62% | 2.71% |

Kaynak repo ayrıca karar ağacı, confusion matrix, ROC, learning curve ve feature-importance görselleştirmeleri içeriyor.
