# CyberThreat AI v2
## Phase 6: Advanced Machine Learning Evaluation

### 1. Objective

Evaluate the multiclass Random Forest model beyond basic accuracy using
confusion matrix analysis, ROC-AUC, precision-recall evaluation and
misclassification analysis.

### 2. Evaluation Dataset

- Model: Random Forest Classifier
- Test records: 8287
- Numerical features: 69
- Attack categories: 15
- Evaluation method: Reconstructed group-aware test split
- Model retraining: Not performed
- Prediction probabilities: Generated using the saved model

### 3. Overall Performance

| Metric | Result |
|---|---:|
| Accuracy | 0.978159 |
| Balanced Accuracy | 0.876782 |
| Macro Precision | 0.946547 |
| Macro Recall | 0.876782 |
| Macro F1 | 0.900598 |
| Weighted F1 | 0.977790 |

### 4. Confusion Matrix Analysis

- Total test records: 8287
- Correct predictions: 8106
- Misclassified predictions: 181
- Misclassification rate: 0.021841

The confusion matrix and row-normalized confusion matrix are available
as separate CSV files.

### 5. Multiclass ROC-AUC

One-vs-Rest ROC-AUC evaluation:

| Metric | Score |
|---|---:|
| Macro ROC-AUC | 0.994130 |
| Weighted ROC-AUC | 0.998871 |
| Micro ROC-AUC | 0.999228 |

Per-class ROC-AUC values are available in
phase6_roc_auc_per_class.csv.

### 6. Precision-Recall Evaluation

| Metric | Score |
|---|---:|
| Macro Average Precision | 0.933563 |
| Weighted Average Precision | 0.985734 |
| Micro Average Precision | 0.996121 |

Per-class Average Precision values are available in
phase6_precision_recall_per_class.csv.

### 7. Misclassification Analysis

- Total misclassified records: 181
- Most frequent actual/predicted category pairs are recorded in
  phase6_top_misclassification_pairs.csv.
- Misclassification counts by actual category are recorded in
  phase6_errors_by_class.csv.
- Individual prediction errors are available in
  phase6_misclassified_records.csv.

### 8. Evaluation Limitations

- The evaluation uses a single group-aware test fold.
- Rare categories have limited test support.
- ROC-AUC and Average Precision should be interpreted alongside
  per-class support and recall.
- The results do not establish performance on unseen datasets or
  real-world network environments.
- The dataset is an attack-enriched CIC-IDS2017 sample.

### 9. Generated Files

- phase6_confusion_matrix.csv
- phase6_normalized_confusion_matrix.csv
- phase6_class_confusion_analysis.csv
- phase6_confusion_matrix.png
- phase6_roc_auc_per_class.csv
- phase6_multiclass_roc_curves.png
- phase6_precision_recall_per_class.csv
- phase6_precision_recall_curves.png
- phase6_misclassified_records.csv
- phase6_top_misclassification_pairs.csv
- phase6_errors_by_class.csv
- phase6_advanced_metrics.csv
- phase6_classification_report.csv

### 10. Conclusion

The advanced evaluation assessed the existing Random Forest model
using multiple classification metrics and error analysis techniques.

The results provide a broader understanding of model performance
across the 15 network traffic categories. They also identify
misclassification patterns and highlight the limitations of
evaluating rare attack categories using a single test fold.
