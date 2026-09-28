from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "customerspro.csv"

PROCESSED_FILE = BASE_DIR / "data" / "processed" / "customers_processed.csv"


def test_raw_file_exists():

    assert RAW_FILE.exists()


def test_processed_file_exists():

    assert PROCESSED_FILE.exists()


def test_processed_dataset_not_empty():

    df = pd.read_csv(PROCESSED_FILE)

    assert not df.empty


def test_required_columns_exist():

    df = pd.read_csv(PROCESSED_FILE)

    required_columns = [
        "customer_id",
        "age",
        "salary",
        "tenure_months",
        "monthly_charges",
        "contract_type",
        "internet_service",
        "churn",
        "annual_charges",
        "estimated_total_charges",
        "age_group",
        "tenure_group",
        "churn_flag",
        "high_monthly_charge",
    ]

    for column in required_columns:

        assert column in df.columns


def test_customer_ids_are_unique():

    df = pd.read_csv(PROCESSED_FILE)

    assert df["customer_id"].is_unique


def test_churn_flag_is_valid():

    df = pd.read_csv(PROCESSED_FILE)

    assert set(
        df["churn_flag"].unique()
    ).issubset({0, 1})


def test_age_is_positive():

    df = pd.read_csv(PROCESSED_FILE)

    assert (
        df["age"] > 0
    ).all()


def test_salary_is_not_negative():

    df = pd.read_csv(PROCESSED_FILE)

    assert (
        df["salary"] >= 0
    ).all()
