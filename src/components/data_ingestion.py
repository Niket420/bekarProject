import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.components import *
from src.exception import CustomException
from src.logger import logging
from src.utils import export_collection_as_dataframe



@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("entered initiate_data_ingestion method of dataIngestion class")

        try:
            df:pd.DataFrame = export_collection_as_dataframe(
                db_name= MONGO_DATABASE_NAME , collection_name = MONGO_COLLECTION_NAME
            )

            logging.info("Exported collection as dataframe")

        except Exception as e:
            logging.info("error occured in data ingestion file")
            raise CustomException(e,sys)