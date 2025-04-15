import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline


@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join('artifact', 'preprocessor.pkl')
    


class DataTransformation:
    
    def __init__(self):
        self.processor_file = DataTransformationConfig()
        
        
    def get_preprocessor_obj(self):
        '''
        Create Pipline and return the preprocessor object
        '''
        logging.info('Build Pipeline')
        
        
        try:
            
            # Create Pipeline with Impute Missing values and Scalling
            preprocessor_pipe = Pipeline(
                [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            
            return preprocessor_pipe            
        
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
    def initiate_transformation(self, train_path, test_path):
        logging.info('Initiate Transformation')
        
        try:
            # Get Preprocessor Pipeline Object
            processor_obj = self.get_preprocessor_obj()
            
            # Get Traina and Test Data Frames
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            # Use Label Encoding
            categorical_columns = ['Platform', 'Genre', 'Publisher']
            
            encoder_obj = LabelEncoder()
            for var in categorical_columns:
                train_df[var] = encoder_obj.fit_transform(train_df[var])
                test_df[var] = encoder_obj.fit_transform(test_df[var])
                
                
            # Seperate Input and Target Feature of both data frames
            target_feature = 'Global_Sales'
            un_required_feature = 'Name'
            
        
            train_df_input = train_df.drop(columns=[target_feature, un_required_feature])
            train_df_target = train_df[target_feature]
            
            test_df_input = test_df.drop(columns=[target_feature, un_required_feature])
            test_df_target = test_df[target_feature]

            
            # Apply Preprocessor Pipeline to both data frames
            logging.info('Apply Transformation on Train and Test Data Frames')
            
            train_input_arr = processor_obj.fit_transform(train_df_input)
            test_input_arr = processor_obj.transform(test_df_input)
            
            
            # Concatenate Input and Target Arrays
            train_arr = np.c_[train_input_arr, np.array(train_df_target)]
            test_arr = np.c_[test_input_arr, np.array(test_df_target)]
            
            logging.info('Transformation Complete')
            
            # Save Preprocessor Pipeline Object in pkl file
            save_obj(
                file_path=self.processor_file.preprocessor_file_path,
                obj=processor_obj
            )
            
            
            return(
                train_arr,
                test_arr,
                self.processor_file.preprocessor_file_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)