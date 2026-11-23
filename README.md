# 🛡️ CyberThreat-AI

### Network Security Analytics, Intrusion Detection & Machine Learning

CyberThreat-AI is an end-to-end cybersecurity analytics project focused on analyzing network traffic, identifying malicious activity, understanding attack patterns, and evaluating machine learning approaches for network intrusion detection.

The project combines **Data Analytics, Statistical Analysis, Machine Learning, Clustering, Explainable AI, SQL, Excel, and Power BI** to transform network traffic data into meaningful cybersecurity insights.

---

## 📌 Project Overview

Network traffic contains valuable information that can help identify suspicious behavior, malicious activities, and potential security threats. However, analyzing large volumes of network traffic manually is challenging.

CyberThreat-AI explores the CIC-IDS2017 network traffic dataset to:

- Analyze network traffic patterns.
- Identify benign and malicious traffic.
- Understand the distribution of different attack categories.
- Perform exploratory data analysis and statistical analysis.
- Develop machine learning models for intrusion detection.
- Evaluate model performance using multiple metrics.
- Explore traffic patterns using unsupervised learning.
- Interpret model behavior using SHAP explainability.

The project follows an **analyst-first approach**, where data analysis and cybersecurity insights are the primary focus, supported by machine learning techniques.

---

## 🎯 Objectives

- Perform data cleaning and preprocessing on network traffic data.
- Conduct exploratory data analysis (EDA).
- Analyze traffic distribution across attack categories and days.
- Identify important network traffic features.
- Perform statistical analysis to investigate differences between traffic categories.
- Develop binary classification models for benign and malicious traffic detection.
- Develop multiclass classification models to identify different attack categories.
- Evaluate classification models using appropriate performance metrics.
- Apply K-Means clustering to explore traffic patterns.
- Use SHAP to investigate feature contributions.
- Build analytical reports and dashboards using Excel and Power BI.

---

## 📊 Dataset

### CIC-IDS2017

The project uses the **CIC-IDS2017 dataset**, a publicly available network intrusion detection dataset containing benign traffic and multiple types of network attacks.

The dataset includes network flow features such as:

- Flow duration
- Packet counts
- Packet lengths
- Flow inter-arrival times
- Bytes per second
- Packets per second
- TCP flag counts
- Active and idle statistics
- Network protocol information
- Traffic labels

### Dataset Categories

The dataset includes benign traffic and multiple attack categories, including:

- BENIGN
- DDoS
- DoS attacks
- PortScan
- Bot
- FTP-Patator
- SSH-Patator
- Infiltration
- Heartbleed
- Web attacks

### Dataset Preparation

The project includes data preparation and cleaning workflows involving:

- Dataset inspection
- Data cleaning
- Handling invalid values
- Feature analysis
- Dataset integration
- Label analysis
- Preparation of analytical datasets

**Note:** Original raw datasets are not included in the GitHub repository because of their size. Users should obtain the CIC-IDS2017 dataset from its official source and place the required files in the appropriate data directory.

---

## 🔄 Project Workflow

```text
CIC-IDS2017 Dataset
        │
        ▼
Data Understanding
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ├──────────────► Statistical Analysis
        │
        ├──────────────► Excel Analysis
        │
        ├──────────────► SQL Analysis
        │
        └──────────────► Power BI Dashboard
        │
        ▼
Machine Learning
        │
        ├── Binary Classification
        │
        ├── Multiclass Classification
        │
        └── Advanced Model Evaluation
        │
        ▼
Unsupervised Learning
        │
        └── K-Means Clustering
        │
        ▼
Explainable AI
        │
        └── SHAP Analysis
        │
        ▼
Cybersecurity Insights
```

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the characteristics and distribution of network traffic.

The analysis includes:

- Dataset structure and dimensions
- Traffic label distribution
- Attack category distribution
- Traffic analysis across different days
- Numerical feature distributions
- Correlation analysis
- Feature relationships
- Identification of potential patterns and anomalies

The EDA results are documented in the project reports and notebooks.

---

## 📈 Statistical Analysis

Statistical analysis was performed to investigate differences between network traffic categories.

The project includes statistical comparison techniques to explore whether traffic characteristics differ significantly across groups.

The analysis includes:

- Group comparisons
- Statistical testing
- Multiple comparison analysis
- Games-Howell post-hoc comparisons

The corresponding statistical outputs are available in the `reports/` directory.

---

## 🤖 Machine Learning

### 1. Binary Classification

The binary classification task focuses on distinguishing:

- **BENIGN traffic**
- **ATTACK traffic**

The classification workflow includes:

- Feature preparation
- Data splitting
- Model training
- Model evaluation
- Performance comparison

Models explored include:

- Logistic Regression
- Decision Tree
- Random Forest

Evaluation metrics include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

The binary classification workflow is available in:

```text
notebooks/03_binary_classification.ipynb
```

---

### 2. Multiclass Classification

The multiclass classification task aims to classify network traffic into different traffic and attack categories.

The workflow includes:

- Feature preparation
- Multiclass label handling
- Group-aware data splitting
- Model training
- Model comparison
- Performance evaluation

The project evaluates classification performance using:

- Accuracy
- Balanced Accuracy
- Precision
- Recall
- Macro F1-score
- Weighted F1-score
- Confusion Matrix

The multiclass classification workflow is available in:

```text
notebooks/04_multiclass_classification.ipynb
```

A trained multiclass model is included in the repository.

---

## 📊 Advanced Model Evaluation

The project includes advanced evaluation of the multiclass classification model.

Evaluation includes:

- Classification report
- Confusion matrix analysis
- Normalized confusion matrix
- Class-wise performance
- Misclassification analysis
- ROC-AUC analysis
- Precision-Recall analysis
- Error analysis across classes

These evaluations help identify strengths and limitations of the model, particularly for less frequent attack categories.

The detailed evaluation outputs are available in:

```text
reports/
```

---

## 🔬 K-Means Clustering

Unsupervised learning was used to explore network traffic patterns without using traffic labels during the clustering process.

The clustering workflow includes:

- Feature scaling
- K-Means clustering
- Evaluation of multiple cluster configurations
- Silhouette score comparison
- Cluster distribution analysis
- PCA-based visualization
- Post-clustering comparison with traffic labels

The clustering analysis is intended to explore traffic patterns and similarities, rather than serve as a standalone intrusion detection system.

The trained clustering model and scaler are available in:

```text
models/
```

---

## 🧠 Explainable AI (SHAP)

SHAP was used to investigate feature contributions within the clustering analysis.

The analysis includes:

- Feature importance investigation
- SHAP summary visualization
- Mean absolute SHAP values
- Feature contribution analysis

SHAP results help investigate which network traffic characteristics contribute most to the model's output.

**Important:** Feature importance indicates model behavior and does not establish causation.

---

## 📊 Excel Analysis

The Excel workbook contains analytical summaries and traffic analysis.

File:

```text
excel/CyberThreat_AI_Analysis.xlsx
```

Workbook sheets include:

- `Attack_Analysis`
- `Sheet1`
- `Day_Attack_Analysis`
- `master_dataset`
- `XLOOKUP_AnalysisFlo`

The workbook includes attack distribution analysis, day-wise traffic analysis, dataset information, and lookup-related analysis.

---

## 📈 Power BI Dashboard

An interactive Power BI report was developed for network traffic investigation and analysis.

File:

```text
powerbi/Threat Investigation.pbix
```

### Dashboard Pages

#### 1. Executive Overview

Provides a high-level overview of network traffic and attack-related information.

#### 2. Threat Investigation

Supports investigation of network traffic through different traffic attributes and visualizations.

#### 3. ML Detection Performance

Provides a view of machine learning detection and classification performance.

The dashboard includes different visualization types such as:

- KPI cards
- Bar charts
- Column charts
- Donut charts
- Line charts
- Slicers

---

## 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Explainable AI

- SHAP

### Database

- MySQL

### Business Intelligence

- Microsoft Excel
- Power BI

### Development Tools

- Jupyter Notebook
- Git
- GitHub

---

## 📁 Project Structure

```text
CyberThreat-AI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── excel/
│   └── CyberThreat_AI_Analysis.xlsx
│
├── models/
│   ├── multiclass_best_model.joblib
│   ├── phase7_kmeans_model.joblib
│   └── phase7_kmeans_scaler.joblib
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_binary_classification.ipynb
│   └── 04_multiclass_classification.ipynb
│
├── powerbi/
│   └── Threat Investigation.pbix
│
├── reports/
│   ├── eda_summary.csv
│   ├── feature_importance.csv
│   ├── model_report.md
│   ├── multiclass_model_report.md
│   ├── phase6_advanced_evaluation_report.md
│   ├── phase7_clustering_shap_report.md
│   ├── sql_findings.md
│   ├── data_quality.md
│   └── insights.md
│
├── sql/
│   ├── queries/
│   └── views/
│
├── src/
│   ├── import_to_mysql.py
│   ├── multiclass_classification.py
│   └── phase7_clustering_shap.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/minumukeshk/CyberThreat-AI.git
```

### 2. Navigate to the Project Directory

```bash
cd CyberThreat-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Dataset Setup

The raw CIC-IDS2017 dataset is not included in the GitHub repository.

Download the dataset from its official source and place the required files in the appropriate directory:

```text
data/raw/
```

---

## 📚 Project Reports

Detailed analysis and evaluation outputs are available in:

```text
reports/
```

The reports include:

- Exploratory Data Analysis
- Feature Importance
- Binary Classification Results
- Multiclass Classification Results
- Advanced Model Evaluation
- Confusion Matrix Analysis
- Misclassification Analysis
- Clustering Analysis
- SHAP Analysis
- Statistical Analysis
- Data Quality Findings
- SQL Analysis Findings

---

## ⚠️ Limitations

- The project uses the CIC-IDS2017 dataset, which represents a controlled traffic collection environment.
- Dataset class imbalance affects the performance of models on rare attack categories.
- Model performance on the dataset does not guarantee performance on real-world or unseen network environments.
- The clustering results are exploratory and should not be interpreted as a standalone threat detection system.
- SHAP feature contributions describe model behavior and do not imply causality.
- Further validation using unseen network traffic and additional datasets would be required before practical deployment.

---

## 🚀 Future Enhancements

Potential future improvements include:

- Evaluation on additional intrusion detection datasets
- Testing on unseen network environments
- Real-time network traffic monitoring
- Automated threat alerting
- Model deployment through an API
- Interactive investigation interface
- Additional anomaly detection methods
- Deep learning-based detection approaches
- Model monitoring and drift detection

---

## 👩‍💻 Author

**Minu Mukesh K**

MCA Student | Data Science | Machine Learning | Data Analytics

GitHub: [minumukeshk](https://github.com/minumukeshk)

---

## 📌 Disclaimer

This project is developed for educational, analytical, and research purposes.

The machine learning models and analytical methods are evaluated using the CIC-IDS2017 dataset. Results should not be interpreted as guarantees of performance in real-world cybersecurity environments.

---     