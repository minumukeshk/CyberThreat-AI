import pandas as pd
import numpy as np
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, classification_report, confusion_matrix,
    balanced_accuracy_score
)

ROOT = Path.cwd()
DATA_PATH = ROOT / "data" / "master_dataset.csv"

REPORTS = ROOT / "reports"
MODELS = ROOT / "models"

REPORTS.mkdir(exist_ok=True)
MODELS.mkdir(exist_ok=True)

print("=" * 60)
print("CYBERTHREAT AI - PHASE 5: MULTICLASS CLASSIFICATION")
print("=" * 60)

# 1. Load dataset
df = pd.read_csv(DATA_PATH, low_memory=False)

print("\nOriginal dataset:", df.shape)
print("Original classes:", df["Label"].nunique())

# 2. Prepare features and target
drop_columns = [
    "Flow ID", "Source IP", "Destination IP",
    "Timestamp", "Day", "Label",
    "Source Port", "Destination Port"
]

X = df.drop(columns=drop_columns, errors="ignore")
y = df["Label"].copy()

# Keep numeric features only
X = X.select_dtypes(include=[np.number])
X = X.replace([np.inf, -np.inf], np.nan)

# 3. Remove conflicting feature-label combinations
grouped = X.groupby(list(X.columns), dropna=False)["Label"] if False else None

feature_groups = pd.concat(
    [X.reset_index(drop=True), y.reset_index(drop=True).rename("Target")],
    axis=1
)

conflicts = (
    feature_groups.groupby(list(X.columns), dropna=False)["Target"]
    .nunique()
)

conflict_keys = conflicts[conflicts > 1].index

multi_index = pd.MultiIndex.from_frame(X)
conflict_mask = multi_index.isin(conflict_keys)

X = X.loc[~conflict_mask].copy()
y = y.loc[~conflict_mask].copy()

# Remove identical feature rows after conflicting groups are removed
X["_target_temp_"] = y
combined = X.drop_duplicates()
y = combined.pop("_target_temp_")
X = combined

print("\nRecords after conflict removal and deduplication:", len(X))
print("Remaining classes:", y.nunique())

class_counts = y.value_counts()
print("\nClass distribution:")
print(class_counts)

if class_counts.min() < 2:
    raise ValueError(
        "At least one class has fewer than 2 records. "
        "A stratified train-test split is not possible."
    )

# 4. Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# 5. Train Decision Tree
print("\nTraining Decision Tree...")

dt_model = DecisionTreeClassifier(
    random_state=42,
    class_weight="balanced"
)

dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)

# 6. Train Random Forest
print("Training Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced_subsample"
)

rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# 7. Evaluate models
models = {
    "Decision Tree": (dt_model, dt_predictions),
    "Random Forest": (rf_model, rf_predictions)
}

results = []

for name, (model, predictions) in models.items():
    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Balanced Accuracy": balanced_accuracy_score(y_test, predictions),
        "Precision Macro": precision_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "Recall Macro": recall_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "F1 Macro": f1_score(
            y_test, predictions, average="macro", zero_division=0
        ),
        "F1 Weighted": f1_score(
            y_test, predictions, average="weighted", zero_division=0
        )
    })

metrics = pd.DataFrame(results)
print("\nMODEL COMPARISON")
print(metrics.round(4).to_string(index=False))

metrics.to_csv(REPORTS / "multiclass_metrics.csv", index=False)

# 8. Select model using macro F1
best_name = metrics.sort_values(
    "F1 Macro", ascending=False
).iloc[0]["Model"]

best_model, best_predictions = models[best_name]

print("\nSelected model:", best_name)

# 9. Classification report
class_report = classification_report(
    y_test,
    best_predictions,
    labels=sorted(y.unique()),
    zero_division=0,
    output_dict=True
)

class_report_df = pd.DataFrame(class_report).transpose()
class_report_df.to_csv(
    REPORTS / "multiclass_classification_report.csv"
)

print("\nCLASSIFICATION REPORT")
print(classification_report(
    y_test,
    best_predictions,
    labels=sorted(y.unique()),
    zero_division=0
))

# 10. Confusion matrix
labels = sorted(y.unique())

cm = confusion_matrix(
    y_test,
    best_predictions,
    labels=labels
)

cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels
)

cm_df.to_csv(REPORTS / "multiclass_confusion_matrix.csv")

# 11. Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": best_model.feature_importances_
}).sort_values("Importance", ascending=False)

importance.to_csv(
    REPORTS / "multiclass_feature_importance.csv",
    index=False
)

# 12. Save best model
joblib.dump(
    {
        "model": best_model,
        "features": list(X.columns),
        "classes": labels
    },
    MODELS / "multiclass_best_model.joblib"
)

# 13. Save project report
best_metrics = metrics[metrics["Model"] == best_name].iloc[0]

report = f"""# CyberThreat AI v2
## Phase 5: Multiclass Classification Report

### Objective
Classify network traffic into its original attack categories.

### Dataset
- Original records: {len(df)}
- Original categories: {df['Label'].nunique()}
- Records after conflict removal and deduplication: {len(X)}
- Numerical features: {X.shape[1]}
- Training records: {len(X_train)}
- Testing records: {len(X_test)}
- Train-test strategy: Stratified 80:20 split
- Random state: 42

### Models
- Decision Tree
- Random Forest

### Model Comparison

{metrics.to_markdown(index=False)}

### Selected Model
{best_name}

### Selected Model Performance
- Accuracy: {best_metrics['Accuracy']:.4f}
- Balanced Accuracy: {best_metrics['Balanced Accuracy']:.4f}
- Macro Precision: {best_metrics['Precision Macro']:.4f}
- Macro Recall: {best_metrics['Recall Macro']:.4f}
- Macro F1: {best_metrics['F1 Macro']:.4f}
- Weighted F1: {best_metrics['F1 Weighted']:.4f}

### Important Limitations
- Very rare categories have limited examples.
- Stratification does not guarantee generalisation to unseen attack families.
- Results are based on an attack-enriched CIC-IDS2017 sample.
- Further generalisation testing is required.
- Performance on rare classes must be interpreted using per-class metrics.

### Generated Files
- multiclass_metrics.csv
- multiclass_classification_report.csv
- multiclass_confusion_matrix.csv
- multiclass_feature_importance.csv
- multiclass_best_model.joblib
"""

(REPORTS / "multiclass_model_report.md").write_text(
    report, encoding="utf-8"
)

print("\n" + "=" * 60)
print("PHASE 5 CORE MODEL TRAINING FINISHED")
print("=" * 60)

print("\nGenerated files:")
for path in [
    REPORTS / "multiclass_metrics.csv",
    REPORTS / "multiclass_classification_report.csv",
    REPORTS / "multiclass_confusion_matrix.csv",
    REPORTS / "multiclass_feature_importance.csv",
    REPORTS / "multiclass_model_report.md",
    MODELS / "multiclass_best_model.joblib"
]:
    print(path)

print("\nIMPORTANT: Review per-class results before marking Phase 5 complete.")
