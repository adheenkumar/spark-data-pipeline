import pandas as pd

def run_checks():
    df = pd.read_parquet("data/processed/taxi_data")

    assert len(df) > 0, "❌ No data found"
    assert df["trip_distance"].min() >= 0, "❌ Negative trip distance"
    assert df["trip_duration"].min() >= 0, "❌ Negative trip duration"
    assert df["tpep_pickup_datetime"].isnull().sum() == 0, "❌ Null pickup datetime"

    print("✅ Data quality checks passed")

if __name__ == "__main__":
    run_checks()