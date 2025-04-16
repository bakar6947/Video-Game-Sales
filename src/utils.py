import os
import sys

from src.exception import CustomException

import pickle
from sklearn.metrics import r2_score
from src.logger import logging


# Dump PKL file object
def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
    
    except Exception as e:
        raise CustomException(e, sys)
    
    
# Load PKL file object   
def load_obj(file_path):
    try:
        
        with open(file_path, "rb") as file:
            file_obj = pickle.load(file)
            
            return file_obj
        
    except Exception as e:
        raise CustomException(e, sys)
        

# Model Evaluation        
def evaluate_model(models, X_train, y_train, X_test, y_test):
    logging.info('Model Evaluation Start')
    try:
        r2_result = []
        
        for key, value in models.items():
            model = value
            model.fit(X_train, y_train)
            
            train_pred = model.predict(X_train)
            test_pred = model.predict(X_test)
            
            r2 = {
                'Model': key,
                'Train': round(r2_score(y_train, train_pred), 4),
                'Test': round(r2_score(y_test, test_pred), 4)
            }
            r2_result.append(r2) 
            
        logging.info('Model Evaluation Complete')    
        return r2_result
                   
    except Exception as e:
        raise CustomException(e, sys)