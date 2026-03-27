from prefect import flow, task
import subprocess

@task
def ingest():
    subprocess.run(["python", "ingestion/ingest_taxi_data.py"])

@task
def transform():
    subprocess.run(["python", "transformation/spark_transform.py"])

@task
def quality():
    subprocess.run(["python", "quality/data_quality.py"])

@task
def load():
    subprocess.run(["python", "warehouse/load_mysql.py"])

@flow
def taxi_pipeline():
    ingest()
    transform()
    quality()
    load()

if __name__ == "__main__":
    taxi_pipeline()