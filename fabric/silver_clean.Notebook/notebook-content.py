# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

from pyspark.sql import functions as F

bronze = spark.read.table("bronze_customers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Standardise names and postcodes, remove duplicates
silver = (
    bronze
    # Remove spaces at the start and end of customer_name 
    # so that " Ray" and "Ray" count as the same name when grouping or matching.
    .withColumn("customer_name", F.trim(F.col("customer_name")))
    # Convert postcode to uppercase so that "mn3 gh5" and "MN3 GH5" are treated as the same when grouping or matching.
    .withColumn("postcode", F.upper(F.col("postcode")))
    # Keep one row for each customer_id 
    # so that a customer is not counted twice when counting or adding up totals.
    .dropDuplicates(["customer_id"])
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

silver.write.mode("overwrite").saveAsTable("silver_customers")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
