# Databricks notebook source

# COMMAND ----------

dbutils.widgets.text("catalog", "nbcu", "Catalog Name")
dbutils.widgets.text("schema", "peacock", "Schema Name")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

# COMMAND ----------

spark.sql(f"""
INSERT INTO {catalog}.{schema}.viewership
SELECT uuid() AS view_id,
       u.user_id,
       s.show_id,
       current_date() AS view_date,
       CASE WHEN rand() < 0.1 THEN NULL ELSE cast(rand()*60 as int) END AS watch_time
FROM (
  SELECT user_id FROM {catalog}.{schema}.users ORDER BY rand() LIMIT 50
) u
CROSS JOIN (
  SELECT show_id FROM {catalog}.{schema}.shows ORDER BY rand() LIMIT 2
) s
LIMIT 100
""")
