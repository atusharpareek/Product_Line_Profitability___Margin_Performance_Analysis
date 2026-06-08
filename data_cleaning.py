import pandas as pd


def clean_data(df):
    print("🧹 Starting Data Cleaning...\n")

    # -----------------------------
    # Convert date columns
    # -----------------------------
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

    # -----------------------------
    # Validate Sales & Cost
    # -----------------------------
    df = df[(df['Sales'] > 0) & (df['Cost'] >= 0)]

    # -----------------------------
    # Validate Gross Profit
    # -----------------------------
    df = df[df['Gross Profit'].notnull()]

    # -----------------------------
    # Handle missing Units
    # -----------------------------
    df['Units'] = df['Units'].fillna(0)

    # Remove zero or negative units
    df = df[df['Units'] > 0]

    # -----------------------------
    # Remove inconsistent profit rows
    # (Sales - Cost should roughly match Gross Profit)
    # -----------------------------
    df['calculated_profit'] = df['Sales'] - df['Cost']

    df = df[abs(df['calculated_profit'] - df['Gross Profit']) < 0.01]

    df.drop(columns=['calculated_profit'], inplace=True)

    # -----------------------------
    # Standardize text columns
    # -----------------------------
    df['Product Name'] = df['Product Name'].str.strip().str.title()
    df['Division'] = df['Division'].str.strip().str.title()

    # -----------------------------
    # Remove duplicates
    # -----------------------------
    df = df.drop_duplicates()

    print("✅ Data Cleaning Completed!\n")

    return df
