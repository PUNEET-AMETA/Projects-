import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(r"...\data\cleaned_sales.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

results = []

for category in df["Category"].unique():

    cat_df = df[df["Category"] == category]

    monthly = (
        cat_df
        .groupby(pd.Grouper(
            key="Order Date",
            freq="MS"
        ))["Sales"]
        .sum()
        .reset_index()
    )

    monthly["Month_Num"] = monthly["Order Date"].dt.month
    monthly["Quarter"] = monthly["Order Date"].dt.quarter

    monthly["Lag_1"] = monthly["Sales"].shift(1)

    monthly["Rolling_3"] = (
        monthly["Sales"]
        .rolling(3)
        .mean()
        .shift(1)
    )

    monthly = monthly.dropna()

    X = monthly[
        [
            "Month_Num",
            "Quarter",
            "Lag_1",
            "Rolling_3"
        ]
    ]

    y = monthly["Sales"]

    model = RandomForestRegressor(
        n_estimators=500,
        random_state=42
    )

    model.fit(X, y)

    history = list(monthly["Sales"].tail(3))

    last_date = monthly["Order Date"].max()

    for i in range(6):

        future_date = (
            last_date +
            pd.DateOffset(months=i+1)
        )

        row = pd.DataFrame({
            "Month_Num":[future_date.month],
            "Quarter":[future_date.quarter],
            "Lag_1":[history[-1]],
            "Rolling_3":[np.mean(history[-3:])]
        })

        pred = model.predict(row)[0]

        results.append({
            "Date": future_date,
            "Category": category,
            "Predicted_Sales": pred
        })

        history.append(pred)

forecast_df = pd.DataFrame(results)

forecast_df.to_csv(
    r"...data/category_forecast.csv",
    index=False
)

print(forecast_df.head())