import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Load monthly sales
df = pd.read_csv(r"...\data\monthly_sales.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Time Features
df["Month_Num"] = df["Order Date"].dt.month
df["Quarter"] = df["Order Date"].dt.quarter

# Lag Features
df["Lag_1"] = df["Sales"].shift(1)

# Rolling Average
df["Rolling_3"] = (
    df["Sales"]
    .rolling(window=3)
    .mean()
    .shift(1)
)

# Remove null rows
df = df.dropna().reset_index(drop=True)

# Features
X = df[
    [
        "Month_Num",
        "Quarter",
        "Lag_1",
        "Rolling_3"
    ]
]

y = df["Sales"]

# Train Model
model = RandomForestRegressor(
    n_estimators=500,
    max_depth=8,
    random_state=42
)

model.fit(X, y)

# ---------------------------
# Forecast Next 6 Months
# ---------------------------

future_predictions = []

last_sales = list(df["Sales"].tail(3))

last_date = df["Order Date"].max()

for i in range(6):

    future_date = last_date + pd.DateOffset(months=i+1)

    month_num = future_date.month
    quarter = future_date.quarter

    lag_1 = last_sales[-1]

    rolling_3 = np.mean(last_sales[-3:])

    future_row = pd.DataFrame({
        "Month_Num":[month_num],
        "Quarter":[quarter],
        "Lag_1":[lag_1],
        "Rolling_3":[rolling_3]
    })

    prediction = model.predict(future_row)[0]

    future_predictions.append(
        {
            "Date": future_date,
            "Predicted_Sales": prediction
        }
    )

    last_sales.append(prediction)

forecast = pd.DataFrame(future_predictions)

forecast.to_csv(
    r"...\data\random_forest_forecast.csv",
    index=False
)

print(forecast)