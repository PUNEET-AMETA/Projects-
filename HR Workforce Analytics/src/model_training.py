import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

# ==========================
# Load Data
# ==========================

DATA_PATH = "Projects\HR Workforce Analytics Dashboard\data\processed\employee_model_ready.csv"

df = pd.read_csv(DATA_PATH)

# ==========================
# Feature Selection
# ==========================

X = df.drop(
    columns=[
        "Attrition",
        "Attrition_Target",
        "AgeGroup",
        "SalaryGroup",
        "TenureGroup",
        "Satisfaction_Level",
        "RiskCategory",
        "Over18"
    ],
    errors="ignore"
)

X = X.select_dtypes(
    include=[
        "int64",
        "float64",
        "uint8",
        "bool"
    ]
)

y = df["Attrition_Target"]

print(f"Features Used: {X.shape[1]}")
print(f"Samples: {X.shape[0]}")

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Models
# ==========================

lr = LogisticRegression(
    max_iter=5000,
    class_weight="balanced"
)

rf = RandomForestClassifier(
    n_estimators=500,
    max_depth=10,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

xgb = XGBClassifier(
    n_estimators=500,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="logloss",
    random_state=42
)

# ==========================
# Training
# ==========================

print("\nTraining Logistic Regression...")
lr.fit(X_train, y_train)

print("Training Random Forest...")
rf.fit(X_train, y_train)

print("Training XGBoost...")
xgb.fit(X_train, y_train)

# ==========================
# Save Models
# ==========================

MODELS_DIR = "Projects\HR Workforce Analytics Dashboard\models"

joblib.dump(
    lr,
    rf"{MODELS_DIR}\logistic.pkl"
)

joblib.dump(
    rf,
    rf"{MODELS_DIR}\random_forest.pkl"
)

joblib.dump(
    xgb,
    rf"{MODELS_DIR}\xgboost.pkl"
)

print("\nModels Saved Successfully")

# ==========================
# Feature Importance
# ==========================

importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": xgb.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 15 Important Features")
print(importance.head(15))

importance.to_csv(
    "Projects\HR Workforce Analytics Dashboard\reports\feature_importance.csv",
    index=False
)

print("\nFeature Importance Report Saved")
print("\nTraining Complete")