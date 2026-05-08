import os
import sys
import pickle
import pandas as pd
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging    
from Books_Recommender.config.configuration import AppConfiguration

class DataTransformation:
    def __init__(self,app_config=AppConfiguration()):
        try:
            self.data_transformation_config=app_config.get_data_transformation_config()
            self.data_validation_config=app_config.get_data_validation_config()
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_transformer(self):
        try:
            file_path=os.path.join(self.data_transformation_config.clean_data_dir,"ratings.csv")
            df=pd.read_csv(file_path)

            book_pivot=df.pivot(index='user_id',columns='title',values='rating')
            logging.info(f"book_pivot shape: {book_pivot.shape}")
            book_pivot.fillna(0,inplace=True)

            os.makedirs(self.data_transformation_config.data_transformation_dir,exist_ok=True)
            pickle.dump(book_pivot,open(os.path.join(self.data_transformation_config.data_transformation_dir,'transformed_data.pkl'),'wb'))
            logging.info(f"serialized objects saved at {self.data_transformation_config.data_transformation_dir}")

            book_names=book_pivot.index

            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(book_names,open(os.path.join(self.data_validation_config.serialized_objects_dir, "book_names.pkl"),"wb"))
            logging.info(f"Saved book_names serialization object to {self.data_validation_config.serialized_objects_dir}")


            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(book_pivot,open(os.path.join(self.data_validation_config.serialized_objects_dir, "books_pivot.pkl"),"wb"))
            logging.info(f"Saved book_pivot serialization object to {self.data_validation_config.serialized_objects_dir}")
        except Exception as e:
            raise CustomException(e,sys)
        

        def initiate_data_transformation(self):
            try:
                logging.info(f"{'='*20}Data Transformation log started.{'='*20} ")
                self.get_data_transformer()
                logging.info(f"{'='*20}Data Transformation log completed.{'='*20} \n\n")
            except Exception as e:
                raise CustomException(e, sys) 