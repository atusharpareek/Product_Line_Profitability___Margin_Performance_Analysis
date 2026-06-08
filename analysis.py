def calculate_kpis(df):
    print("📊 Calculating KPIs...\n")

    # -----------------------------
    # 1. Gross Margin (%)
    # -----------------------------
    df['Gross Margin %'] = df['Gross Profit'] / df['Sales']

    # -----------------------------
    # 2. Profit per Unit
    # -----------------------------
    df['Profit per Unit'] = df['Gross Profit'] / df['Units']

    # -----------------------------
    # 3. Total Profit Contribution
    # -----------------------------
    total_profit = df['Gross Profit'].sum()
    df['Gross Margin %'] = df['Gross Margin %'] * 100
    df['Profit Contribution'] = df['Gross Profit'] / total_profit
    df['Profit Contribution_final'] = df['Profit Contribution'] * 100
    print("✅ KPI Calculation Completed!\n")

    return df