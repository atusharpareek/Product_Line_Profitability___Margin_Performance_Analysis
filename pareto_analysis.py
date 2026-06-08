def pareto_analysis(product_df):
    print("📊 Running Pareto Analysis...\n")

    # -----------------------------
    # Sort by Sales (Revenue Pareto)
    # -----------------------------
    revenue_df = product_df.sort_values(by='Sales', ascending=False).copy()
    revenue_df['Cumulative Revenue %'] = revenue_df['Sales'].cumsum() / revenue_df['Sales'].sum() * 100

    # -----------------------------
    # Sort by Profit (Profit Pareto)
    # -----------------------------
    profit_df = product_df.sort_values(by='Gross Profit', ascending=False).copy()
    profit_df['Cumulative Profit %'] = profit_df['Gross Profit'].cumsum() / profit_df['Gross Profit'].sum() * 100

    print("✅ Pareto Analysis Completed!\n")

    return revenue_df, profit_df

def dependency_analysis(product_df):
    print("⚠️ Checking Dependency Risk...\n")

    total_products = len(product_df)

    top_20_percent = int(0.2 * total_products)

    top_products = product_df.sort_values(by='Gross Profit', ascending=False).head(top_20_percent)

    contribution = top_products['Gross Profit'].sum() / product_df['Gross Profit'].sum() * 100

    print(f"Top {top_20_percent} products contribute {contribution:.2f}% of total profit")

    if contribution > 80:
        print("🚨 High dependency risk detected!")
    else:
        print("✅ Dependency is balanced")

    return contribution

def region_analysis(df):
    print("🌍 Running Region Analysis...\n")

    region_df = df.groupby('Region').agg({
        'Sales': 'sum',
        'Gross Profit': 'sum'
    }).reset_index()

    region_df['Revenue %'] = region_df['Sales'] / region_df['Sales'].sum() * 100

    print(region_df.sort_values(by='Sales', ascending=False))

    return region_df