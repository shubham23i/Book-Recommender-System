import os
import sys
import ast
import pandas as pd
import pickle
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging
from Books_Recommender.config.configuration import AppConfiguration


class DataValidation:
    def __init__(self,app_config=AppConfiguration()):
        try:
            self.data_validation_config=app_config.get_data_validation_config()
        except Exception as e:
            raise CustomException(e,sys)
        
    def process_data(self):
        try:
            ratings=pd.read_csv(self.data_validation_config.ratings_csv_file,sep=';',encoding='latin-1',on_bad_lines='skip')
            books=pd.read_csv(self.data_validation_config.books_csv_file,sep=';',encoding='latin-1',on_bad_lines='skip',low_memory=False)

            logging.info(f"ratings shape: {ratings.shape}")
            logging.info(f"books shape: {books.shape}")

            books=books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher',
                'Image-URL-L']]
            books.columns = books.columns.str.replace('"', '').str.strip()

            ratings.columns = ratings.columns.str.replace('"', '').str.strip()
            books.rename(columns={
                'ISBN':'isbn',
                'Book-Title':'title',
                'Book-Author':'author',
                'Year_Of_Publication':'year',
                'publisher':'publisher',
                'Image-URL-L':'image_url',
            },inplace=True)
            ratings.rename(columns={
                'User-ID':'user_id',
                'ISBN':'isbn',
                'Book-Rating':'rating'
            },inplace=True)
            x=ratings['user_id'].value_counts()>200
            y=x[x].index
            ratings=ratings[ratings['user_id'].isin(y)]

            ratings_with_books=ratings.merge(books,on='isbn',how='left')
            number_rating=ratings_with_books.groupby('title')['rating'].count().reset_index()
            number_rating.rename(columns={
                'rating':'number_of_rating'
            },inplace=True)
            final_rating=ratings_with_books.merge(number_rating,on='title',how='left')

            final_rating=final_rating[final_rating['number_of_rating']>50]


            final_rating.drop_duplicates(['user_id','title'],inplace=True)
            logging.info(f"final_rating shape: {final_rating.shape}")


            os.makedirs(self.data_validation_config.clean_data_dir,exist_ok=True)
            final_rating.to_csv(os.path.join(self.data_validation_config.clean_data_dir,'ratings.csv'),index=False)
            logging.info(f"clean data saved at {self.data_validation_config.clean_data_dir}")


            os.makedirs(self.data_validation_config.serialized_objects_dir,exist_ok=True)
            pickle.dump(final_rating,open(os.path.join(self.data_validation_config.serialized_objects_dir,'ratings.pkl'),'wb'))
            logging.info(f"serialized objects saved at {self.data_validation_config.serialized_objects_dir}")

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self):
        try:
            logging.info(f"{'='*20} data validation log started {'='*20}")
            self.process_data()
            logging.info(f"{'='*20} data validation log completed {'='*20}")
        except Exception as e:  
            raise CustomException(e,sys)