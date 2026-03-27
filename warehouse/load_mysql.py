import pandas as pd
import mysql.connector
import time


def get_connection():
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root",
                database="taxi_db",
                port=3306,
                ssl_disabled=True
            )
            print("Connected to MySQL")
            return conn
        except Exception:
            print(f"Retry {i+1}: waiting for MySQL...")
            time.sleep(3)

    raise Exception("Could not connect to MySQL after retries")


def load():
    print("Connecting to MySQL...")

    conn = get_connection()
    cursor = conn.cursor()

    print("Ensuring table exists...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS taxi_trips (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pickup_datetime DATETIME,
            dropoff_datetime DATETIME,
            trip_distance FLOAT
        )
    """)

    print("Reading processed data...")
    df = pd.read_parquet("data/processed/taxi_data")

    if df.empty:
        print("No data found. Skipping load.")
        return

    df = df[[
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance"
    ]]

    print(f"Rows to insert: {len(df)}")

    data = [
        (
            row["tpep_pickup_datetime"],
            row["tpep_dropoff_datetime"],
            float(row["trip_distance"])
        )
        for _, row in df.head(5000).iterrows()
    ]

    print("Inserting data into MySQL...")

    cursor.executemany(
        """
        INSERT INTO taxi_trips (pickup_datetime, dropoff_datetime, trip_distance)
        VALUES (%s, %s, %s)
        """,
        data
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into MySQL successfully")


if __name__ == "__main__":
    load()