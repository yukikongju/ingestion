-- DDL for table creation on specific environment
-- Terminal: dbt run-operation create_fake_data --target dev
{% macro create_fake_data() %}

{% set sql %}
CREATE TABLE IF NOT EXISTS `relax-melodies-android`.`ua_extract_{{ target.name }}.fake_data2` (
    day date NOT NULL, 
    network string NOT null, 
    platform string not null, 
    country string not null, 
    impressions float64,
    clicks float64,
    installs float64,
    trials float64,
    extracted_at timestamp,
)
PARTITION BY day
CLUSTER BY network, platform, country, extracted_at;
{% endset %}

{% do run_query(sql) %}
--  {% do log("Created table fake_data2 in environment" ~ target.name, info=True) %}
{% do log("Query" ~ sql, info=True) %}

{% endmacro %}
