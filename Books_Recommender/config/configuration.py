import os
import sys
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging
from Books_Recommender.utils.util import read_yaml
from Books_Recommender.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelRecommendationConfig
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
        
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            data_transformation_config=self.config_info['data_transformation_config']
            data_validation_config=self.config_info['data_validation_config']
            data_ingestion_config=self.config_info['data_ingestion_config']
            dataset_dir=self.config_info['data_ingestion_config']['dataset_dir']
            artifacts_directory=self.config_info['artifacts_config']['artifacts_directory']

            clean_data_path=os.path.join(artifacts_directory,dataset_dir,data_validation_config['clean_data_dir'])
            transformed_data_dir=os.path.join(artifacts_directory,dataset_dir,data_transformation_config['data_transformation_dir'])
             
            response=DataTransformationConfig(
                clean_data_dir=clean_data_path,
                data_transformation_dir=transformed_data_dir
            )
            logging.info(f'Data transformation config: {response}')
            return response
        except Exception as e:
            raise CustomException(e,sys)
        

    def get_model_trainer_config(self,config=ModelTrainerConfig):
        try:
            model_trainer_config=self.config_info['model_trainer_config']
            data_transformation_config=self.config_info['data_transformation_config']
            data_ingestion_config=self.config_info['data_ingestion_config']
            
            dataset_dir=data_ingestion_config['dataset_dir']
            artifacts_directory=self.config_info['artifacts_config']['artifacts_directory']

            transformed_data_file_dir = os.path.join(artifacts_directory, dataset_dir, data_transformation_config['data_transformation_dir'])
            trained_model_dir = os.path.join(artifacts_directory, model_trainer_config['trained_model_dir'])
            trained_model_name = model_trainer_config['trained_model_name']

            response=ModelTrainerConfig(
                transformed_data_file_dir=transformed_data_file_dir,
                trained_model_dir=trained_model_dir,
                trained_model_name=trained_model_name
            )
            logging.info(f'Model trainer config: {response}')
            return response
        except Exception as e:
            raise CustomException(e,sys)

    def get_model_recommendation_config(self)->ModelRecommendationConfig:
        try:
            model_reccomendation_config=self.config_info['recommendation_config']
            model_trainer_config=self.config_info['model_trainer_config']
            data_ingestion_config=self.config_info['data_ingestion_config']
            data_validation_config=self.config_info['data_validation_config']
            trained_model_name=model_trainer_config['trained_model_name']
            artifacts_directory=self.config_info['artifacts_config']['artifacts_directory']
            trained_model_directory=os.path.join(artifacts_directory,model_trainer_config['trained_model_dir'])
            poster_api=model_reccomendation_config['poster_url']

            book_name_serialized_objects=os.path.join(artifacts_directory,data_validation_config['serialized_objects_dir'],"book_names.pkl")
            book_pivot_serialized_objects = os.path.join(
                                                    artifacts_directory,
                                                    data_ingestion_config['dataset_dir'],
                                                    data_validation_config['serialized_objects_dir'],
                                                    "books_pivot.pkl"
                                                )
            final_rating_serialized_objects = os.path.join(
                                                    artifacts_directory,
                                                    data_ingestion_config['dataset_dir'],
                                                    data_validation_config['serialized_objects_dir'],
                                                    "ratings.pkl"
                                                )
            trained_model_path=os.path.join(trained_model_directory,trained_model_name)

            response=ModelRecommendationConfig(
                book_name_serialized_objects=book_name_serialized_objects,
                book_pivot_serialized_objects=book_pivot_serialized_objects,
                final_rating_serialized_objects=final_rating_serialized_objects,
                trained_model_path=trained_model_path
            )
            return response
        except Exception as e:
            raise CustomException(e,sys)
                                                           