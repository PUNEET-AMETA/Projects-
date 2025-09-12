# 🏪 Retail Insights Dashboard

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

**Author:** Puneet  Ameta 👨‍💻  
**Project Type:** Database Normalization & Business Intelligence Dashboard 📊  

---


## 🎯 Project Overview

This project demonstrates comprehensive data analytics skills through database normalization and business intelligence visualization. Using a retail store dataset, the project transforms raw transactional data into a normalized database structure and creates insightful visualizations for business decision-making.

### ✨ Key Features
- 🗄️ **Database Normalization**: Transform denormalized retail data into proper relational structure
- 🚀 **Data Optimization**: Achieve significant storage reduction through normalization
- 📈 **Business Intelligence**: Create meaningful visualizations for strategic insights
- ⚡ **Performance Analysis**: Implement efficient database design with proper indexing

---

## 📋 Key Objectives

| Objective | Description | Status |
|-----------|-------------|--------|
| 🏗️ Database Normalization | Transform denormalized retail data into proper relational database structure | ✅ |
| 💾 Data Optimization | Achieve significant storage reduction through normalization | ✅ |
| 📊 Business Intelligence | Create meaningful visualizations for strategic business insights | ✅ |
| ⚡ Performance Analysis | Implement efficient database design with proper indexing and foreign keys | ✅ |

---

## 📦 Dataset Description

The project uses a comprehensive retail store dataset containing:

- 📋 **Order Information**: Order IDs, dates, shipping details
- 👥 **Customer Data**: Customer demographics and segmentation  
- 🛍️ **Product Details**: Categories, subcategories, product specifications
- 🗺️ **Geographic Data**: Regional distribution across US states and cities
- 💰 **Financial Metrics**: Sales, profit, discount, and quantity data

### 📊 Dataset Stats
- **Total Data Points**: 209,874 📈
- **Original Attributes**: 21 columns 📝
- **Normalized Tables**: 5 optimized tables 🗃️

---

## 🏗️ Database Schema

### 📉 Original Structure
```
🔸 Raw Data: Single denormalized table with 21 attributes
🔸 Data Points: 209,874 total data points
```

### 🚀 Normalized Structure
The database is normalized into 5 optimized tables:

| Table | Description | Icon |
|-------|-------------|------|
| `customers` | Customer information and segmentation | 👥 |
| `locations` | Geographic data with unique location identifiers | 📍 |
| `products` | Product catalog with categories and subcategories | 🛍️ |
| `orders` | Order header information with foreign key relationships | 📋 |
| `order_items` | Order line items (junction table) | 📦 |

### 🔗 Entity Relationship Diagram
The project includes a comprehensive ER diagram showing:
- 🔑 Primary and foreign key relationships
- 📊 Table dependencies and constraints  
- ⚡ Optimized data structure for query performance

---

## 📊 Key Visualizations & Insights

### 1. 🛍️ Product Category Analysis
- **🥇 Technology Leadership**: Technology category leads with $836K in sales
- **💡 Profit Margin Insights**: Office Supplies shows more stable profitability
- **🎯 Strategic Value**: Guides product portfolio optimization

### 2. 🗺️ Regional Performance Dashboard
- **🌟 West Region Excellence**: 31.6% of total sales with 14.9% profit margin
- **📈 Geographic Opportunities**: California, New York, and Texas lead in sales
- **⚡ Operational Efficiency**: East and West regions show superior profit margins

### 3. 👥 Customer Segment Analytics
- **🎯 Consumer Dominance**: 51.6% of customers contributing highest sales ($1.16M)
- **💼 Home Office Premium**: Smallest segment (18.7%) with highest average order value ($241)
- **📊 Segmentation Strategy**: Clear behavioral differences require differentiated approaches

### 4. 📅 Temporal Analysis
- **🎄 Seasonal Patterns**: Clear sales peaks at year-end periods
- **📈 Growth Trajectory**: Significant growth in late 2017
- **🔗 Sales-Profit Correlation**: Strong correlation of 0.716 between sales and profit

---

## 🧠 Business Intelligence Outcomes

### 💡 Strategic Insights
- **🎯 Market Focus**: Technology products drive revenue, Office Supplies drive margins
- **🌍 Regional Strategy**: West region represents most valuable market  
- **👥 Customer Strategy**: Balance consumer volume with home office premium segments

### ⚙️ Operational Benefits
- **📦 Inventory Management**: Data-driven guidance for product allocation
- **📢 Marketing Optimization**: Regional and segment-specific campaign targeting
- **💰 Financial Planning**: Seasonal pattern recognition for cash flow management

---

## 🛠️ Technologies Used

| Technology | Purpose | Badge |
|------------|---------|-------|
| MySQL | Database Management | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white) |
| Python | Data Processing & Analysis | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| pandas | Data Manipulation | ![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white) |
| numpy | Numerical Computing | ![NumPy](https://img.shields.io/badge/numpy-013243?style=flat&logo=numpy&logoColor=white) |
| matplotlib | Static Visualizations | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat) |
| seaborn | Statistical Visualizations | ![seaborn](https://img.shields.io/badge/seaborn-388E3C?style=flat) |
| plotly | Interactive Visualizations | ![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat&logo=plotly&logoColor=white) |

---

## 📈 Analysis Highlights

### 📊 Quantitative Results

| Metric | Value | Category |
|--------|-------|----------|
| Technology Sales | $836K | 🥇 Top Category |
| West Region Share | 31.6% | 🌟 Leading Region |
| Consumer Segment | 51.6% | 👥 Largest Group |
| Home Office AOV | $241 | 💼 Premium Value |
| Sales-Profit Correlation | 0.716 | 🔗 Strong Link |

### 🎯 Strategic Recommendations

#### 🛍️ Product Portfolio
- Balance high-volume technology sales with high-margin office supplies
- Focus on cross-selling opportunities between categories

#### 🌍 Geographic Expansion  
- Focus investment in West region while exploring East region opportunities
- Develop targeted strategies for underperforming regions

#### 👥 Customer Acquisition
- Differentiated strategies for consumer volume vs. home office premium segments
- Implement loyalty programs for high-value customers

---


## 📁 Project Structure

```
📦 MySQL-Python-Data-Analytics
├── 📄 README.md
├── 📊 data/
│   ├── raw_data.csv
│   └── normalized_tables/
├── 🐍 scripts/
│   ├── normalize_database.py
│   ├── create_dashboard.py
│   └── analysis.py
├── 📈 visualizations/
│   ├── category_analysis.png
│   ├── regional_dashboard.png
│   └── customer_segments.png
└── 📋 documentation/
    ├── ER_diagram.png
    └── project_report.pdf
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. 🍴 Fork the Project
2. 🌟 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 👨‍💻 Author

**Puneet Ameta**
- 📧 Email: ametapuneet04@gmail.com

- 🐙 GitHub: https://github.com/PUNEET-AMETA

---

## 🙏 Acknowledgments

- Thanks to the open-source community for amazing libraries
- Special thanks to contributors and reviewers


---

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

<div align="center">

**📊 Transforming Data into Insights 📈**

</div>
