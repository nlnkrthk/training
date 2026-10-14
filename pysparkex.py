from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyFirstSparkApp") \
    .getOrCreate()

print("Spark started successfully")

spark.stop()