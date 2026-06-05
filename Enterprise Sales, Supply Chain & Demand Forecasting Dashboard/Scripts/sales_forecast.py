import pandas as pd

df = pd.read_csv(r"...\data\cleaned_sales.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(pd.Grouper(key="Order Date", freq="MS"))
    ["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.to_csv(
    r"...\data/monthly_sales.csv",
    index=False
)

print(monthly_sales.head())