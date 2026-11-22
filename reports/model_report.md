# CyberThreat AI v2
## Phase 4: Binary Classification Model Report

### 1. Objective

The objective of this phase was to develop machine learning models to classify network traffic into two categories:

- BENIGN (0): Normal network traffic.
- ATTACK (1): Malicious network traffic.

### 2. Dataset Preparation

- Dataset: CIC-IDS2017
- Records before conflict removal: 42,220
- Records after conflict removal: 42,034
- Features used: 69 numerical features
- Training records: 33,591
- Testing records: 8,443

Features containing identifiers, IP addresses, ports, timestamps and target labels were excluded from model training.

Eight feature combinations contained conflicting binary labels. The 186 affected records were excluded to avoid training on contradictory examples.

### 3. Train-Test Splitting

A GroupShuffleSplit strategy was used to prevent identical feature combinations from appearing in both training and testing datasets.

- Training proportion: Approximately 80%
- Testing proportion: Approximately 20%
- Random state: 42
- Identical feature-row overlap between training and testing: 0%

### 4. Models Developed

Four approaches were evaluated:

1. Majority-Class Baseline
2. Logistic Regression
3. Decision Tree
4. Random Forest

### 5. Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Majority-Class Baseline | 51.26% | 51.26% | 100.00% | 67.78% |
| Logistic Regression | 87.55% | 84.46% | 92.79% | 88.43% |
| Decision Tree | 99.50% | 99.40% | 99.63% | 99.52% |
| Random Forest | 99.54% | 99.72% | 99.38% | 99.55% |

Random Forest achieved the highest accuracy, precision and F1 score. Decision Tree achieved the highest recall.

### 6. Random Forest Confusion Matrix

| | Predicted BENIGN | Predicted ATTACK |
|---|---:|---:|
| Actual BENIGN | 4103 | 12 |
| Actual ATTACK | 27 | 4301 |

Interpretation:

- True Negatives: 4,103
- False Positives: 12
- False Negatives: 27
- True Positives: 4,301

The model correctly classified most records, while a small number of benign and malicious records were misclassified.

### 7. Feature Importance

Permutation importance identified the following influential features:

| Feature | Importance |
|---|---:|
| Init_Win_bytes_forward | 0.030940 |
| Init_Win_bytes_backward | 0.009774 |
| URG Flag Count | 0.004604 |
| Fwd IAT Min | 0.003969 |
| Fwd Header Length | 0.001818 |

The initial window-size features had the strongest influence on the model's F1 score.

These values represent the mean decrease in F1 score when individual features are shuffled. They are not percentages.

### 8. Day-Wise Model Evaluation

| Day | Records | Accuracy | Attack Recall | F1 Score |
|---|---:|---:|---:|---:|
| Friday | 2,757 | 99.38% | 99.23% | 99.56% |
| Monday | 834 | 99.76% | N/A | N/A |
| Thursday | 1,195 | 99.08% | 97.60% | 98.34% |
| Tuesday | 1,377 | 100% | 100% | 100% |
| Wednesday | 2,280 | 99.61% | 99.74% | 99.70% |

Monday contained no attack records in the test set. Therefore, attack recall and attack-class F1 score were not applicable.

### 9. Key Findings

- Random Forest achieved the strongest overall performance among the evaluated models.
- Decision Tree achieved slightly higher attack recall.
- Logistic Regression provided a useful baseline for comparison.
- Group-based splitting prevented identical feature combinations from leaking across the training and testing sets.
- Feature importance highlighted the contribution of network packet and flow characteristics.

### 10. Limitations

- The dataset is an attack-enriched sample and does not represent real-world network traffic prevalence.
- High model scores on this dataset do not guarantee equivalent performance on unseen real-world networks.
- GroupShuffleSplit prevents identical feature groups from crossing the split but does not establish generalization to entirely unseen attack families or capture days.
- Additional validation is required before considering the model reliable for operational deployment.

### 11. Conclusion

The binary classification phase successfully developed and evaluated Logistic Regression, Decision Tree and Random Forest models for distinguishing benign and malicious network traffic.

Random Forest achieved the highest overall F1 score of 99.55% on the grouped holdout test set.

Further validation, multiclass classification and explainability analysis will be conducted in the subsequent phases of CyberThreat AI v2.

