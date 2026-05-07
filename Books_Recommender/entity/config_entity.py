from collections import namedtuple

DataIngestionConfig = namedtuple('DataIngestionConfig',['dataset_download_url','ingested_dir','raw_data_dir'])

DataValidationConfig=namedtuple('DataValidationConfig',['clean_data_dir','serialized_objects_dir','books_csv_file','ratings_csv_file'])