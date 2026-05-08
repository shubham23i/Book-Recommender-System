import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging
from Books_Recommender.config.configuration import AppConfiguration

class ModelTrainer:
    def __init__(self,app_config=AppConfiguration()):
        try:
            self.model_trainer_config=app_config.get_model_trainer_config()
        except Exception as e:
            raise CustomException(e, sys)
        
    def train(self):
        try:
            book_pivot_path=os.path.join(self.model_trainer_config.transformed_data_file_dir,'transformed_data.pkl')
            book_pivot=pickle.load(open(book_pivot_path,'rb'))
            
            book_sparse=csr_matrix(book_pivot)

            model=NearestNeighbors(algorithm='brute')
            model.fit(book_sparse)

            os.makedirs(self.model_trainer_config.trained_model_dir,exist_ok=True)
            file_name=os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model,open(file_name,'wb'))
            logging.info(f"Saved trained model to {file_name}")
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20} Model Trainer log started {'='*20}")
            self.train()
            logging.info(f"{'='*20} Model Trainer log completed {'='*20}")
        except Exception as e:
            raise CustomException(e,sys)

