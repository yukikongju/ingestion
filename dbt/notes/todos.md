# Todos

Tables:
- `source_dev`, `source_prod`
- `staging_dev`, `staging_prod`
- `trial2paid_dev`
- `late_conversions`

CI/CD:
```{jinja}
{% macro get_target_schema() %}
    {% set branch = env_var('DBT_BRANCH', 'dev') %}

    {% if branch == 'main' %}
        {{ return('prod') }}
    {% elif branch == 'develop' %}
        {{ return('staging') }}
    {% else %}
        {{ return('dev') }}
    {% endif %}
{% endmacro %}

```

`git rev-parse --abbrev-ref HEAD`

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

