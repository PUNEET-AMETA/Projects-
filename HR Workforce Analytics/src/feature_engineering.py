import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

class FeatureEngineer:

    def __init__(self, input_path):
        self.input_path = input_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        print("Data Loaded")
        return self.df

    def encode_target(self):

        self.df["Attrition_Target"] = self.df["Attrition"].map(
            {
                "Yes": 1,
                "No": 0
            }
        )

    def create_overtime_flag(self):

        self.df["Overtime_Flag"] = self.df["OverTime"].map(
            {
                "Yes": 1,
                "No": 0
            }
        )

    def create_satisfaction_level(self):

        conditions = [
            self.df["JobSatisfaction"] <= 2,
            self.df["JobSatisfaction"] == 3,
            self.df["JobSatisfaction"] == 4
        ]

        values = [
            "Low",
            "Medium",
            "High"
        ]

        self.df["Satisfaction_Level"] = np.select(
            conditions,
            values,
            default="Unknown"
        )

    def create_risk_score(self):

        score = 0

        score += self.df["Overtime_Flag"] * 30

        score += np.where(
            self.df["JobSatisfaction"] <= 2,
            25,
            0
        )

        score += np.where(
            self.df["WorkLifeBalance"] <= 2,
            20,
            0
        )

        score += np.where(
            self.df["MonthlyIncome"] < self.df["MonthlyIncome"].median(),
            15,
            0
        )

        score += np.where(
            self.df["YearsAtCompany"] < 3,
            10,
            0
        )

        self.df["RiskScore"] = score

    def create_risk_category(self):

        self.df["RiskCategory"] = pd.cut(
            self.df["RiskScore"],
            bins=[0, 30, 60, 100],
            labels=[
                "Low",
                "Medium",
                "High"
            ]
        )

    def encode_features(self):

        categorical_columns = [
            "BusinessTravel",
            "Department",
            "EducationField",
            "Gender",
            "JobRole",
            "MaritalStatus",
            "OverTime"
        ]

        self.df = pd.get_dummies(
            self.df,
            columns=categorical_columns,
            drop_first=True
        )

    def save_dataset(self, output_path):

        self.df.to_csv(
            output_path,
            index=False
        )

        print("Model Ready Dataset Saved")

if __name__ == "__main__":

    INPUT_PATH = "Projects\HR Workforce Analytics Dashboard\data\processed\employee_cleaned.csv"

    OUTPUT_PATH = "Projects\HR Workforce Analytics Dashboard\data\processed\employee_model_ready.csv"

    fe = FeatureEngineer(INPUT_PATH)

    fe.load_data()

    fe.encode_target()

    fe.create_overtime_flag()

    fe.create_satisfaction_level()

    fe.create_risk_score()

    fe.create_risk_category()

    fe.encode_features()

    fe.save_dataset(OUTPUT_PATH)