import pandas as pd

DATA_PATH ="Projects\HR Workforce Analytics Dashboard\data\processed\employee_cleaned.csv"

df = pd.read_csv(DATA_PATH)

def recommendation(row):

    recommendations = []

    if row["OverTime"] == "Yes":
        recommendations.append(
            "Reduce Overtime"
        )

    if row["JobSatisfaction"] <= 2:
        recommendations.append(
            "Manager Feedback Session"
        )

    if row["WorkLifeBalance"] <= 2:
        recommendations.append(
            "Flexible Work Arrangement"
        )

    if row["MonthlyIncome"] < df["MonthlyIncome"].median():
        recommendations.append(
            "Compensation Review"
        )

    if len(recommendations) == 0:
        recommendations.append(
            "No Immediate Action Needed"
        )

    return ", ".join(recommendations)

df["RetentionRecommendation"] = df.apply(
    recommendation,
    axis=1
)

OUTPUT_PATH = "Projects\HR Workforce Analytics Dashboard\data\processed\retention_recommendations.csv"

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("Recommendations Generated")