import pandas as pd

df = pd.read_csv(r"...\data\archive\Global_Superstore2.csv", encoding='latin-1')


print("Total Revenue:", df["Sales"].sum())

print("Total Profit:", df["Profit"].sum())

print(
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)