from pathlib import Path

import pandas as pd


# --------------------------------------------------
# 1. Define input and output files
# --------------------------------------------------

INPUT_FILE = Path(
    r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\processed\customers_cleaned.csv"
)

OUTPUT_FILE = Path(
    r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\processed\customers_processed.csv"
)


# --------------------------------------------------
# 2. Load cleaned data
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Cleaned dataset loaded.")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")


# --------------------------------------------------
# 3. Create annual charges
# --------------------------------------------------

df["annual_charges"] = (
    df["monthly_charges"] * 12
)


# --------------------------------------------------
# 4. Create estimated total charges
# --------------------------------------------------

df["estimated_total_charges"] = (
    df["monthly_charges"]
    * df["tenure_months"]
)


# --------------------------------------------------
# 5. Create customer age groups
# --------------------------------------------------

def classify_age(age):

    if age < 30:
        return "young"

    elif age < 50:
        return "middle"

    else:
        return "senior"


df["age_group"] = df["age"].apply(
    classify_age
)


# --------------------------------------------------
# 6. Create tenure groups
# --------------------------------------------------

def classify_tenure(tenure):

    if tenure < 12:
        return "new"

    elif tenure < 36:
        return "established"

    else:
        return "long_term"


df["tenure_group"] = df[
    "tenure_months"
].apply(
    classify_tenure
)


# --------------------------------------------------
# 7. Convert churn to numerical value
# --------------------------------------------------

df["churn_flag"] = df["churn"].map(
    {
        "No": 0,
        "Yes": 1,
    }
)


# --------------------------------------------------
# 8. Create high monthly charge indicator
# --------------------------------------------------

average_monthly_charge = (
    df["monthly_charges"].mean()
)

df["high_monthly_charge"] = (
    df["monthly_charges"]
    > average_monthly_charge
).astype(int)


# --------------------------------------------------
# 9. Save processed dataset
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

PARQUET_FILE = Path(
    r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\processed\customers_processed.parquet"
)

df.to_parquet(
    PARQUET_FILE,
    index=False
)

print("Feature engineering completed.")

print(
    f"Processed dataset saved to: "
    f"{OUTPUT_FILE}"
)

print(
    f"Parquet dataset saved to: "
    f"{PARQUET_FILE}"
)


print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")

print("\nFinal columns:")

for column in df.columns:
    print(f"- {column}")