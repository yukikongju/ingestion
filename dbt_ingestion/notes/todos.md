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
