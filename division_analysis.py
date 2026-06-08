def division_analysis(df):
    print("📊 Running Division-Level Analysis...\n")

    # -----------------------------
    # Aggregate metrics
    # -----------------------------
    division_df = df.groupby('Division').agg({
        'Sales': 'sum',
        'Gross Profit': 'sum',
        'Units': 'sum'
    }).reset_index()

    # -----------------------------
    # Calculate KPIs
    # -----------------------------
    division_df['Avg Margin %'] = (division_df['Gross Profit'] / division_df['Sales']) * 100
    division_df['Profit per Unit'] = division_df['Gross Profit'] / division_df['Units']

    print("✅ Division Analysis Completed!\n")

    return division_df

def classify_divisions(division_df):
    print("🧠 Classifying Divisions...\n")

    avg_margin = division_df['Avg Margin %'].mean()
    avg_profit = division_df['Gross Profit'].mean()

    def classify(row):
        if row['Avg Margin %'] >= avg_margin and row['Gross Profit'] >= avg_profit:
            return "High Efficiency"
        elif row['Avg Margin %'] < avg_margin and row['Gross Profit'] >= avg_profit:
            return "High Revenue but Low Margin"
        elif row['Avg Margin %'] >= avg_margin and row['Gross Profit'] < avg_profit:
            return "Efficient but Low Scale"
        else:
            return "Structural Margin Issue"

    division_df['Category'] = division_df.apply(classify, axis=1)

    print("✅ Division Classification Done!\n")

    return division_df