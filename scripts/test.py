from bq_utils import get_bigquery_client, get_bigquery_table_path


def main():
    client = get_bigquery_client()
    table_path = get_bigquery_table_path(project_id='relax-melodies-android', dataset_id='ua_extract', table_id='facebook_ads_complete')
    query = f"""
    SELECT * from `{table_path}`
    where
        date = '2025-09-01'
    """

    print(f"Query from {table_path}...")
    query_job = client.query(query)
    rows = query_job.result()



if __name__ == "__main__":
    main()
