# DBT Ingestion

**Initializing the project**

1. Install `direnv`
2. Setup `.envrc` file with the following

```
export DBT_PROFILES_DIR=./.dbt
export DBT_GCP_PROJECT=<GCP_PROJECT>
export DBT_GCP_DATASET=<GCP_DATASET> # this variable will be the prefix for all dbt models created => ex: ua, dbt; will also be used as default dataset if no schema is defined
export DBT_GCP_KEYFILE=<GCP_KEYFILE>
```

