def product_level_analysis(df):
    print("📊 Running Product-Level Analysis...\n")

    # -----------------------------
    # Aggregate at Product Level
    # -----------------------------
    product_df = df.groupby('Product Name').agg({
        'Sales': 'sum',
        'Gross Profit': 'sum',
        'Units': 'sum'
    }).reset_index()

    # -----------------------------
    # Recalculate KPIs at product level
    # -----------------------------
    product_df['Gross Margin %'] = (product_df['Gross Profit'] / product_df['Sales']) * 100
    product_df['Profit per Unit'] = product_df['Gross Profit'] / product_df['Units']

    # -----------------------------
    # Ranking
    # -----------------------------
    product_df = product_df.sort_values(by='Gross Profit', ascending=False)
    # Add ranking columns
    product_df['Profit Rank'] = product_df['Gross Profit'].rank(ascending=False)
    product_df['Margin Rank'] = product_df['Gross Margin %'].rank(ascending=False)
    print("✅ Product Analysis Completed!\n")

    return product_df


def advanced_classification(product_df):
    print("🧠 Advanced Product Classification...\n")

    avg_sales = product_df['Sales'].mean()
    avg_margin = product_df['Gross Margin %'].mean()

    def classify(row):
        if row['Sales'] >= avg_sales and row['Gross Margin %'] >= avg_margin:
            return "High Sales & High Margin"
        elif row['Sales'] >= avg_sales and row['Gross Margin %'] < avg_margin:
            return "High Sales but Low Margin"
        elif row['Sales'] < avg_sales and row['Gross Margin %'] >= avg_margin:
            return "Low Sales but High Margin"
        else:
            return "Low Sales & Low Profit"

    product_df['Business Category'] = product_df.apply(classify, axis=1)

    print("✅ Advanced Classification Done!\n")

    return product_df