# Create Custom Exception
import sys
from src.logger import logging


def get_error_detail(message, details=None):
    if details is None:
        return f"Error occured: [{message}]"
    
    _, _, exc_tb = details.exc_info()
    
    exc_file = exc_tb.tb_frame.f_code.co_filename
    exc_line = exc_tb.tb_lineno
    
    custom_message = f"Error occured in file: [{exc_file}] at line number: [{exc_line}], with message: [{str(message)}]"
    
    return custom_message





class CustomException(Exception):
    
    def __init__(self, error_message, error_detial=None):
        super().__init__(error_message)
        
        self.error_message = get_error_detail(error_message, error_detial)
    
    def __str__(self):
        return self.error_message
    

# Test Logging and Exception  
# try:
#     c = 1/0
# except Exception as e:
#     # logging.info('test logging and exception')
#     raise CustomException(e, sys)