import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

from sklearn.model_selection import train_test_split






@dataclass
class DataIngestionConfig:
    raw_data_file = os.path.join('artifact', 'raw_data.csv')
    train_data_file = os.path.join('artifact', 'train_data.csv')
    test_data_file = os.path.join('artifact', 'test_data.csv')
    logging.info('Raw, Train and Test CSV files created.')
    
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion Start')
        
        try:
            # Load Data Set
            df = pd.read_csv('notebook/data/Video Games Sales(Clean).csv')
            
            # Craete folder name: artifact
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_file), exist_ok=True)
            
            # Store Raw Data Frame
            df.to_csv(self.ingestion_config.raw_data_file, index=False)
            
            # Train Test Split
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
            
            # Create Train and Test Data Frames
            train_data.to_csv(self.ingestion_config.train_data_file, index=False)
            
            test_data.to_csv(self.ingestion_config.test_data_file, index=False)
            
            logging.info('Data Ingestion Complete')
            return(
                self.ingestion_config.train_data_file,
                self.ingestion_config.test_data_file
            )

        except Exception as e:
            raise CustomException(e, sys)