from setuptools import setup, find_packages
from typing import List


hyphon_e = '-e .'
def get_packages(file_name:str)->List[str]:
    '''
    This function get file name as argument and return requirements as list of str
    '''
    requirements = []
    
    with open(file_name) as file:
        requirements = file.readlines()
        
        # Replace \n with ''
        requirements = [req.replace('\n', '') for req in requirements]
        
        if hyphon_e in requirements:
            requirements.remove(hyphon_e)
        
    return requirements



# Configure the package
setup(
    name='game_sales',
    version='0.1',
    author='Abu Bakar',
    author_email='abubakarrajput6947@gmail.com',
    
    description='This package is used to predict the Global Sales of Video Games',
    
    packages=find_packages(),
    install_requires= get_packages("requirements.txt")
)