def cost_structure_analysis(product_df):
    print("📊 Running Cost Structure Diagnostics...\n")

    # -----------------------------
    # Add Cost (recalculate from original df logic)
    # -----------------------------
    # Cost = Sales - Profit
    product_df['Total Cost'] = product_df['Sales'] - product_df['Gross Profit']

    # -----------------------------
    # Cost-to-Sales Ratio
    # -----------------------------
    product_df['Cost %'] = (product_df['Total Cost'] / product_df['Sales']) * 100

    # -----------------------------
    # Classification Logic
    # -----------------------------
    avg_margin = product_df['Gross Margin %'].mean()
    avg_cost = product_df['Cost %'].mean()

    def classify(row):
        if row['Cost %'] > avg_cost and row['Gross Margin %'] < avg_margin:
            return "❌ Cost Heavy & Low Margin"
        elif row['Cost %'] > avg_cost and row['Gross Margin %'] >= avg_margin:
            return "⚠️ High Cost but Good Margin"
        elif row['Cost %'] <= avg_cost and row['Gross Margin %'] < avg_margin:
            return "⚠️ Pricing Issue"
        else:
            return "✅ Healthy Product"

    product_df['Cost Category'] = product_df.apply(classify, axis=1)

    print("✅ Cost Analysis Completed!\n")

    return product_df

def recommend_actions(product_df):
    print("🧠 Generating Recommendations...\n")

    def action(row):
        if row['Cost Category'] == "❌ Cost Heavy & Low Margin":
            return "Discontinue or Renegotiate Cost"
        elif row['Cost Category'] == "⚠️ Pricing Issue":
            return "Increase Price"
        elif row['Cost Category'] == "⚠️ High Cost but Good Margin":
            return "Optimize Cost"
        else:
            return "Maintain & Scale"

    product_df['Recommended Action'] = product_df.apply(action, axis=1)

    print("✅ Recommendations Generated!\n")

    return product_df

import matplotlib.pyplot as plt

def plot_cost_vs_sales(product_df):
    plt.figure()
    plt.scatter(product_df['Sales'], product_df['Total Cost'])

    plt.xlabel("Sales")
    plt.ylabel("Cost")
    plt.title("Cost vs Sales Analysis")

    plt.show()