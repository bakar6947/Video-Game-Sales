import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_obj


class PredictPipeline:
    
    def __init__(self):
        pass
    
    
    def load_models(self):
        
        try:
            
            '''
            For run test.py file, Use these paths, else face error
            
            transformer_path = os.path.join('artifact', 'transformer.pkl')
            model_path = os.path.join('artifact', 'model_trainer.pkl')
            '''
            
            # These paths just for app.views.py
            transformer_path = os.path.join('..', 'artifact', 'transformer.pkl')
            model_path = os.path.join('..', 'artifact', 'model_trainer.pkl')
            
            # Load Processor and Model
            transformer = load_obj(transformer_path)
            model = load_obj(model_path)
            
            return transformer, model
            
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
    def predict(self, user_data):
        logging.info('Make Prediction')
        
        try:
            transformer, model = self.load_models()
            
            transformed_data = transformer.transform(user_data)
            prediction = model.predict(transformed_data)
            
            return prediction
            
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
class CustomData:
    
    def __init__(self, platform, year, gener, publisher, NA_sales, EU_sales, JP_sales, other_sales):
        
        self.platform = platform,
        self.year = year,
        self.gener = gener,
        self.publisher = publisher,
        self.NA_sales = NA_sales,
        self.EU_sales = EU_sales,
        self.JP_sales = JP_sales,
        self.other_sales = other_sales

    def get_data_transfor_as_df(self):
        try:
            user_data = {
                'Platform': self.platform,
                'Year': self.year,
                'Genre': self.gener,
                'Publisher': self.platform,
                'NA_Sales': self.NA_sales,
                'EU_Sales': self.EU_sales,
                'JP_Sales': self.JP_sales,
                'Other_Sales': self.other_sales
            }
            
            user_df = pd.DataFrame(user_data)
            return user_df
        
        except Exception as e:
            raise CustomData(e, sys)