from Books_Recommender.exception.exception_handler import CustomException
from Books_Recommender.logger.log import logging
import sys

if __name__=="__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info(f"checking logger")
        raise CustomException(e,sys)
        