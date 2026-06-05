import pandas as pd

df = pd.read_csv(r"...\data\archive\Global_Superstore2.csv", encoding='latin1')

print("Shape:", df.shape)

df.columns = df.columns.str.strip()

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
) * 100

print(df.head())

df.to_csv(
    "../data/cleaned_sales.csv",
    index=False
)

print("Cleaning Complete")