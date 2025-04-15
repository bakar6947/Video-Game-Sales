import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer


from sklearn.model_selection import train_test_split






@dataclass
class DataIngestionConfig:
    raw_data_file = os.path.join('artifact', 'raw_data.csv')
    train_data_file = os.path.join('artifact', 'train_data.csv')
    test_data_file = os.path.join('artifact', 'test_data.csv')
    
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info('Initiate Data Ingestion')
        
        try:
            # Load Data Set
            df = pd.read_csv('notebook/data/Video Games Sales(Clean).csv')
            logging.info('Read the data frame')
            
            # Craete folder name: artifact
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_file), exist_ok=True)
            
            # Store Raw Data Frame
            df.to_csv(self.ingestion_config.raw_data_file, index=False)
            
            
            # Train Test Split
            logging.info('Initiate Train Test Split')
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            
            # Create Train and Test Data Frames
            train_data.to_csv(self.ingestion_config.train_data_file, index=False)
            
            test_data.to_csv(self.ingestion_config.test_data_file, index=False)
            
            
            return(
                self.ingestion_config.train_data_file,
                self.ingestion_config.test_data_file
            )

        except Exception as e:
            raise CustomException(e, sys)
        
        
        
# Test Components
if __name__ == '__main__':
    try:
        ingestion_obj = DataIngestion()
        transform_obj = DataTransformation()
        trainer = ModelTrainer()
    
    
        train_data, test_data = ingestion_obj.initiate_data_ingestion()

        train_arr, test_arr, processor_obj = transform_obj.initiate_transformation(train_data, test_data)

        best_model_name, best_r2_score = trainer.initiate_model_trainer(train_arr, test_arr)
        
    except Exception as e:
        raise CustomException(e, sys)