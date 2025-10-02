# DBT Ingestion

**Initializing the project**

1. Install `direnv`
2. Setup `.envrc` file with the following

```
export DBT_PROFILES_DIR=./.dbt
export DBT_GCP_PROJECT=<GCP_PROJECT>
export DBT_GCP_DATASET=<GCP_DATASET>
export DBT_GCP_KEYFILE=<GCP_KEYFILE>
```

