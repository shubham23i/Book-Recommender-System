import sys
import PyYAML  as yaml
from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging

def read_yaml(file_path):
    try:
        with open(file_path,"r") as f:
            data=yaml.safe_load(f)
            return data
    except Exception as e:
        CustomException(e,sys)

