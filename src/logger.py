# Create Logger

import os
import logging
from datetime import datetime


# Create Logging File Structure
log_structure = f'{datetime.now().strftime('%d_%m_%Y_%H_%M')}'
file_structure = f'{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log'

# Craete Log Directory
log_path = os.path.join(os.getcwd(), 'Logs', log_structure)
os.makedirs(log_path, exist_ok=True)


# Create Log File
LOG_FILE = os.path.join(log_path, file_structure)


# Configure Logger
logging.basicConfig(
    filename=LOG_FILE,
    format='[ %(asctime)s ] %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    level=logging.INFO
)



# Test Logging
if __name__ == '__main__':
    logging.info('logging started')