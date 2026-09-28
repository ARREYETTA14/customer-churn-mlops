from pathlib import Path

import pandas as pd  # type: ignore[reportMissingModuleSource]


# --------------------------------------------------
# 1. Define input and output locations
# --------------------------------------------------

INPUT_FILE = Path(r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\raw\customerspro.csv")

OUTPUT_FILE = Path(
    r"C:\Users\WORLD COMPUTERS\Downloads\MLops Project 1\Customer Churn Data Pipeline\data\processed\customers_cleaned.csv"
)


# --------------------------------------------------
# 2. Load the raw dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("Raw dataset loaded.")

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")


# --------------------------------------------------
# 3. Remove duplicate customers
# --------------------------------------------------

before_duplicates = len(df)

df = df.drop_duplicates(
    subset="customer_id"
)

after_duplicates = len(df)

duplicates_removed = (
    before_duplicates - after_duplicates
)

print(
    f"Duplicate rows removed: "
    f"{duplicates_removed}"
)


# --------------------------------------------------
# 4. Clean text columns
# --------------------------------------------------

text_columns = [
    "contract_type",
    "internet_service",
    "churn",
]

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# --------------------------------------------------
# 5. Convert numeric columns
# --------------------------------------------------

numeric_columns = [
    "age",
    "salary",
    "tenure_months",
    "monthly_charges",
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# --------------------------------------------------
# 6. Handle missing numeric values
# --------------------------------------------------

for column in numeric_columns:

    median_value = df[column].median()

    df[column] = df[column].fillna(
        median_value
    )


# --------------------------------------------------
# 7. Handle missing categorical values
# --------------------------------------------------

categorical_columns = [
    "contract_type",
    "internet_service",
    "churn",
]

for column in categorical_columns:

    df[column] = df[column].fillna(
        "Unknown"
    )


# --------------------------------------------------
# 8. Remove impossible values
# --------------------------------------------------

df = df[df["age"] > 0]

df = df[df["salary"] >= 0]

df = df[df["tenure_months"] >= 0]

df = df[df["monthly_charges"] >= 0]


# --------------------------------------------------
# 9. Create output directory if necessary
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------------------------
# 10. Save cleaned dataset
# --------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("Data processing completed.")

print(
    f"Cleaned dataset saved to: "
    f"{OUTPUT_FILE}"
)

print(f"Final rows: {len(df)}")
print(f"Final columns: {len(df.columns)}")