import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj, evaluate_model


from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from xgboost import XGBRegressor



@dataclass
class ModelTrainerConfig:
    model_trainer_file = os.path.join('artifact', 'model_trainer.pkl')
    
    

class ModelTrainer:
    
    def __init__(self):
        self.trainer_config = ModelTrainerConfig()
        
    
    def initiate_model_trainer(self, train_data, test_data):
        logging.info('Initiate Model Trainer')
        
        try:
            
            X_train, y_train, X_test, y_test = (
                train_data[:, :-1],
                train_data[:, -1],
                test_data[:, :-1],
                test_data[:, -1]
            )
            
            
            models = {
                'Linear Regression': LinearRegression(),
                'Ridge': Ridge(),
                'KNN Regressor': KNeighborsRegressor(),
                'Support Vector Regressor': SVR(),
                'Decision Tree': DecisionTreeRegressor(),
                'Random Forest': RandomForestRegressor(),
                'Ada-Boost Regressor': AdaBoostRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'XGB Regressor': XGBRegressor()
            }
            
            
            r2_result = evaluate_model(models, X_train, y_train, X_test, y_test)
            
            sorted_r2_score = sorted(r2_result, key=lambda x: x['Test'])
            
            best_model_name = sorted_r2_score[7]['Model']
            best_model_result = sorted_r2_score[7]['Test']
            best_model = models[best_model_name]
            
            if best_model_result < 0.6:
                logging.info('No best model found')
                raise CustomException("No best model found")
       
            logging.info(f'Best model found as: {best_model_name} with R2-Score: {best_model_result}')
            
            save_obj(
                file_path= self.trainer_config.model_trainer_file,
                obj=best_model
            )
            
            
            y_pred = best_model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            
            return(
                best_model_name,
                r2
            )
            
        except Exception as e:
            raise CustomException(e, sys)