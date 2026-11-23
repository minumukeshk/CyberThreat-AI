# CyberThreat AI v2
## Phase 4: Binary Classification Model Report

### 1. Objective

The objective of Phase 4 was to develop and evaluate machine learning models capable of classifying network traffic into two categories:

- **BENIGN (0):** Normal network traffic.
- **ATTACK (1):** Malicious network traffic.

This phase focused on identifying malicious network activity using supervised machine learning techniques and comparing multiple classification models based on their performance.

---

### 2. Dataset Preparation

The dataset used for this phase was derived from the CIC-IDS2017 network intrusion detection dataset.

| Parameter | Value |
|---|---|
| Dataset | CIC-IDS2017 |
| Records before conflict removal | 42,220 |
| Records after conflict removal | 42,034 |
| Removed conflicting records | 186 |
| Features used | 69 numerical features |
| Training records | 33,591 |
| Testing records | 8,443 |

Features containing identifiers, IP addresses, ports, timestamps, and target labels were excluded from model training to prevent inappropriate information from influencing the predictions.

During data preparation, eight feature combinations were identified as having conflicting binary labels. These combinations affected 186 records. The conflicting records were removed to prevent the models from learning contradictory labels for identical feature combinations.

---

### 3. Data Splitting Strategy

A **GroupShuffleSplit** strategy was used to divide the dataset into training and testing sets.

This approach grouped identical feature combinations together, preventing identical records from appearing in both datasets.

| Parameter | Value |
|---|---|
| Training proportion | Approximately 80% |
| Testing proportion | Approximately 20% |
| Random state | 42 |
| Group-based splitting | Yes |
| Identical feature-row overlap | 0% |

The absence of identical feature-row overlap between the training and testing datasets helped reduce data leakage and provided a more reliable evaluation of model performance.

However, this splitting strategy does not guarantee generalization to entirely unseen attack families, networks, or environments.

---

### 4. Models Developed

Four approaches were evaluated during this phase:

1. **Majority-Class Baseline**
2. **Logistic Regression**
3. **Decision Tree Classifier**
4. **Random Forest Classifier**

The majority-class baseline was used as a reference point to understand how much improvement the machine learning models achieved compared with a simple prediction strategy.

Logistic Regression provided a linear classification baseline, while Decision Tree and Random Forest were used to evaluate more complex nonlinear relationships in network traffic features.

---

### 5. Model Performance Comparison

The models were evaluated using Accuracy, Precision, Recall, and F1 Score.

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Majority-Class Baseline | 51.26% | 51.26% | 100.00% | 67.78% |
| Logistic Regression | 87.55% | 84.46% | 92.79% | 88.43% |
| Decision Tree | 99.50% | 99.40% | 99.63% | 99.52% |
| Random Forest | 99.54% | 99.72% | 99.38% | 99.55% |

### Performance Interpretation

- **Random Forest** achieved the highest Accuracy, Precision, and F1 Score.
- **Decision Tree** achieved the highest Recall.
- **Logistic Regression** performed substantially better than the majority-class baseline.
- Both tree-based models demonstrated strong performance on the grouped holdout test dataset.

Random Forest was selected as the best-performing model based on its overall balance of evaluation metrics.

---

### 6. Random Forest Confusion Matrix

The confusion matrix provides a detailed view of the Random Forest model's predictions.

| Actual Class | Predicted BENIGN | Predicted ATTACK |
|---|---:|---:|
| BENIGN | 4,103 | 12 |
| ATTACK | 27 | 4,301 |

### Confusion Matrix Interpretation

| Metric | Value |
|---|---:|
| True Negatives | 4,103 |
| False Positives | 12 |
| False Negatives | 27 |
| True Positives | 4,301 |

The model correctly classified the majority of benign and malicious network traffic.

- **True Negatives:** Benign traffic correctly identified as benign.
- **False Positives:** Benign traffic incorrectly classified as malicious.
- **False Negatives:** Malicious traffic incorrectly classified as benign.
- **True Positives:** Malicious traffic correctly identified as malicious.

The model produced a relatively small number of false positives and false negatives on the test dataset.

---

### 7. Feature Importance Analysis

Permutation importance was used to identify features that had a significant influence on the model's F1 Score.

| Feature | Importance |
|---|---:|
| Init_Win_bytes_forward | 0.030940 |
| Init_Win_bytes_backward | 0.009774 |
| URG Flag Count | 0.004604 |
| Fwd IAT Min | 0.003969 |
| Fwd Header Length | 0.001818 |

The initial TCP window-size features demonstrated the strongest influence on the model's performance.

Permutation importance measures the decrease in model performance when the values of an individual feature are randomly shuffled.

These importance values represent the mean decrease in F1 Score and should not be interpreted as percentages or as evidence of causal relationships.

---

### 8. Day-Wise Model Evaluation

The model was also evaluated across different days represented in the dataset to examine performance variation.

| Day | Records | Accuracy | Attack Recall | F1 Score |
|---|---:|---:|---:|---:|
| Friday | 2,757 | 99.38% | 99.23% | 99.56% |
| Monday | 834 | 99.76% | N/A | N/A |
| Thursday | 1,195 | 99.08% | 97.60% | 98.34% |
| Tuesday | 1,377 | 100.00% | 100.00% | 100.00% |
| Wednesday | 2,280 | 99.61% | 99.74% | 99.70% |

### Day-Wise Interpretation

The model maintained high accuracy across the evaluated days.

Thursday demonstrated comparatively lower performance, particularly in attack recall, indicating that a small proportion of malicious traffic was not detected.

Monday contained no attack records in the test subset. Therefore, attack recall and attack-class F1 Score could not be calculated for that day.

The day-wise evaluation provides additional insight into model performance across different traffic conditions. However, it should not be considered a complete temporal validation because the dataset and test split do not represent all possible future network environments.

---

### 9. Key Findings

The binary classification phase produced the following findings:

- Random Forest achieved the strongest overall performance among the evaluated models.
- Decision Tree achieved slightly higher Recall, making it effective at identifying malicious records in the evaluated dataset.
- Logistic Regression provided a useful baseline for comparison.
- Group-based splitting prevented identical feature combinations from appearing in both training and testing datasets.
- Initial TCP window-size features were among the most influential features.
- The model maintained high performance across the evaluated days.
- The evaluation demonstrated the potential of machine learning for distinguishing benign and malicious network traffic.

---

### 10. Limitations

Despite the high evaluation scores, several limitations must be considered:

- CIC-IDS2017 is an attack-enriched dataset and does not represent the actual prevalence of malicious traffic in all real-world networks.
- High performance on this dataset does not guarantee equivalent performance on unseen real-world network traffic.
- GroupShuffleSplit prevents identical feature combinations from crossing the train-test boundary but does not guarantee generalization to completely unseen attack families or environments.
- The dataset contains specific attack scenarios and traffic patterns that may not represent modern or emerging cyber threats.
- Further testing using additional datasets and real-world network traffic is required before operational deployment.
- Model performance may change when traffic characteristics, network infrastructure, or attack patterns change.

---

### 11. Conclusion

Phase 4 successfully developed and evaluated machine learning models for binary network traffic classification.

Logistic Regression, Decision Tree, and Random Forest were compared using a grouped holdout test dataset.

Random Forest achieved the highest overall F1 Score of **99.55%**, along with an Accuracy of **99.54%** and Precision of **99.72%**.

The results demonstrate the potential of machine learning techniques for identifying malicious network traffic within the CIC-IDS2017 dataset.

The binary classification model forms an important component of the broader CyberThreat AI project, which subsequently explores multiclass classification, advanced model evaluation, clustering, explainability, and cybersecurity analytics through Power BI.

Further validation using unseen datasets and real-world network environments remains necessary before the model can be considered suitable for operational cybersecurity deployment.