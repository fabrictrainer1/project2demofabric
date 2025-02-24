# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d1b22d00-491e-4134-a11d-d15e81b3a00b",
# META       "default_lakehouse_name": "data_lakehouse",
# META       "default_lakehouse_workspace_id": "17adc9c6-b14f-487d-a679-8e2a4a56a0df"
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/bronze/sales.csv")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
