# Customer 360 Dashboard

Customer Analytics and Segmentation platform built using **Python, Machine Learning, Power BI, and Data Analytics** to create a complete **Customer 360 View** from retail transaction data.

The project performs data cleaning, customer behavior analysis, RFM segmentation, clustering, and interactive dashboard visualization to generate actionable business insights.

---

## Project Overview

This project helps organizations understand customer purchasing behavior and improve business decision-making using analytics and machine learning.

### Workflow

```text
Raw Retail Data
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
RFM Analysis
       ↓
Customer Segmentation
       ↓
K-Means Clustering
       ↓
Power BI Dashboard
       ↓
Business Insights
```

---

## Features

### Data Processing

- Missing value handling
- Duplicate record removal
- Invalid transaction filtering
- Revenue calculation
- Data preprocessing pipeline

### Exploratory Data Analysis

- Revenue trend analysis
- Top-performing countries
- Product performance insights
- Purchase distribution patterns

### RFM Customer Analysis

Customer classification based on:

| Metric | Description |
|---------|-------------|
| Recency | How recently a customer purchased |
| Frequency | How often a customer purchases |
| Monetary | Total spending by customer |

Generated customer groups:

- VIP Customers
- Loyal Customers
- Regular Customers
- At-Risk Customers

---

## Machine Learning Pipeline

### Customer Segmentation using K-Means Clustering

Pipeline:

1. Feature Engineering
2. Data Scaling using `StandardScaler`
3. Cluster Optimization (Elbow Method)
4. K-Means Model Training
5. Cluster Assignment
6. Cluster Visualization

Output:

- Customer Cluster Labels
- Behavioral Segmentation
- Business Intelligence Insights

---

## Power BI Dashboard

Interactive dashboard developed for business monitoring and decision support.

### Dashboard Components

#### KPI Metrics

- Total Revenue
- Total Customers
- Total Orders
- Average Revenue

#### Business Visualizations

- Revenue Trend Over Time
- Revenue by Country
- Product Performance Analysis
- Customer Cluster Distribution
- RFM Scatter Visualization

#### Interactive Filtering

Dashboard supports dynamic filtering by:

- Country
- Customer Segment
- Customer Cluster
- Time Period

---

## Tech Stack

### Programming Language

- Python

### Libraries

```text
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
```

### Visualization

- Power BI

### Development Environment

- Jupyter Notebook

---

## Project Structure

```text
Customer360Dashboard/
│
├── data/
│   ├── online-retail-dataset.csv
│   ├── cleaned_retail.csv
│   ├── customer360_final.csv
│   └── rfm_customers.csv
│
├── customer360.ipynb
├── FINAL DASHBOARD.pbix
├── README.md
└── requirements.txt
```

---

## Dashboard Insights

The system provides insights into:

- Customer purchasing behavior
- Revenue growth trends
- Product demand patterns
- Geographic revenue distribution
- Customer retention opportunities
- Customer segmentation performance

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/Customer360Dashboard.git
```

Move into project directory:

```bash
cd Customer360Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
customer360.ipynb
```

---

## Output Files

### `customer360_final.csv`

Contains:

- Revenue calculations
- Customer information
- Cluster labels
- Segmentation results

### `rfm_customers.csv`

Contains:

- Recency score
- Frequency score
- Monetary score
- Customer cluster
- Segment category

### `FINAL DASHBOARD.pbix`

Interactive Power BI analytics dashboard.

---

## Business Impact

This solution enables organizations to:

- Identify high-value customers
- Improve customer retention
- Detect churn-risk customers
- Personalize marketing campaigns
- Optimize CRM strategies
- Support data-driven decision making

---

## Future Improvements

- Streamlit deployment
- Real-time analytics pipeline
- Churn prediction model
- Recommendation engine
- Customer lifetime value prediction
- AI-powered insight generation

---

## Author

**Puneet Ameta**  
Bachelor of Technology — Computer Science Engineering (AI & ML)

### Skills

Python • Machine Learning • Data Analytics • SQL • Power BI • Artificial Intelligence

LinkedIn:

www.linkedin.com/in/puneet-ameta-531a35324

---

If you found this project useful, consider giving it a star.
