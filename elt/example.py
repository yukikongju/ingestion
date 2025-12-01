"""
Example Extraction Script for different extraction jobs

Simulating the following:
    - Different source: API, S3
    - Different data types: DataFrame, Parquet, JSON
    - Different date types: str, datetime, pd.Timestamp // pd.to_datetime

Edge Cases:
    - Reading from bucket only shows us a specific amount of data, regardless 
      of the specified start_date and end_date => need to check if data has 
      been extracted

"""
import logging
import pandas as pd
from datetime import datetime
from pydantic import BaseModel
from typing import Any

from pipeline import Extractor, Transformer
from pipeline import extraction_run
from dummy import generate_sample_ads_data, DataFormat

# TODO: replace data to
class Data(BaseModel):
    data: Any

class FacebookExtractor(Extractor):

    def __init__(self, key, metrics) -> None:
        super().__init__()
        self.key = key
        self.metrics = metrics

    def extract(self, start_date: str, end_date: str) -> Any:
        return generate_sample_ads_data(start_date, end_date, DataFormat.DATAFRAME)

def main():
    start_date, end_date = '2025-10-01', '2025-11-01'
    logging.basicConfig(level=logging.INFO)
    facebook_extractor = FacebookExtractor(
        key='key',
        metrics=['impressions', 'clicks', 'installs']
    )
    extraction_run(
        facebook_extractor.extract,
        start_date=start_date, 
        end_date=end_date, 
    )


if __name__ == "__main__":
    main()

