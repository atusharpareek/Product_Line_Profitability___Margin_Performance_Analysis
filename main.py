import pandas as pd
from data_cleaning import clean_data
from analysis import calculate_kpis
from product_analysis import product_level_analysis
from product_analysis import advanced_classification
from division_analysis import division_analysis
from division_analysis import classify_divisions
from pareto_analysis import pareto_analysis
from pareto_analysis import dependency_analysis
from pareto_analysis import region_analysis
from cost_analysis import cost_structure_analysis
from cost_analysis import plot_cost_vs_sales
from cost_analysis import recommend_actions

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


if __name__ == "__main__":
    file_path = "nassau_data.csv"

    df = load_data(file_path)

    if df is not None:
        print("\n🔍 Before Cleaning Shape:", df.shape)

        df = clean_data(df)

        print("🔍 After Cleaning Shape:", df.shape)

        print("\n🔍 Cleaned Data Preview:")
        print("\n❗ Any negative profit?")
        print((df['Gross Profit'] < 0).sum())

        print("\n📦 Unique Divisions:")
        print(df['Division'].unique())

        # KPI calculation
        df = calculate_kpis(df)

        print("\n📊 KPI Preview:")
        print(df[['Product Name', 'Sales', 'Gross Profit',
                  'Gross Margin %', 'Profit per Unit',
                  'Profit Contribution', 'Profit Contribution_final']].head())

        product_df = product_level_analysis(df)

        print("\n🏆 Top 5 Products by Profit:")
        print(product_df.head())

        print("\n⚠️ Bottom 5 Products by Profit:")
        print(product_df.tail())

        product_df = advanced_classification(product_df)

        print("\n📊 Business Categories:")
        print(product_df[['Product Name', 'Business Category']])

        division_df = division_analysis(df)

        print("\n📊 Division Performance:")
        print(division_df)

        division_df = classify_divisions(division_df)

        print("\n📊 Division Categories:")
        print(division_df[['Division', 'Category']])

        revenue_df, profit_df = pareto_analysis(product_df)

        # -----------------------------
        # Top contributors (80%)
        # -----------------------------
        top_revenue = revenue_df[revenue_df['Cumulative Revenue %'] <= 80]
        top_profit = profit_df[profit_df['Cumulative Profit %'] <= 80]

        print("\n💰 Products contributing to 80% Revenue:")
        print(top_revenue[['Product Name', 'Cumulative Revenue %']])

        print("\n🏆 Products contributing to 80% Profit:")
        print(top_profit[['Product Name', 'Cumulative Profit %']])

        dependency_analysis(product_df)
        region_df = region_analysis(df)

        product_df = cost_structure_analysis(product_df)

        print("\n📊 Cost Diagnostics:")
        print(product_df[['Product Name', 'Cost %', 'Gross Margin %', 'Cost Category']])

        product_df = recommend_actions(product_df)

        print("\n📌 Final Cost Recommendations:")
        print(product_df[['Product Name', 'Cost Category', 'Recommended Action']])

        plot_cost_vs_sales(product_df)

        from src.eda import (
            eda_distributions,
            eda_product_division,
            eda_relationships,
            eda_time_region
        )

        eda_distributions(df)
        eda_product_division(df)
        eda_relationships(df)
        eda_time_region(df)
