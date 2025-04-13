import os 
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Project name
project_name = "Diamond_Price_Predict_End_to_End"

# List of files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",  # fixed typo from __int__.py to __init__.py
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/configuration.yaml",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/pipeline.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# File creation loop
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
