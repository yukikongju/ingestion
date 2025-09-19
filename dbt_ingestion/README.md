# DBT Ingestion

The goal of this project is to test the following dbt behavior:
- CRON
    * Populate the data daily with `dbt run`
- CI/CD
    * Pointing directly tables to dev/staging/prod based on branch name
    * Unable to push to dev/staging/prod directly, need to make PR
- Python Models
    * Be able to run python code inside dbt
- DBT
    * Incremental Tables
    * Cumulative Tables



