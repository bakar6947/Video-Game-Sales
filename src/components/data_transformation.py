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
from sklearn.compose import ColumnTransformer


@dataclass
class DataTransformerConfig:
    preprocessor_file_path = os.path.join('artifact', 'transformer.pkl')
    logging.info('Transformer PKL File Created')


class DataTransformer:
    
    def __init__(self):
        self.processor_file = DataTransformerConfig()
        
        
    def get_transformer(self):
        logging.info('Build Pipeline')
        
        try:
            transformer_pipe = Pipeline(
                [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            
            return transformer_pipe            
        
        except Exception as e:
            raise CustomException(e, sys)
        
        
        
    def initiate_transformation(self, train_path, test_path):
        logging.info('Start Data Transformation')
        
        try:
            # Get Preprocessor Pipeline Object
            transformer_obj = self.get_transformer()
            
            # Get Traina and Test Data Frames
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            
            # Seperate Input and Target Feature of both data frames
            target_feature = 'Global_Sales'
            un_required_feature = ['Rank' ,'Name']
        
            train_df_input = train_df.drop(columns=un_required_feature + [target_feature] )
            train_df_target = train_df[target_feature]
            
            test_df_input = test_df.drop(columns=un_required_feature + [target_feature])
            test_df_target = test_df[target_feature]

            
            # Label Encoding
            categorical_columns = ['Platform', 'Genre', 'Publisher']
            
            for var in categorical_columns:
                encoder = LabelEncoder()
                train_df_input[var] = encoder.fit_transform(train_df_input[var])
                test_df_input[var] = encoder.transform(test_df_input[var])
            
            
            # Apply Transformer Object
            train_input_arr = transformer_obj.fit_transform(train_df_input)
            test_input_arr = transformer_obj.transform(test_df_input)
            
            
            # Concatenate Input and Target Arrays
            train_arr = np.c_[train_input_arr, np.array(train_df_target)]
            test_arr = np.c_[test_input_arr, np.array(test_df_target)]

            
            # Save Preprocessor Pipeline Object in pkl file
            save_obj(
                file_path=self.processor_file.preprocessor_file_path,
                obj=transformer_obj
            )
            
            logging.info('Data Transformation Complete')
            
            return(
                train_arr,
                test_arr,
                self.processor_file.preprocessor_file_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)