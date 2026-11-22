# CyberThreat AI v2
## Phase 7: K-means Clustering and SHAP Explainability

### 1. Objective

Discover patterns in network traffic using unsupervised K-means
clustering and explain the saved multiclass Random Forest model
using SHAP.

### 2. Dataset

- Records: 42220
- Numerical features: 69
- Attack categories: 15
- Dataset: CIC-IDS2017 master dataset

### 3. K-means Methodology

- Algorithm: K-means
- Feature scaling: StandardScaler
- Random state: 42
- Tested cluster counts: 2 to 6
- Cluster selection: Highest sampled Silhouette Score
- Selected K: 2
- Selected Silhouette Score: 0.488666

The attack labels were not used to fit the clustering algorithm.
They were used only after clustering to examine cluster composition.

### 4. Cluster Analysis

Cluster distribution is available in:

- phase7_cluster_distribution.csv
- phase7_cluster_label_analysis.csv
- phase7_cluster_label_percentage.csv

PCA visualization:

- phase7_kmeans_pca.png

### 5. SHAP Explainability

SHAP execution status: SUCCESS

The saved multiclass Random Forest model was used.
No model retraining was performed.

Generated SHAP outputs, when successful:

- phase7_shap_feature_importance.csv
- phase7_shap_feature_importance.png
- phase7_shap_summary.png

### 6. Limitations

- K-means assumes distance-based cluster structure.
- StandardScaler is sensitive to extreme values.
- Silhouette Score was estimated using a sample of up to 5,000 records.
- Cluster IDs do not represent attack categories automatically.
- SHAP explanations describe the saved model, not necessarily
  the underlying real-world causes of network activity.
- CIC-IDS2017 is a benchmark dataset and does not establish
  performance on unseen production networks.

### 7. Conclusion

Phase 7 applies unsupervised learning to identify network traffic
groupings and uses SHAP to interpret the saved multiclass model.

The results should be interpreted with the evaluation limitations
and class support in mind.
