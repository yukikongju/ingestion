--- This query generates DDL for the existing tables in ua_extract_dev
select 
  table_name, ddl
from `relax-melodies-android.ua_extract_dev`.INFORMATION_SCHEMA.TABLES
order by 
  table_name

