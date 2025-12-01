import random
import pandas as pd
from typing import Any, Union
from enum import Enum, auto

class DataFormat(Enum):
    DATAFRAME = auto()
    JSON = auto()
    PARQUET = auto()

def generate_sample_ads_data(start_date: Union[str, pd.Timestamp], end_date: Union[str, pd.Timestamp], data_format: DataFormat) -> Any: 
    # TODO: verify that dates are valid

    #  generate dummy data
    dates = pd.date_range(start_date, end_date).tolist()

    n = len(dates)
    impressions = [random.uniform(1000, 10000)] * n
    clicks = [random.uniform(1000, 1000)] * n
    installs = [random.uniform(100, 800)] * n


    # format
    if data_format == DataFormat.DATAFRAME:
        df = pd.DataFrame(dates, columns=['date'])
        df['impressions'] = impressions
        df['clicks'] = clicks
        df['installs'] = installs
        return df
    elif data_format == DataFormat.JSON:
        raise NotImplementedError("JSON data format not implemented yet.")
    elif data_format == DataFormat.PARQUET:
        raise NotImplementedError("PARQUET data format not implemented yet.")


