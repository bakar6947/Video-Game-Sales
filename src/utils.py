import os
import sys

from src.exception import CustomException
from src.logger import logging

import pickle



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
        with open(file_path, 'rb') as file:
            file_obj = pickle.load(file)

            return file_obj
    
    except Exception as e:
        raise CustomException(e, sys)
        
        
        