{{ config(materialized='view') }}

with agg as (
    select 
	day, platform, network, country, 
	sum(cost) as cost, 
	sum(impressions) as impressions,
	sum(clicks) as clicks
    from {{ ref('fake_data_unique') }}
    group by day, platform, network, country
)

select * from agg
