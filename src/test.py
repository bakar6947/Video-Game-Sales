import sys

from src.exception import CustomException
from src.logger import logging


from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformer
from src.components.model_training import ModelTrainer

from src.pipeline.predict_pipeline import CustomData, PredictPipeline


        
        
        
# Test Components
if __name__ == '__main__':
    logging.info('Testing all Components')
    try:
        
        ingestion_obj = DataIngestion()
        transformer_obj = DataTransformer()
        trainer_obj = ModelTrainer()
    

        train_data, test_data = ingestion_obj.initiate_data_ingestion()

        train_arr, test_arr, processor_obj = transformer_obj.initiate_transformation(train_data, test_data)

        best_model_name, best_r2_score = trainer_obj.initiate_model_trainer(train_arr, test_arr)
        
        print(best_model_name, best_r2_score)
        # # Output is: Linear Regression 0.9999934710404391
        
        
        
        # Predict new Data Point for testing
        custom_data_obj = CustomData(
            platform=16,
            year=2006.0,
            gener=10,
            publisher=10,
            NA_sales=41.49,
            EU_sales=29.02,
            JP_sales=3.77,
            other_sales=8.46
        )
        
        data_point = custom_data_obj.get_data_transfor_as_df()
        
        
        # Make Final Prediction
        predict_pipe = PredictPipeline()
        
        global_sales = predict_pipe.predict(data_point)
        print(global_sales)
        
        logging.info(f'Final Prediction: {global_sales}')
        
    except Exception as e:
        raise CustomException(e, sys)