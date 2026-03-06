# Databricks notebook source

# COMMAND ----------

dbutils.widgets.text("catalog", "nbcu", "Catalog Name")
dbutils.widgets.text("schema", "peacock", "Schema Name")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

# COMMAND ----------

spark.sql(f"""
INSERT INTO {catalog}.{schema}.shows
SELECT uuid() AS show_id,
       CASE WHEN rand() < 0.1 THEN NULL ELSE concat('Show_', n) END AS show_name,
       CASE WHEN rand() < 0.2 THEN NULL ELSE CASE WHEN rand() > 0.5 THEN 'Comedy' ELSE 'Drama' END END AS genre,
       current_date() AS release_date,
       CASE WHEN rand() < 0.1 THEN NULL ELSE cast(rand()*60 as int) END AS duration
FROM (SELECT explode(sequence(1, 50)) AS n)
""")
