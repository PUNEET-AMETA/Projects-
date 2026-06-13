import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

# ==========================
# Load Dataset
# ==========================

DATA_PATH = "\Projects\HR Workforce Analytics Dashboard\data\processed\employee_model_ready.csv"

df = pd.read_csv(DATA_PATH)

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
    include=["int64", "float64", "uint8", "bool"]
)

y = df["Attrition_Target"]

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
# Load Models
# ==========================

MODELS_DIR = "Projects\HR Workforce Analytics Dashboard\models"

models = {
    "Logistic Regression":
        joblib.load(f"{MODELS_DIR}\\logistic.pkl"),

    "Random Forest":
        joblib.load(f"{MODELS_DIR}\\random_forest.pkl"),

    "XGBoost":
        joblib.load(f"{MODELS_DIR}\\xgboost.pkl")
}

results = []

# ==========================
# Evaluate
# ==========================

for name, model in models.items():

    pred = model.predict(X_test)

    prob = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, pred)

    prec = precision_score(y_test, pred)

    rec = recall_score(y_test, pred)

    f1 = f1_score(y_test, pred)

    auc = roc_auc_score(y_test, prob)

    print(f"\n{name}")

    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall   : {rec:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC AUC  : {auc:.4f}")

    print("\nConfusion Matrix")

    print(confusion_matrix(y_test, pred))

    results.append([
        name,
        acc,
        prec,
        rec,
        f1,
        auc
    ])

# ==========================
# Save Results
# ==========================

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1Score",
        "ROCAUC"
    ]
)

results_df.to_csv(
    "Projects\HR Workforce Analytics Dashboard\reports\model_comparison.csv",
    index=False
)

print("\nModel Comparison Saved")