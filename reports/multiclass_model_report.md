# CyberThreat AI v2
## Phase 5: Multiclass Classification Report

### 1. Objective

Classify network traffic into its original attack categories using supervised machine learning.

### 2. Dataset Overview

- Original records: 42,220
- Original categories: 15
- Numerical features: 69
- Records after conflicting feature-group removal: 42,034
- Unique feature groups after conflict removal: 35,559
- Conflicting feature groups identified: 8
- Records removed due to conflicting labels: 186

### 3. Data Preparation

The following columns were excluded from model training:

- Flow ID
- Source IP
- Destination IP
- Timestamp
- Day
- Label
- Source Port
- Destination Port

Only numerical features were used.

Identical numerical feature rows were assigned to the same group. Feature groups containing multiple different labels were identified as conflicting groups and removed.

Repeated observations with consistent labels were retained.

### 4. Train-Test Split

- Splitting strategy: StratifiedGroupKFold
- Number of folds: 5
- Selected fold: First fold
- Random state: 42
- Training records: 33,747
- Testing records: 8,287
- Classes in training: 15
- Classes in testing: 15
- Overlapping feature groups: 0

The group-aware splitting strategy ensured that identical feature groups did not appear in both training and testing datasets.

### 5. Models Evaluated

Two supervised machine learning algorithms were trained:

1. Decision Tree Classifier
2. Random Forest Classifier

Class weighting was applied to address class imbalance.

### 6. Model Comparison

| Model | Accuracy | Balanced Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 |
|---|---:|---:|---:|---:|---:|---:|
| Decision Tree | 97.71% | 88.05% | 90.15% | 88.05% | 88.97% | 97.71% |
| Random Forest | 97.82% | 87.68% | 94.65% | 87.68% | 90.06% | 97.78% |

### 7. Selected Model

Random Forest was selected based on its highest Macro F1 score.

### 8. Random Forest Performance

- Accuracy: 97.82%
- Balanced Accuracy: 87.68%
- Macro Precision: 94.65%
- Macro Recall: 87.68%
- Macro F1: 90.06%
- Weighted F1: 97.78%

### 9. Class-Level Evaluation

| Category | Precision | Recall | F1-Score | Test Support |
|---|---:|---:|---:|---:|
| BENIGN | 0.99 | 0.99 | 0.99 | 3,906 |
| Bot | 0.94 | 0.85 | 0.89 | 209 |
| DDoS | 1.00 | 1.00 | 1.00 | 799 |
| DoS GoldenEye | 1.00 | 0.99 | 0.99 | 293 |
| DoS Hulk | 0.99 | 0.99 | 0.99 | 764 |
| DoS Slowhttptest | 0.99 | 0.99 | 0.99 | 313 |
| DoS slowloris | 0.99 | 0.99 | 0.99 | 282 |
| FTP-Patator | 1.00 | 1.00 | 1.00 | 333 |
| Heartbleed | 1.00 | 1.00 | 1.00 | 3 |
| Infiltration | 1.00 | 0.67 | 0.80 | 9 |
| PortScan | 1.00 | 1.00 | 1.00 | 723 |
| SSH-Patator | 1.00 | 1.00 | 1.00 | 340 |
| Web Attack - Brute Force | 0.69 | 0.72 | 0.71 | 178 |
| Web Attack - Sql Injection | 1.00 | 0.40 | 0.57 | 5 |
| Web Attack - XSS | 0.61 | 0.55 | 0.58 | 130 |

### 10. Key Findings

- Random Forest achieved 97.82% overall accuracy.
- Random Forest achieved a Macro F1 score of 90.06%.
- DDoS, PortScan and FTP-Patator achieved an F1-score of 1.00 on this test set.
- Several DoS categories also achieved F1-scores close to 1.00.
- Web Attack - Brute Force, SQL Injection and XSS showed comparatively lower classification performance.
- The results indicate that performance varies considerably across attack categories.

### 11. Limitations

- The dataset is an attack-enriched sample of CIC-IDS2017 and does not represent real-world attack prevalence.
- Heartbleed, SQL Injection and Infiltration have very small test supports.
- High scores on rare categories should not be interpreted as proof of reliable generalisation.
- Evaluation is based on a single group-aware train-test fold.
- Testing on independent datasets and unseen attack environments is required to assess broader generalisation.
- Feature-group removal may exclude ambiguous observations where identical numerical features have different labels.

### 12. Generated Files

- multiclass_metrics.csv
- multiclass_classification_report.csv
- multiclass_confusion_matrix.csv
- multiclass_feature_importance.csv
- multiclass_best_model.joblib

### 13. Conclusion

The multiclass classification experiment successfully evaluated Decision Tree and Random Forest models across 15 network traffic categories.

Random Forest achieved the highest Macro F1 score of 90.06% and an overall accuracy of 97.82%.

The group-aware evaluation approach retained repeated observations while preventing identical feature groups from appearing in both training and testing datasets.

The experiment demonstrates the potential of supervised machine learning for network traffic classification while highlighting the need for further evaluation of rare and difficult-to-classify attack categories.

