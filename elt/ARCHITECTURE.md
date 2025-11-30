# ELT

The ELT pipeline has the following steps:
1. Extraction
2. Load
3. Transformation
4. Store

Our ELT job can be broken down into 2 jobs:
1. Extraction Job: 
    a. Data Gathering. Often from API or S3 bucket
    b. File Format. csv, parquet, JSON, ...
    c. Store data. Store in Postgres, BigQuery, ...
2. Transformation Job:
    a. Load Data. Read data from path
    b. Transform the data.
    c. Store the data.

This package was designed such that data orchestration becomes 
easier and developper can focus on extract and transforms

```

class CustomTransform(Transform):

    def __init__(self, loader, transformer, uploader):
	pass

transform.run()
```

```

extract >> transform
```

To write:
- [ ] Setup DB => Postgres, BigQuery
- [ ] Data Class
    - [ ] Pipeline
    - [ ] Extractor and Transformator
    - [ ] Extractor, Formatter, Loader, Transfomer, Uploader/Exporter

Checklist:
- environment
- tests
- what if abstract class functions don't pass the same params 
  into arguments

To read:
- typing: Callable, Protocol


### Docs

- [petl docs](https://github.com/petl-developers/petl)
- [Arjan Codes - container](https://github.com/ArjanCodes/examples/blob/main/2025/di/container.py)


