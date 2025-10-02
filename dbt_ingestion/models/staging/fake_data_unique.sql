with data as (
    select 
	*
	, row_number() over (partition by day, platform, network, country order by loaded_timestamp desc) as rn
    from {{ source('extract', 'fake_data') }}
), dedup as (
    select
	*
    from data
    where rn = 1
)

select * from dedup
