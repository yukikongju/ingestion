import logging
import pandas as pd

from abc import ABC
from collections.abc import Callable
from pydantic import BaseModel
from typing import Any, Dict, List, Union


#  TODO: define Data with pydantic
#  type Data = List[Dict[str, Any]] # (format_type, data)

#############
#  CONFIGS  #
#############




#############
#  CLASSES  #
#############

class Extractor(ABC):

    def __init__(self) -> None:
        super().__init__()

    def extract(self):
        """
        Extract the data from source
        """
        pass

class Formatter(ABC):

    def __init__(self) -> None:
        super().__init__()

    def format(self, data, model: BaseModel):
        """
        Format the data based on pydantic based model
        """
        pass

class Loader(ABC):

    def __init__(self) -> None:
        super().__init__()

    def load(self):
        """
        Load data from database/source/file
        """
        pass
        
class Transformer(ABC):

    def __init__(self) -> None:
        super().__init__()

    def transform(self, data):
        """
        Transform the data
        """
        pass
        
class Uploader(ABC):

    def __init__(self) -> None:
        super().__init__()

    def upload(self, data):
        """
        Upload data to database/file
        """
        pass

##########
#  RUNS  #
##########

def extraction_run(func: Callable[[Union[str, pd.Timestamp], Union[str, pd.Timestamp]], Any], 
        start_date: Union[str, pd.Timestamp ], end_date: Union[str, pd.Timestamp]) -> Any:
    func(start_date, end_date)
    logging.info(f"---- Extraction: {func.__qualname__}")


##########
#  JOBS  #
##########

class Job(ABC):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass

class ExtractJob(ABC):

    def __init__(self, extractor: Extractor, formatter: Formatter, 
                 model: BaseModel, uploader: Uploader) -> None:
        super().__init__()
        self.extractor = extractor
        self.formatter = formatter
        self.model = model
        self.uploader = uploader

    def run(self):
        data = self.extractor.extract()
        formatted = self.formatter.format(data, self.model)
        if formatted:
            self.uploader.upload(data)

class TransformJob(ABC):

    def __init__(self, loader: Loader, transformer: Transformer, formatter: Formatter, model: BaseModel, uploader: Uploader) -> None:
        super().__init__()
        self.loader = loader
        self.transformer = transformer
        self.formatter = formatter
        self.model = model
        self.uploader = uploader

    def run(self):
        data = self.loader.load()
        transformed = self.transformer.transform(data)
        formatted = self.formatter.format(transformed, self.model)
        if formatted:
            self.uploader.upload(formatted)
