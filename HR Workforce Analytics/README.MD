
HR Workforce Analytics Dashboard 📊

An end-to-end HR Analytics and Employee Attrition Prediction project that combines SQL, Python, Machine Learning, and Power BI to analyze workforce trends, identify attrition drivers, segment employee risk, and provide actionable business recommendations for HR decision-making.

🚀 Project Overview

Employee attrition is one of the most critical challenges faced by organizations. This project analyzes workforce data from 1,470 employees to uncover the factors influencing employee turnover and build predictive models that help HR teams proactively identify at-risk employees.

The project follows a complete analytics lifecycle:

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
🎯 Objectives
Analyze workforce demographics and employee behavior.
Identify key drivers of employee attrition.
Develop predictive models for attrition forecasting.
Create employee risk segmentation using custom risk scoring.
Build an executive-level Power BI dashboard.
Generate actionable retention recommendations.
🛠️ Tech Stack
Data Analysis
Python
Pandas
NumPy
SQL (MySQL)
Visualization
Power BI
Matplotlib
Seaborn
Machine Learning
Scikit-Learn
XGBoost
Model Persistence
Joblib
📂 Project Structure
HR Workforce Analytics Dashboard
│
├── data
│   ├── raw
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   │
│   └── processed
│       ├── employee_cleaned.csv
│       └── employee_model_ready.csv
│
├── models
│   ├── logistic.pkl
│   ├── random_forest.pkl
│   └── xgboost.pkl
│
├── reports
│   ├── feature_importance.csv
│   └── model_comparison.csv
│
├── sql
│   ├── 01_database_setup.sql
│   ├── 02_attrition_analysis.sql
│   ├── 03_department_analysis.sql
│   ├── 04_overtime_analysis.sql
│   ├── 05_salary_analysis.sql
│   └── 06_jobrole_analysis.sql
│
├── powerbi
│   └── HR_Workforce_Analytics.pbix
│
├── screenshots
│   ├── executive_overview.png
│   ├── attrition_analysis.png
│   ├── workforce_insights.png
│   ├── risk_analysis.png
│   └── ml_insights.png
│
├── src
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
│
└── README.md
📊 Dataset Information

Dataset: IBM HR Analytics Employee Attrition Dataset

Total Employees: 1,470
Features: 35+
Target Variable: Attrition
Employee Attrition Count: 237
Attrition Rate: 16.12%
🔍 Data Analysis
Exploratory Data Analysis

Performed:

Data quality assessment
Missing value analysis
Duplicate record detection
Outlier detection
Workforce demographic analysis
Attrition trend analysis
Workforce Metrics
Metric	Value
Total Employees	1,470
Attrition Count	237
Attrition Rate	16.12%
Avg Satisfaction	2.73
Avg Tenure	7.01 Years
🧠 Feature Engineering

Created additional analytical features:

Risk Score

Custom risk scoring based on:

Overtime
Job Satisfaction
Work-Life Balance
Years at Company
Promotion History
Risk Category
Low Risk
Medium Risk
High Risk
Employee Segmentation
Age Groups
Salary Groups
Tenure Groups
Additional Features
Attrition Target
Overtime Flag
Satisfaction Level
🤖 Machine Learning Models

Three machine learning algorithms were trained and evaluated:

Logistic Regression
Accuracy: 75.51%
Precision: 36.56%
Recall: 72.34%
F1 Score: 48.57%
ROC-AUC: 0.7929
Random Forest
Accuracy: 83.33%
Precision: 47.50%
Recall: 40.43%
F1 Score: 43.68%
ROC-AUC: 0.7955
XGBoost
Accuracy: 85.71%
Precision: 64.71%
Recall: 23.40%
F1 Score: 34.38%
ROC-AUC: 0.7804
Best Performing Model
Accuracy

🏆 XGBoost

Accuracy = 85.71%
ROC-AUC

🏆 Random Forest

ROC-AUC = 0.7955
📈 Feature Importance Analysis

Top drivers of employee attrition identified using XGBoost:

Rank	Feature
1	JobRole_Human Resources
2	OverTime_Yes
3	RiskScore
4	JobLevel
5	StockOptionLevel
6	JobRole_Sales Executive
7	Overtime_Flag
8	MaritalStatus_Single
9	Department_Sales
10	BusinessTravel_Travel_Frequently
💼 SQL Analysis

Business questions answered using SQL:

Attrition Analysis
What is the overall attrition rate?
Which departments have the highest turnover?
Workforce Insights
Salary comparison by attrition status
Overtime impact on attrition
Job role-wise attrition trends
Marital status analysis
HR KPIs
Headcount distribution
Department-wise employee count
Employee retention metrics
📊 Power BI Dashboard

The dashboard consists of 5 interactive pages:

1. Executive Overview
Total Employees
Attrition Count
Attrition Rate
Average Salary
Average Satisfaction
Average Tenure
2. Attrition Analysis
Department-wise Attrition
Job Role Attrition
Overtime Impact
Marital Status Analysis
Business Travel Analysis
3. Workforce Insights
Salary Distribution
Years at Company Analysis
Job Satisfaction Analysis
Work-Life Balance Insights
Stock Option Analysis
4. Risk Analysis
Risk Category Distribution
Risk Score Distribution
High-Risk Employee Identification
Department Risk Assessment
5. Machine Learning Insights
Model Comparison
Feature Importance
Predictive Analytics Results
Executive AI Insights
📌 Key Business Findings
Overtime Increases Attrition Risk

Employees working overtime are significantly more likely to leave the organization.

Sales Roles Show Elevated Turnover

Sales-related positions demonstrate higher attrition rates compared to other departments.

Marital Status Influences Retention

Single employees exhibit higher attrition likelihood than married employees.

Stock Options Improve Retention

Employees with higher stock option levels tend to stay longer.

Risk Scoring Enables Early Intervention

Custom risk scoring effectively identifies employees requiring retention efforts.

📷 Dashboard Screenshots
Executive Overview

Attrition Analysis

Workforce Insights

Risk Analysis

Machine Learning Insights

🔮 Future Improvements
Deploy model using Streamlit
Real-time workforce monitoring
Employee retention recommendation engine
Automated HR alerts for high-risk employees
Advanced explainable AI (SHAP Analysis)
👨‍💻 Author

Puneet Ameta

B.Tech Computer Science (AI & ML)
Data Analytics | Machine Learning | Power BI | SQL
LinkedIn: www.linkedin.com/in/puneet-ameta-531a35324
