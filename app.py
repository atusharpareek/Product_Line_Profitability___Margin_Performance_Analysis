import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_cleaning import clean_data
from src.analysis import calculate_kpis
from src.product_analysis import product_level_analysis, advanced_classification
from src.division_analysis import division_analysis, classify_divisions
from src.pareto_analysis import pareto_analysis
from src.cost_analysis import cost_structure_analysis, recommend_actions

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(layout="wide")
st.title("📊 Nassau Candy Profitability Dashboard")

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Nassau Candy Distributor.csv")
    df = clean_data(df)
    df = calculate_kpis(df)
    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

# Date filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['Order Date'].min(), df['Order Date'].max()]
)

# Division filter
division_filter = st.sidebar.multiselect(
    "Select Division",
    options=df['Division'].unique(),
    default=df['Division'].unique()
)

# Margin slider
margin_filter = st.sidebar.slider(
    "Minimum Margin %",
    0.0, 100.0, 0.0
)

# Product search
product_search = st.sidebar.text_input("Search Product")

# Apply filters
df = df[
    (df['Division'].isin(division_filter)) &
    (df['Gross Margin %'] >= margin_filter)
]

df = df[
    (df['Order Date'] >= pd.to_datetime(date_range[0])) &
    (df['Order Date'] <= pd.to_datetime(date_range[1]))
]

if product_search:
    df = df[df['Product Name'].str.contains(product_search, case=False)]

# -----------------------------
# PRODUCT ANALYSIS
# -----------------------------
product_df = product_level_analysis(df)
product_df = advanced_classification(product_df)

st.header("📦 Product Profitability Overview")

# Leaderboard
st.subheader("🏆 Top Products by Margin")
top_margin = product_df.sort_values(by='Gross Margin %', ascending=False).head(10)
st.dataframe(top_margin)

# Profit contribution chart
fig = px.bar(product_df.head(10), x='Product Name', y='Gross Profit',
             title="Top 10 Products by Profit")
st.plotly_chart(fig)

st.subheader("🧠 Product Insights")

top_product = product_df.iloc[0]['Product Name']
low_product = product_df.iloc[-1]['Product Name']

st.info(f"Top performing product is **{top_product}**, contributing highest profit.")

st.warning(f"Low-performing product is **{low_product}**, contributing minimal profit.")

st.success("Recommendation: Focus on scaling top-performing products and review low-performing ones for discontinuation or improvement.")

# -----------------------------
# DIVISION ANALYSIS
# -----------------------------
division_df = division_analysis(df)
division_df = classify_divisions(division_df)

st.header("🏢 Division Performance")

# Revenue vs Profit
fig2 = px.bar(division_df, x='Division', y=['Sales', 'Gross Profit'],
              barmode='group', title="Revenue vs Profit by Division")
st.plotly_chart(fig2)

# Margin distribution
fig3 = px.bar(division_df, x='Division', y='Avg Margin %',
              title="Margin % by Division")
st.plotly_chart(fig3)

st.subheader("🧠 Division Insights")

best_div = division_df.sort_values(by='Gross Profit', ascending=False).iloc[0]['Division']
worst_div = division_df.sort_values(by='Avg Margin %').iloc[0]['Division']

st.info(f"**{best_div}** division is the most profitable.")

st.warning(f"**{worst_div}** division has the lowest margin and may have structural inefficiencies.")

st.success("Recommendation: Invest in high-performing divisions and optimize cost structure in weaker divisions.")

# -----------------------------
# COST ANALYSIS
# -----------------------------
product_df = cost_structure_analysis(product_df)
product_df = recommend_actions(product_df)

st.header("💸 Cost vs Margin Diagnostics")

# Scatter plot
fig4 = px.scatter(product_df, x='Sales', y='Total Cost',
                  color='Cost Category',
                  title="Cost vs Sales Scatter")
st.plotly_chart(fig4)

# Risk table
st.subheader("⚠️ Margin Risk Products")
risk_products = product_df[product_df['Cost Category'] != "✅ Healthy Product"]
st.dataframe(risk_products[['Product Name', 'Cost Category', 'Recommended Action']])

st.subheader("🧠 Cost Insights")

risky = product_df[product_df['Cost Category'] == "❌ Cost Heavy & Low Margin"]

if not risky.empty:
    st.warning("Some products are cost-heavy and low-margin, indicating inefficiency.")

st.success("Recommendation: Consider cost renegotiation or discontinuation for inefficient products.")

# -----------------------------
# PARETO ANALYSIS
# -----------------------------
revenue_df, profit_df = pareto_analysis(product_df)

st.header("📊 Profit Concentration (Pareto)")

# Revenue Pareto
fig5 = px.line(revenue_df, x='Product Name', y='Cumulative Revenue %',
               title="Cumulative Revenue %")
st.plotly_chart(fig5)

# Profit Pareto
fig6 = px.line(profit_df, x='Product Name', y='Cumulative Profit %',
               title="Cumulative Profit %")
st.plotly_chart(fig6)

# Dependency indicator
top_20 = int(0.2 * len(product_df))
top_products = product_df.sort_values(by='Gross Profit', ascending=False).head(top_20)
dependency = top_products['Gross Profit'].sum() / product_df['Gross Profit'].sum() * 100

st.metric("📌 Top 20% Products Contribution", f"{dependency:.2f}%")

st.subheader("🧠 Pareto Insights")

st.info("A small number of products contribute to the majority of revenue and profit.")

if dependency > 80:
    st.warning("High dependency on a few products — business risk is high.")
else:
    st.success("Revenue and profit are well distributed — dependency risk is low.")

st.success("Recommendation: Maintain diversification and avoid over-reliance on a few products.")
# ----------------------------------------------------------------------------------------------------

