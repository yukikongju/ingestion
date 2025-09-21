from git import Repo
from google.cloud import bigquery
import pandas as pd

def get_current_branch(path=".") -> str:
    repo = Repo(path)
    return repo.active_branch.name

def get_env_name_from_branch() -> str:
    branch = get_current_branch()
    if branch == "main":
        return "prod"
    elif branch == "staging":
        return "staging"
    else:
        return "dev"


def get_bigquery_table_path(project_id: str, dataset_id: str, table_id: str) -> str:
    """
    Get bigquery table path based on branch

    Example
    -------
    > get_bigquery_table_path('relax-melodies-android', 'ua_extraction', 'facebook_ads')
    """
    env = get_env_name_from_branch()
    return f"{project_id}.{dataset_id}_{env}.{table_id}"

def get_bigquery_client() -> bigquery.Client :
    return bigquery.Client()
