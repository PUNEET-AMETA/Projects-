import pandas as pd
import numpy as np

class HRPreprocessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print(f"Dataset Loaded Successfully")
        print(f"Rows : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

        return self.df

    def dataset_info(self):

        print("\nDataset Information")
        print(self.df.info())

        print("\nMissing Values")
        print(self.df.isnull().sum())

        print("\nDuplicate Records")
        print(self.df.duplicated().sum())

    def remove_duplicates(self):

        before = self.df.shape[0]

        self.df.drop_duplicates(inplace=True)

        after = self.df.shape[0]

        print(f"Removed {before-after} duplicate rows")

    def check_outliers(self):

        numerical_columns = self.df.select_dtypes(
            include=['int64', 'float64']
        ).columns

        outlier_summary = {}

        for col in numerical_columns:

            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            count = self.df[
                (self.df[col] < lower) |
                (self.df[col] > upper)
            ].shape[0]

            outlier_summary[col] = count

        print("\nOutlier Summary")
        print(pd.DataFrame(
            outlier_summary.items(),
            columns=['Column', 'Outliers']
        ))

    def create_age_group(self):

        self.df['AgeGroup'] = pd.cut(
            self.df['Age'],
            bins=[18,25,35,45,55,65],
            labels=[
                '18-25',
                '26-35',
                '36-45',
                '46-55',
                '55+'
            ]
        )

    def create_salary_group(self):

        self.df['SalaryGroup'] = pd.cut(
            self.df['MonthlyIncome'],
            bins=[0,3000,7000,12000,20000],
            labels=[
                'Low',
                'Medium',
                'High',
                'Very High'
            ]
        )

    def create_tenure_group(self):

        self.df['TenureGroup'] = pd.cut(
            self.df['YearsAtCompany'],
            bins=[0,2,5,10,20,40],
            labels=[
                'New',
                'Junior',
                'Mid',
                'Senior',
                'Veteran'
            ]
        )

    def save_cleaned_data(self, output_path):

        self.df.to_csv(output_path, index=False)

        print(f"\nSaved Successfully : {output_path}")


if __name__ == "__main__":

    DATA_PATH = "Projects\HR Workforce Analytics Dashboard\data\raw\WA_Fn-UseC_-HR-Employee-Attrition.csv"

    OUTPUT_PATH = "Projects\HR Workforce Analytics Dashboard\data\processed\employee_cleaned.csv"

    processor = HRPreprocessor(DATA_PATH)

    processor.load_data()

    processor.dataset_info()

    processor.remove_duplicates()

    processor.check_outliers()

    processor.create_age_group()

    processor.create_salary_group()

    processor.create_tenure_group()

    processor.save_cleaned_data(OUTPUT_PATH)