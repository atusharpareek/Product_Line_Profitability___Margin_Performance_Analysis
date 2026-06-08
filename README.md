Product Line Profitability & Margin Performance Analysis
Nassau Candy Distributor
📌 Project Overview

This project focuses on analyzing product-level profitability, gross margin performance, and division-wise financial efficiency for Nassau Candy Distributor. While sales volume is often used as a primary performance indicator, it does not always reflect actual profitability. Some products generate high revenue but contribute little profit due to high manufacturing or operational costs.

The objective of this project is to identify the products, divisions, regions, and states that drive profitability, detect margin risks, and provide actionable recommendations for pricing, sourcing, and portfolio optimization. The project also includes an interactive Streamlit dashboard for real-time business intelligence and decision support.

🎯 Problem Statement

Nassau Candy Distributor lacks visibility into:

Which products generate the highest profit and gross margin.
Whether high-sales products are truly profitable.
How profitability varies across divisions.
Which products pose margin risks due to excessive costs.

Without these insights, pricing decisions, promotional strategies, and product portfolio management remain reactive rather than data-driven.

🎯 Objectives
Analyze product-level profitability and gross margins.
Identify high-performing and underperforming products.
Evaluate division-wise revenue and profit contributions.
Perform cost structure diagnostics.
Analyze profit concentration using Pareto principles.
Study regional and state-level sales performance.
Build an interactive Streamlit dashboard for business users.
📊 Dataset Description

The dataset contains order-level transactional records including:

Column	Description
Row ID	Unique record identifier
Order ID	Unique order number
Order Date	Date of order placement
Ship Date	Shipment date
Ship Mode	Shipping method
Customer ID	Customer identifier
Country/Region	Customer region
City	Customer city
State/Province	Customer state
Postal Code	ZIP code
Division	Product division
Region	Sales region
Product ID	Product identifier
Product Name	Product name
Sales	Revenue generated
Units	Quantity sold
Gross Profit	Profit earned
Cost	Manufacturing cost
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Streamlit
📈 Analytical Methodology
1. Data Cleaning & Validation
Removed invalid records.
Validated Sales, Cost, and Profit values.
Handled missing values.
Standardized product and division names.
2. KPI Engineering

Calculated key business metrics:

Gross Margin (%)
Profit per Unit
Revenue Contribution
Profit Contribution
3. Product Profitability Analysis
Ranked products by Sales.
Ranked products by Gross Profit.
Identified high-profit and low-margin products.
4. Division Performance Analysis

Compared:

Revenue contribution by division
Profit contribution by division
Average gross margin
5. Cost Structure Diagnostics

Analyzed:

Sales vs Cost relationship
Cost-heavy products
Margin-poor products
6. Geographic Performance Analysis

Evaluated:

Region-wise profitability
State-wise sales contribution
7. Time-Series Analysis

Studied sales trends over time to identify growth patterns and seasonal fluctuations.

8. Correlation Analysis

Measured relationships between:

Sales
Cost
Units
Gross Profit
⚠️ Why K-Means Clustering Was Not Used

Although clustering techniques such as K-Means are commonly used for customer or product segmentation, they were not implemented in this project.

The dataset primarily consists of transactional profitability metrics with a limited number of product categories and clearly interpretable business dimensions. The project's goal was to perform profitability and margin analysis rather than behavioral segmentation.

Applying K-Means clustering would not have provided meaningful business value because:

Product categories were already predefined.
Clear profitability patterns were observable through descriptive analytics.
Business decisions could be directly supported using KPI-based analysis.

Therefore, emphasis was placed on actionable profitability insights rather than artificial cluster generation.

📊 Key Findings
Product Performance
Wonka Bar – Scrumdiddlyumptious generated the highest gross profit.
Wonka Bar – Triple Dazzle Caramel generated the highest sales revenue.
Several products generated significant revenue but lower profit contributions.
Division Analysis
Chocolate division dominates both sales and profitability.
Sugar division contributes comparatively lower revenue.
Other division demonstrates margin variability.
Profitability Analysis
Gross margins are concentrated around 65–72%.
Profitability strongly correlates with sales performance.
Geographic Analysis
Pacific region generates the highest profit contribution.
California leads overall sales performance.
New York and Texas are also major revenue contributors.
Correlation Analysis

Strong positive correlations were observed:

Variables	Correlation
Sales vs Gross Profit	0.98
Sales vs Cost	0.96
Units vs Gross Profit	0.82
📌 Business Recommendations
Prioritize high-margin products for promotion and expansion.
Reassess low-margin products despite high sales volume.
Monitor product profitability continuously.
Diversify revenue sources to reduce dependency on a few products.
Expand distribution efforts in high-performing regions.
📱 Streamlit Dashboard

The project includes an interactive Streamlit dashboard providing:

Product Profitability Dashboard
Product margin leaderboard
Profit contribution analysis
Product search functionality
Division Performance Dashboard
Revenue vs Profit comparison
Margin distribution by division
Cost & Margin Diagnostics
Sales vs Cost analysis
Margin risk identification
Geographic Analytics
Region-wise profitability
State-level sales performance
Trend Analysis
Sales over time
Profitability monitoring
User Controls
Date Range Filter
Division Filter
Margin Threshold Slider
Product Search
🚀 Run Locally

Clone the repository:

git clone https://github.com/yourusername/nassau-candy-profitability-analysis.git

Navigate to project directory:

cd nassau-candy-profitability-analysis

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py

Application URL:

http://localhost:8501/
📂 Project Structure
├── data/
│   └── Nassau_Candy_Dataset.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── dashboard/
│   └── app.py
│
├── reports/
│   └── Research_Paper.pdf
│
├── images/
│   └── dashboard_screenshots
│
├── requirements.txt
└── README.md
🔮 Future Scope

Future enhancements may include predictive profit forecasting, machine learning-based demand estimation, real-time ERP integration, automated margin monitoring, supply chain optimization, and advanced customer segmentation to support strategic decision-making and improve overall business profitability.

📄 Research Paper

The complete project report containing methodology, visualizations, insights, recommendations, and dashboard explanation is included in the repository.

👨‍💻 Author

Tushar Pareek
