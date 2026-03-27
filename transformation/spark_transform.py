from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month
from pyspark.sql.functions import unix_timestamp, col

spark = SparkSession.builder.appName("TaxiTransform").getOrCreate()

input_path = "data/raw/yellow_tripdata.parquet"
output_path = "data/processed/taxi_data"

df = spark.read.parquet(input_path)

# Data cleaning
df = df.dropna(subset=["tpep_pickup_datetime"])

# Feature engineering
df = df.withColumn(
    "trip_duration",
    (
        unix_timestamp(col("tpep_dropoff_datetime")) -
        unix_timestamp(col("tpep_pickup_datetime"))
    ) / 60
)

df = df.filter(col("trip_duration") > 0)

# Partition columns
df = df.withColumn("year", year("tpep_pickup_datetime"))
df = df.withColumn("month", month("tpep_pickup_datetime"))

# Write partitioned parquet
df.write.mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet(output_path)

print("✅ Transformation completed")

spark.stop()