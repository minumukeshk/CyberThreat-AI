import os
import warnings
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")

# ============================================================
# CYBERTHREAT AI V2
# PHASE 7: K-MEANS CLUSTERING AND SHAP EXPLAINABILITY
# ============================================================

ROOT = os.getcwd()

DATA_PATH = os.path.join(ROOT, "data", "master_dataset.csv")
MODEL_PATH = os.path.join(ROOT, "models", "multiclass_best_model.joblib")

REPORT_DIR = os.path.join(ROOT, "reports")
MODEL_DIR = os.path.join(ROOT, "models")

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

RANDOM_STATE = 42

print("=" * 65)
print("CYBERTHREAT AI V2 - PHASE 7")
print("=" * 65)


# ============================================================
# 1. LOAD DATA
# ============================================================

print("\n[1/8] Loading dataset and saved model...")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH)

print("Dataset shape:", df.shape)
print("Model:", type(model).__name__)

if "Label" not in df.columns:
    raise ValueError("Label column is missing from the dataset.")


# ============================================================
# 2. PREPARE NUMERICAL FEATURES
# ============================================================

print("\n[2/8] Preparing numerical features...")

excluded_columns = [
    "Flow ID",
    "Source IP",
    "Destination IP",
    "Timestamp",
    "Day",
    "Label",
    "Source Port",
    "Destination Port"
]

if hasattr(model, "feature_names_in_"):
    feature_columns = list(model.feature_names_in_)
else:
    feature_columns = [
        col for col in df.select_dtypes(include=np.number).columns
        if col not in excluded_columns
    ]

missing_columns = [
    col for col in feature_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Model features missing from dataset: {missing_columns}"
    )

X = df[feature_columns].copy()

X = X.replace([np.inf, -np.inf], np.nan)

if X.isnull().sum().sum() > 0:
    raise ValueError(
        "Missing or infinite values found in model features. "
        "Do not silently impute them. Check the cleaned dataset."
    )

if X.shape[1] != 69:
    raise ValueError(
        f"Expected 69 model features, found {X.shape[1]}. "
        "Check feature selection before continuing."
    )

if len(feature_columns) != model.n_features_in_:
    raise ValueError("Feature count does not match saved model.")

labels = df["Label"].astype(str).reset_index(drop=True)
X = X.reset_index(drop=True)

print("Records:", len(X))
print("Features:", X.shape[1])
print("Attack categories:", labels.nunique())


# ============================================================
# 3. K-MEANS CLUSTERING
# ============================================================

print("\n[3/8] Running K-means clustering...")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Compare different cluster counts
cluster_results = []

for k in range(2, 7):

    print(f"Testing K = {k}")

    kmeans_test = KMeans(
        n_clusters=k,
        random_state=RANDOM_STATE,
        n_init=10
    )

    cluster_labels = kmeans_test.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        cluster_labels,
        sample_size=min(5000, len(X_scaled)),
        random_state=RANDOM_STATE
    )

    cluster_results.append({
        "K": k,
        "Inertia": kmeans_test.inertia_,
        "Silhouette_Score": score
    })

cluster_results_df = pd.DataFrame(cluster_results)

cluster_results_df.to_csv(
    os.path.join(REPORT_DIR, "phase7_cluster_comparison.csv"),
    index=False
)

best_k = int(
    cluster_results_df.loc[
        cluster_results_df["Silhouette_Score"].idxmax(),
        "K"
    ]
)

print("\nCluster comparison:")
print(cluster_results_df.to_string(index=False))

print("\nSelected K:", best_k)


# ============================================================
# 4. TRAIN FINAL K-MEANS MODEL
# ============================================================

print("\n[4/8] Fitting final K-means model...")

kmeans = KMeans(
    n_clusters=best_k,
    random_state=RANDOM_STATE,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df_clustered = df.copy()
df_clustered["Cluster"] = clusters

df_clustered.to_csv(
    os.path.join(REPORT_DIR, "phase7_clustered_dataset.csv"),
    index=False
)

joblib.dump(
    scaler,
    os.path.join(MODEL_DIR, "phase7_kmeans_scaler.joblib")
)

joblib.dump(
    kmeans,
    os.path.join(MODEL_DIR, "phase7_kmeans_model.joblib")
)

cluster_distribution = (
    df_clustered["Cluster"]
    .value_counts()
    .sort_index()
    .rename_axis("Cluster")
    .reset_index(name="Records")
)

cluster_distribution.to_csv(
    os.path.join(REPORT_DIR, "phase7_cluster_distribution.csv"),
    index=False
)

print("\nCluster distribution:")
print(cluster_distribution.to_string(index=False))


# ============================================================
# 5. CLUSTER VS ATTACK CATEGORY ANALYSIS
# ============================================================

print("\n[5/8] Analysing cluster composition...")

cluster_label_analysis = pd.crosstab(
    df_clustered["Cluster"],
    df_clustered["Label"]
)

cluster_label_analysis.to_csv(
    os.path.join(REPORT_DIR, "phase7_cluster_label_analysis.csv")
)

cluster_label_percentage = pd.crosstab(
    df_clustered["Cluster"],
    df_clustered["Label"],
    normalize="index"
) * 100

cluster_label_percentage.to_csv(
    os.path.join(REPORT_DIR, "phase7_cluster_label_percentage.csv")
)

print("\nCluster and attack category distribution:")
print(cluster_label_analysis)


# ============================================================
# 6. PCA VISUALIZATION
# ============================================================

print("\n[6/8] Generating PCA visualization...")

pca = PCA(n_components=2, random_state=RANDOM_STATE)

X_pca = pca.fit_transform(X_scaled)

pca_df = pd.DataFrame({
    "PCA1": X_pca[:, 0],
    "PCA2": X_pca[:, 1],
    "Cluster": clusters
})

# Plot a sample to keep visualization readable
plot_df = pca_df.sample(
    n=min(10000, len(pca_df)),
    random_state=RANDOM_STATE
)

plt.figure(figsize=(11, 7))

for cluster_id in sorted(plot_df["Cluster"].unique()):

    subset = plot_df[plot_df["Cluster"] == cluster_id]

    plt.scatter(
        subset["PCA1"],
        subset["PCA2"],
        label=f"Cluster {cluster_id}",
        alpha=0.55,
        s=12
    )

plt.title("CyberThreat AI - K-means Traffic Clusters")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(REPORT_DIR, "phase7_kmeans_pca.png"),
    dpi=300
)

plt.close()


# ============================================================
# 7. SHAP EXPLAINABILITY
# ============================================================

print("\n[7/8] Running SHAP explainability...")

try:

    import sys

    

    # Prevent incompatible optional PySpark integration.

    sys.modules["pyspark"] = None

    

    import shap
    # Use a manageable sample for explanation.
    sample_size = min(500, len(X))

    X_shap = X.sample(
        n=sample_size,
        random_state=RANDOM_STATE
    )

    print("SHAP sample size:", sample_size)

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_shap)

    # Handle different SHAP output formats.
    if isinstance(shap_values, list):

        importance_values = np.mean(
            np.stack([
                np.abs(values).mean(axis=0)
                for values in shap_values
            ]),
            axis=0
        )

    else:

        shap_array = np.asarray(shap_values)

        if shap_array.ndim == 3:

            # Common multiclass layouts:
            # samples x features x classes
            # samples x classes x features

            if shap_array.shape[1] == X_shap.shape[1]:
                importance_values = np.abs(shap_array).mean(
                    axis=(0, 2)
                )

            elif shap_array.shape[2] == X_shap.shape[1]:
                importance_values = np.abs(shap_array).mean(
                    axis=(0, 1)
                )

            else:
                raise ValueError(
                    "Unexpected 3D SHAP output shape: "
                    f"{shap_array.shape}"
                )

        elif shap_array.ndim == 2:

            importance_values = np.abs(shap_array).mean(axis=0)

        else:

            raise ValueError(
                f"Unexpected SHAP output dimensions: {shap_array.shape}"
            )

    if len(importance_values) != X_shap.shape[1]:
        raise ValueError("SHAP feature importance count mismatch.")

    shap_importance = pd.DataFrame({
        "Feature": X_shap.columns,
        "Mean_Absolute_SHAP": importance_values
    }).sort_values(
        "Mean_Absolute_SHAP",
        ascending=False
    )

    shap_importance.to_csv(
        os.path.join(REPORT_DIR, "phase7_shap_feature_importance.csv"),
        index=False
    )

    # Global SHAP feature importance plot
    plt.figure(figsize=(10, 8))

    shap_importance.head(20).sort_values(
        "Mean_Absolute_SHAP"
    ).plot(
        x="Feature",
        y="Mean_Absolute_SHAP",
        kind="barh",
        legend=False,
        figsize=(10, 8)
    )

    plt.title("Top 20 Features - Mean Absolute SHAP Values")
    plt.xlabel("Mean Absolute SHAP Value")
    plt.ylabel("Feature")
    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORT_DIR, "phase7_shap_feature_importance.png"),
        dpi=300
    )

    plt.close()

    # Class-specific SHAP summary plot for Web Attack - XSS

    class_name = "Web Attack - XSS"
    model_classes = list(model.classes_)

    if class_name not in model_classes:
        raise ValueError(f"Class not found: {class_name}")

    class_index = model_classes.index(class_name)

    if isinstance(shap_values, list):
        class_shap_values = shap_values[class_index]
    else:
        shap_array = np.asarray(shap_values)

        if shap_array.ndim != 3:
            raise ValueError(
                f"Unexpected SHAP shape: {shap_array.shape}"
            )

        if shap_array.shape[1] == X_shap.shape[1]:
            class_shap_values = shap_array[:, :, class_index]
        elif shap_array.shape[2] == X_shap.shape[1]:
            class_shap_values = shap_array[:, class_index, :]
        else:
            raise ValueError(
                f"Cannot identify feature axis: {shap_array.shape}"
            )

    shap.summary_plot(
        class_shap_values,
        X_shap,
        show=False,
        max_display=20
    )

    plt.title(f"SHAP Summary - {class_name}")
    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORT_DIR, "phase7_shap_summary.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    shap_status = "SUCCESS"

    print("\nTop SHAP features:")
    print(shap_importance.head(10).to_string(index=False))

except Exception as error:

    shap_status = "FAILED"

    print("\nSHAP execution failed:")
    print(repr(error))

    print(
        "\nK-means outputs are preserved. "
        "Do not treat SHAP as completed."
    )


# ============================================================
# 8. GENERATE PHASE 7 REPORT
# ============================================================

print("\n[8/8] Generating Phase 7 report...")

silhouette_best = float(
    cluster_results_df.loc[
        cluster_results_df["K"] == best_k,
        "Silhouette_Score"
    ].iloc[0]
)

report = f"""
# CyberThreat AI v2
## Phase 7: K-means Clustering and SHAP Explainability

### 1. Objective

Discover patterns in network traffic using unsupervised K-means
clustering and explain the saved multiclass Random Forest model
using SHAP.

### 2. Dataset

- Records: {len(X)}
- Numerical features: {X.shape[1]}
- Attack categories: {labels.nunique()}
- Dataset: CIC-IDS2017 master dataset

### 3. K-means Methodology

- Algorithm: K-means
- Feature scaling: StandardScaler
- Random state: {RANDOM_STATE}
- Tested cluster counts: 2 to 6
- Cluster selection: Highest sampled Silhouette Score
- Selected K: {best_k}
- Selected Silhouette Score: {silhouette_best:.6f}

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

SHAP execution status: {shap_status}

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
"""

report_path = os.path.join(
    REPORT_DIR,
    "phase7_clustering_shap_report.md"
)

with open(report_path, "w", encoding="utf-8") as file:
    file.write(report.strip() + "\n")


# ============================================================
# FINAL OUTPUT AUDIT
# ============================================================

print("\n" + "=" * 65)
print("PHASE 7 EXECUTION SUMMARY")
print("=" * 65)

print("K-means selected K:", best_k)
print("Silhouette Score:", round(silhouette_best, 6))
print("SHAP status:", shap_status)

print("\nGenerated Phase 7 report:")
print(report_path)

print("\nPhase 7 report files:")

for filename in sorted(os.listdir(REPORT_DIR)):
    if filename.startswith("phase7_"):
        filepath = os.path.join(REPORT_DIR, filename)
        print(f"{filename} | {os.path.getsize(filepath):,} bytes")

print("\n" + "=" * 65)
print("PHASE 7 SCRIPT FINISHED")
print("=" * 65)

if shap_status != "SUCCESS":
    raise RuntimeError(
        "K-means completed, but SHAP failed. "
        "Review the error above before marking Phase 7 complete."
    )

