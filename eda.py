# SECTION 1: DISTRIBUTIONS

import matplotlib.pyplot as plt
import seaborn as sns

def eda_distributions(df):
    print("📊 Running Distribution Analysis...")

    # 1. Sales Distribution
    plt.figure()
    sns.histplot(df['Sales'], kde=True)
    plt.title("Sales Distribution")
    plt.show()

    # 2. Profit Distribution
    plt.figure()
    sns.histplot(df['Gross Profit'], kde=True)
    plt.title("Profit Distribution")
    plt.show()

    # 3. Units Distribution
    plt.figure()
    sns.histplot(df['Units'], kde=True)
    plt.title("Units Distribution")
    plt.show()

    # 4. Margin Distribution
    plt.figure()
    sns.histplot(df['Gross Margin %'], kde=True)
    plt.title("Margin Distribution")
    plt.show()

# SECTION 2: PRODUCT & DIVISION
def eda_product_division(df):
    print("📊 Product & Division Analysis...")

    # 5. Top 10 Products by Sales
    top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10)
    plt.figure()
    top_products.plot(kind='bar')
    plt.title("Top 10 Products by Sales")
    plt.show()

    # 6. Top 10 Products by Profit
    top_profit = df.groupby('Product Name')['Gross Profit'].sum().nlargest(10)
    plt.figure()
    top_profit.plot(kind='bar')
    plt.title("Top 10 Products by Profit")
    plt.show()

    # 7. Division-wise Sales
    plt.figure()
    df.groupby('Division')['Sales'].sum().plot(kind='bar')
    plt.title("Sales by Division")
    plt.show()

    # 8. Division-wise Margin
    plt.figure()
    df.groupby('Division')['Gross Margin %'].mean().plot(kind='bar')
    plt.title("Average Margin by Division")
    plt.show()

# SECTION 3: RELATIONSHIPS
def eda_relationships(df):
    print("📊 Relationship Analysis...")

    # 9. Sales vs Profit
    plt.figure()
    sns.scatterplot(x='Sales', y='Gross Profit', data=df)
    plt.title("Sales vs Profit")
    plt.show()

    # 10. Sales vs Cost
    plt.figure()
    sns.scatterplot(x='Sales', y='Cost', data=df)
    plt.title("Sales vs Cost")
    plt.show()

    # 11. Units vs Profit
    plt.figure()
    sns.scatterplot(x='Units', y='Gross Profit', data=df)
    plt.title("Units vs Profit")
    plt.show()

    # 12. Correlation Heatmap
    plt.figure()
    sns.heatmap(df[['Sales','Cost','Units','Gross Profit']].corr(), annot=True)
    plt.title("Correlation Matrix")
    plt.show()

# SECTION 4: TIME & REGION
def eda_time_region(df):
    print("📊 Time & Region Analysis...")

    # 13. Sales over time
    time_df = df.groupby('Order Date')['Sales'].sum()
    plt.figure()
    time_df.plot()
    plt.title("Sales Over Time")
    plt.show()

    # 14. Profit by Region
    plt.figure()
    df.groupby('Region')['Gross Profit'].sum().plot(kind='bar')
    plt.title("Profit by Region")
    plt.show()

    # 15. Sales by State (Top 10)
    top_states = df.groupby('State/Province')['Sales'].sum().nlargest(10)
    plt.figure()
    top_states.plot(kind='bar')
    plt.title("Top States by Sales")
    plt.show()
