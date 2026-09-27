"""Customer Churn & Retention Analytics
Reproducible analysis of the IBM Telco Customer Churn dataset.
"""

import pandas as pd

DATA_PATH = "data/Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

# Data quality
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
print("Rows:", len(df))
print("Missing TotalCharges:", df["TotalCharges"].isna().sum())

# Numeric churn flag
df["ChurnFlag"] = df["Churn"].map({"Yes": 1, "No": 0})

# Tenure cohorts
bins = [-1, 12, 24, 48, 60, float("inf")]
labels = ["0-12 months", "13-24 months", "25-48 months", "49-60 months", "61+ months"]
df["TenureGroup"] = pd.cut(df["tenure"], bins=bins, labels=labels)

def churn_summary(column):
    out = (
        df.groupby(column, observed=False)["ChurnFlag"]
          .agg(Customers="size", ChurnRate="mean")
          .reset_index()
    )
    out["ChurnRate"] = (out["ChurnRate"] * 100).round(1)
    return out.sort_values("ChurnRate", ascending=False)

print("\nOverall churn rate (%):", round(df["ChurnFlag"].mean() * 100, 2))
print("\nChurn by contract")
print(churn_summary("Contract"))
print("\nChurn by internet service")
print(churn_summary("InternetService"))
print("\nChurn by payment method")
print(churn_summary("PaymentMethod"))
print("\nChurn by tenure cohort")
print(churn_summary("TenureGroup"))
