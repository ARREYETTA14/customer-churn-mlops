from pathlib import Path

import pandas as pd


# --------------------------------------------------
# 1. Define the location of the raw dataset
# --------------------------------------------------

DATA_FILE = Path(r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\raw\customerspro.csv")


# --------------------------------------------------
# 2. Define the columns that must exist
# --------------------------------------------------

REQUIRED_COLUMNS = [
    "customer_id",
    "age",
    "salary",
    "tenure_months",
    "monthly_charges",
    "contract_type",
    "internet_service",
    "churn",
]


# --------------------------------------------------
# 3. Check that the file exists
# --------------------------------------------------

if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_FILE}"
    )


# --------------------------------------------------
# 4. Load the dataset
# --------------------------------------------------

df = pd.read_csv(DATA_FILE)


# --------------------------------------------------
# 5. Check that the dataset is not empty
# --------------------------------------------------

if df.empty:
    raise ValueError("The dataset is empty.")


# --------------------------------------------------
# 6. Check required columns
# --------------------------------------------------

missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# --------------------------------------------------
# 7. Check for duplicate customer IDs
# --------------------------------------------------

if df["customer_id"].duplicated().any():
    raise ValueError(
        "Duplicate customer IDs found."
    )


# --------------------------------------------------
# 8. Check for missing values
# --------------------------------------------------

missing_values = df[REQUIRED_COLUMNS].isnull().sum()

if missing_values.any():
    print("Missing values found:")
    print(missing_values[missing_values > 0])


# --------------------------------------------------
# 9. Validate age
# --------------------------------------------------

if (df["age"] <= 0).any():
    raise ValueError(
        "Invalid age detected."
    )


# --------------------------------------------------
# 10. Validate salary
# --------------------------------------------------

if (df["salary"] < 0).any():
    raise ValueError(
        "Invalid salary detected."
    )


# --------------------------------------------------
# 11. Validate tenure
# --------------------------------------------------

if (df["tenure_months"] < 0).any():
    raise ValueError(
        "Invalid tenure value detected."
    )


# --------------------------------------------------
# 12. Validate churn values
# --------------------------------------------------

allowed_churn_values = {"Yes", "No"}

invalid_churn_values = set(df["churn"].unique()) - allowed_churn_values

if invalid_churn_values:
    raise ValueError(
        f"Invalid churn values found: {invalid_churn_values}"
    )


# --------------------------------------------------
# 13. Print successful validation
# --------------------------------------------------

print("Data validation completed successfully.")

print(f"Number of rows: {len(df)}")

print(f"Number of columns: {len(df.columns)}")