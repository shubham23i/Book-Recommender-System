import os
import sys
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging
from Books_Recommender.utils.util import read_yaml
from Books_Recommender.entity.config_entity import DataIngestionConfig, DataValidationConfig
from Books_Recommender.constant import *

class AppConfiguration:
    def __init__(self, config_file_path:str=CONFIG_FILE_PATH):
        try:
            self.config_info=read_yaml(file_path=config_file_path)
        except Exception as e:
            raise CustomException(e,sys)

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_config=self.config_info['data_ingestion_config']
            artifacts_dir=self.config_info['artifacts_config']['artifacts_directory']
            dataset_dir=self.config_info['data_ingestion_config']['dataset_dir']

            ingested_data_dir=os.path.join(artifacts_dir,dataset_dir,data_ingestion_config['ingested_dir'])
            raw_data_dir=os.path.join(artifacts_dir,dataset_dir,data_ingestion_config['raw_data_dir'])

            response=DataIngestionConfig(
                dataset_download_url=data_ingestion_config['dataset_download_url'],
                raw_data_dir=raw_data_dir,
                ingested_dir=ingested_data_dir
            )
            logging.info(f'Data ingestion config: {response}')
            return response
        except Exception as e:  
            raise CustomException(e,sys)
        

    def get_data_validation_config(self)->DataValidationConfig:
        try:
            data_validation_config=self.config_info['data_validation_config']
            data_ingestion_config=self.config_info['data_ingestion_config']
            dataset_dir=self.config_info['data_ingestion_config']['dataset_dir']
            artifacts_directory=self.config_info['artifacts_config']['artifacts_directory']
            Books_csv_file=data_validation_config['books_csv_file']
            Ratings_csv_file=data_validation_config['ratings_csv_file']

            books_csv_file_dir=os.path.join(artifacts_directory,dataset_dir,data_ingestion_config['ingested_dir'],Books_csv_file)
            ratings_csv_file_dir=os.path.join(artifacts_directory,dataset_dir,data_ingestion_config['ingested_dir'],Ratings_csv_file)
            clean_data_path=os.path.join(artifacts_directory,dataset_dir,data_validation_config['clean_data_dir'])
            serialized_objects_path=os.path.join(artifacts_directory,dataset_dir,data_validation_config['serialized_objects_dir'])
            
            response=DataValidationConfig(
                clean_data_dir=clean_data_path,
                serialized_objects_dir=serialized_objects_path,
                books_csv_file=books_csv_file_dir,
                ratings_csv_file=ratings_csv_file_dir
            )
            logging.info(f'Data validation config: {response}')
            return response
        except Exception as e:
            raise CustomException(e,sys)
