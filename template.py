import os
from pathlib import Path
import logging
#To log all the information, also during run time

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep', #to write the CI/CD related yaml files, for time being just adding an hidden file, it is an Automatic file, once u do the commit, it automatically deploys the code into cloud
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py', #components will be another folder, so it will be anothe local package
    f'src/{project_name}/utils/__init__.py',#utility related code 
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml', #all the model related parameters
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb', #for all the notebook experiments
    'test.py'
] 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'creating directory: {filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #if my filesize = 0 then create the file
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}')
    
    else:
        logging.info(f'{filename} already exists')