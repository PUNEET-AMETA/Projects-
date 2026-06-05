import pandas as pd

historical = pd.read_csv(r"..0\data\monthly_sales.csv")

forecast = pd.read_csv(r"...\data\random_forest_forecast.csv")

historical["Date"] = pd.to_datetime(historical["Order Date"])

historical = historical[
    ["Date","Sales"]
]

historical["Type"] = "Historical"

forecast["Date"] = pd.to_datetime(
    forecast["Date"]
)

forecast = forecast.rename(
    columns={
        "Predicted_Sales":"Sales"
    }
)

forecast["Type"] = "Forecast"

combined = pd.concat(
    [
        historical,
        forecast
    ],
    ignore_index=True
)

combined = combined.sort_values(
    "Date"
)

combined.to_csv(
    r"...\data\historical_forecast_combined.csv",
    index=False
)

print(combined.tail(15))