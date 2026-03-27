# Spark Data Pipeline

# Data Engineering Pipeline

End-to-end pipeline using Spark, MySQL, Prefect, and GitLab CI/CD.

## Features
- Data ingestion (Python)
- Spark transformations (partitioned parquet)
- Data quality checks
- MySQL warehouse
- Dashboard (Superset)
- CI/CD automation

## Run
docker-compose up  
python orchestration/prefect_pipeline.py