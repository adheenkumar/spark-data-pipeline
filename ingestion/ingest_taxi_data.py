import requests
import os

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

def ingest():
    os.makedirs("data/raw", exist_ok=True)
    file_path = "data/raw/yellow_tripdata.parquet"

    response = requests.get(URL)
    with open(file_path, "wb") as f:
        f.write(response.content)

    print("✅ Data ingestion completed")

if __name__ == "__main__":
    ingest()