# 🛡️ CyberThreat-AI
### Network Security Analytics & Intelligent Threat Detection

## 📌 Project Overview

CyberThreat-AI is a data science and machine learning project focused on analyzing network traffic and identifying potential cyber threats.

The project uses network traffic data to explore patterns of normal and malicious activities, perform exploratory data analysis, build machine learning classification models, evaluate model performance, and analyze network traffic patterns through clustering and explainable AI techniques.

The goal is to transform network traffic data into meaningful security insights that can support threat detection and network security analysis.

## 🎯 Objectives

- Analyze network traffic data to identify patterns and anomalies.
- Perform data cleaning and preprocessing.
- Conduct exploratory data analysis (EDA).
- Build binary classification models to distinguish benign and malicious traffic.
- Develop multiclass classification models to identify different attack categories.
- Evaluate models using appropriate performance metrics.
- Perform clustering to explore network traffic patterns.
- Use explainable AI techniques to understand model predictions.

## 📊 Dataset

The project uses the **CIC-IDS2017 dataset**, which contains network traffic data representing benign activities and different types of cyberattacks.

The dataset includes network traffic features such as:

- Flow duration
- Protocol information
- Packet statistics
- Flow byte and packet rates
- Network traffic characteristics
- Attack labels

Due to the large size of the original dataset, raw and processed datasets are excluded from this GitHub repository.

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

### Model Explainability
- SHAP

### Development Environment
- Jupyter Notebook
- VS Code

### Additional Tools
- SQL
- Microsoft Excel
- Git
- GitHub

## 🔬 Project Workflow

1. **Data Understanding**
   - Dataset inspection
   - Data structure analysis
   - Data quality assessment

2. **Data Preprocessing**
   - Data cleaning
   - Missing value analysis
   - Duplicate analysis
   - Feature preparation

3. **Exploratory Data Analysis**
   - Attack distribution analysis
   - Traffic pattern analysis
   - Feature distributions
   - Correlation analysis
   - Statistical analysis

4. **Binary Classification**
   - Benign vs. malicious traffic classification
   - Model training
   - Performance evaluation

5. **Multiclass Classification**
   - Classification of network traffic into multiple attack categories
   - Model comparison
   - Performance evaluation

6. **Advanced Evaluation**
   - Confusion matrix analysis
   - Precision
   - Recall
   - F1-score
   - ROC-AUC analysis

7. **Clustering & Explainable AI**
   - K-Means clustering
   - Cluster analysis
   - PCA visualization
   - SHAP-based feature importance analysis

## 📁 Project Structure

```text
CyberThreat-AI/
│
├── data/
│   ├── raw/              # Original datasets (excluded from GitHub)
│   ├── processed/        # Cleaned datasets (excluded from GitHub)
│   └── sample/           # Sample dataset
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_binary_classification.ipynb
│   └── 04_multiclass_classification.ipynb
│
├── models/               # Trained machine learning models
│
├── reports/              # Analysis reports and evaluation results
│
├── src/                  # Python source code
│
├── excel/                # Excel-based analysis
│
├── sql/                  # SQL queries and views
│
├── README.md
├── requirements.txt
├── Dockerfile
└── .gitignore
```

## 🤖 Machine Learning Models

The project explores machine learning approaches for network traffic classification and analysis.

### Classification
- Logistic Regression
- Decision Tree
- Random Forest

### Clustering
- K-Means

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC

## 📈 Analysis & Results

The project includes:

- Exploratory analysis of network traffic.
- Identification of attack distributions and traffic patterns.
- Binary classification performance evaluation.
- Multiclass classification performance evaluation.
- Feature importance analysis.
- Misclassification analysis.
- Clustering-based traffic exploration.
- SHAP-based model interpretability.

Detailed results and visualizations are available in the `reports/` directory.

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CyberThreat-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory and execute them in sequence.

## 📂 Dataset Setup

The original CIC-IDS2017 dataset is not included in this repository because of its large file size.

Download the dataset from its official source and place the files in the appropriate directory under:

```text
data/raw/
```

Processed datasets should be stored under:

```text
data/processed/
```

## 🔮 Future Enhancements

- Develop a real-time network traffic monitoring system.
- Integrate a threat detection dashboard.
- Implement automated alert generation.
- Explore deep learning-based classification.
- Improve model generalization on unseen network traffic.
- Deploy the machine learning model through a web application or API.
- Integrate explainable AI insights into an interactive dashboard.

## 👩‍💻 Author

**Minu Mukesh K**

Master of Computer Applications (MCA)  
Data Science & Machine Learning

---

*CyberThreat-AI: Exploring network traffic through data analytics, machine learning, and explainable AI.*