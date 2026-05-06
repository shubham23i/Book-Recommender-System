from collections import namedtuple

DataIngestionConfig = namedtuple('DataIngestionConfig',['dataset_download_url','ingested_dir','raw_data_dir'])