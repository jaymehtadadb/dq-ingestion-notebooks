# DQ Ingestion - Databricks Asset Bundle

A Databricks Asset Bundle (DAB) that orchestrates data ingestion for Users, Shows, and Viewership tables using parameterized notebooks sourced from this Git repo.

## Bundle Structure

```
├── databricks.yml                      # Main bundle config with variables and targets
├── resources/
│   └── dabs_demo_job.yml               # Job definition with task dependencies
├── data_ingestion_users.py             # Notebook: insert 50 mock users
├── data_ingestion_shows.py             # Notebook: insert 50 mock shows
└── data_ingestion_viewership.py        # Notebook: insert 100 mock viewership records
```

## Job Task Dependencies

```
users → shows → viewership
```

All three tasks run as notebook tasks sourced from this Git repo. The job passes `catalog` and `schema` parameters to each notebook.

## Parameters

| Parameter | Default | Description |
|---|---|---|
| `catalog` | `nbcu` | Unity Catalog name |
| `schema` | `peacock` | Schema name |

## Deploy

```bash
# Validate
databricks bundle validate

# Deploy to dev (default)
databricks bundle deploy

# Deploy to prod
databricks bundle deploy -t prod

# Run the job
databricks bundle run DABs_Demo
```
