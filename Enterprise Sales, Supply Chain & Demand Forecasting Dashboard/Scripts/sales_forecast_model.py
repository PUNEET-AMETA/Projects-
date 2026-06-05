import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv(r"...\data\cleaned_sales.csv")

df["Month"] = np.arange(len(df))

X = df[["Month"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

future_months = pd.DataFrame({
    "Month": np.arange(len(df), len(df) + 6)
})

future_sales = model.predict(future_months)

forecast = pd.DataFrame({
    "Forecast_Month": range(1, 7),
    "Predicted_Sales": future_sales
})

forecast.to_csv(
    r"C:\Users\Ameta\Desktop\10 LPA\Projects\AI-Powered Sales Intelligence Platform\data//sales_forecast.csv",
    index=False
)

print(forecast)