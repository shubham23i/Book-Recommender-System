from Books_Recommender.components.stage_00_data_ingestion import DataIngestion
from Books_Recommender.components.stage_01_data_validation import DataValidation
from Books_Recommender.components.stage_02_data_transformation import DataTransformation
from Books_Recommender.components.stage_03_model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion=DataIngestion()
        self.data_validation=DataValidation()
        self.data_transformation=DataTransformation()
        self.model_trainer=ModelTrainer()

    def start_training_pipeline(self):
        self.data_ingestion.initiate_data_ingestion()
        self.data_validation.initiate_data_validation()
        self.data_transformation.get_data_transformer()
        self.model_trainer.train()
    
        


