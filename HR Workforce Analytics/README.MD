# HR Workforce Analytics Dashboard 📊

An end-to-end HR Analytics and Employee Attrition Prediction project that combines **SQL, Python, Machine Learning, and Power BI** to analyze workforce trends, identify attrition drivers, segment employee risk, and provide actionable business recommendations.

---

## 🚀 Project Overview

Employee attrition is one of the most critical challenges faced by organizations. This project analyzes workforce data from **1,470 employees** to uncover factors influencing employee turnover and build predictive models that help HR teams proactively identify at-risk employees.

### Analytics Workflow

```text
Raw HR Dataset
    ↓
SQL Analysis
    ↓
Python EDA & Data Cleaning
    ↓
Feature Engineering
    ↓
Machine Learning Models
    ↓
Power BI Dashboard
    ↓
Business Insights & Recommendations
```

---

## 🎯 Objectives

* Analyze workforce demographics and employee behavior
* Identify key drivers of employee attrition
* Develop predictive models for attrition forecasting
* Create employee risk segmentation using custom risk scoring
* Build an executive-level Power BI dashboard
* Generate actionable retention recommendations

---

## 🛠️ Tech Stack

### Data Analysis

* Python
* Pandas
* NumPy
* SQL (MySQL)

### Visualization

* Power BI
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost

### Model Persistence

* Joblib

---

## 📊 Dataset Information

**Dataset:** IBM HR Analytics Employee Attrition Dataset

| Metric                   | Value     |
| ------------------------ | --------- |
| Total Employees          | 1,470     |
| Employee Attrition Count | 237       |
| Attrition Rate           | 16.12%    |
| Features                 | 35+       |
| Target Variable          | Attrition |

---

## 🧠 Feature Engineering

Created additional analytical features:

* Risk Score
* Risk Category
* Attrition Target
* Overtime Flag
* Satisfaction Level
* Age Groups
* Salary Groups
* Tenure Groups

---

## 🤖 Machine Learning Results

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression | 75.51%   | 36.56%    | 72.34% | 48.57%   | 0.7929  |
| Random Forest       | 83.33%   | 47.50%    | 40.43% | 43.68%   | 0.7955  |
| XGBoost             | 85.71%   | 64.71%    | 23.40% | 34.38%   | 0.7804  |

### Best Accuracy

🏆 XGBoost — 85.71%

### Best ROC-AUC

🏆 Random Forest — 0.7955

---

## 📈 Top Attrition Drivers

1. JobRole_Human Resources
2. OverTime_Yes
3. RiskScore
4. JobLevel
5. StockOptionLevel
6. JobRole_Sales Executive
7. Overtime_Flag
8. MaritalStatus_Single
9. Department_Sales
10. BusinessTravel_Travel_Frequently

---

## 💼 SQL Analysis

Business questions answered:

* What is the overall attrition rate?
* Which departments have the highest turnover?
* How does overtime impact attrition?
* Which job roles are most likely to leave?
* Does marital status affect retention?
* How does salary relate to attrition?

---

## 📊 Power BI Dashboard

### 1. Executive Overview

* Total Employees
* Attrition Count
* Attrition Rate
* Average Salary
* Average Satisfaction
* Average Tenure

### 2. Attrition Analysis

* Department-wise Attrition
* Job Role Attrition
* Overtime Impact
* Marital Status Analysis
* Business Travel Analysis

### 3. Workforce Insights

* Salary Distribution
* Years at Company Analysis
* Job Satisfaction Analysis
* Work-Life Balance Insights
* Stock Option Analysis

### 4. Risk Analysis

* Risk Category Distribution
* Risk Score Distribution
* High-Risk Employee Identification
* Department Risk Assessment

### 5. Machine Learning Insights

* Model Comparison
* Feature Importance
* Predictive Analytics Results
* Executive AI Insights

---

## 📌 Key Business Findings

### Overtime Increases Attrition Risk

Employees working overtime are significantly more likely to leave the organization.

### Sales Roles Show Elevated Turnover

Sales-related positions demonstrate higher attrition rates compared to other departments.

### Marital Status Influences Retention

Single employees exhibit higher attrition likelihood than married employees.

### Stock Options Improve Retention

Employees with higher stock option levels tend to stay longer.

### Risk Scoring Enables Early Intervention

Custom risk scoring effectively identifies employees requiring retention efforts.

---

## 📷 Dashboard Screenshots

### Executive Overview

![Executive Overview](screenshots/executive_overview.png)

### Attrition Analysis

![Attrition Analysis](screenshots/attrition_analysis.png)

### Workforce Insights

![Workforce Insights](screenshots/workforce_insights.png)

### Risk Analysis

![Risk Analysis](screenshots/risk_analysis.png)

### Machine Learning Insights

![ML Insights](screenshots/ml_insights.png)

---

## 🔮 Future Improvements

* Streamlit deployment
* Real-time workforce monitoring
* Employee retention recommendation engine
* Automated HR alerts
* SHAP explainability analysis

---

## 👨‍💻 Author

**Puneet Ameta**

* B.Tech Computer Science (AI & ML)
* Data Analytics | Machine Learning | Power BI | SQL
* LinkedIn: [www.linkedin.com/in/puneet-ameta-531a35324](http://www.linkedin.com/in/puneet-ameta-531a35324)

⭐ If you found this project useful, consider giving it a star.
