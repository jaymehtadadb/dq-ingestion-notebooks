# Databricks notebook source
### test

# COMMAND ----------

dbutils.widgets.text("catalog", "nbcu", "Catalog Name")
dbutils.widgets.text("schema", "peacock", "Schema Name")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

# COMMAND ----------

spark.sql(f"""
INSERT INTO {catalog}.{schema}.users
SELECT uuid() AS user_id,
       CASE WHEN rand() < 0.1 THEN NULL ELSE concat('User_', n) END AS user_name,
       CASE WHEN rand() < 0.1 THEN NULL ELSE concat('user', n, '@example.com') END AS email,
       CASE WHEN rand() < 0.2 THEN NULL ELSE CASE WHEN rand() > 0.5 THEN 'Premium' ELSE 'Basic' END END AS subscription_type,
       current_date() AS join_date
FROM (SELECT explode(sequence(1, 50)) AS n)
""")