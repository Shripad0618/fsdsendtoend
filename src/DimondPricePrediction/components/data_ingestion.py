import pandas as pd
import numpy as np
import os
from src.DimondPricePrediction.logger import logging
from sklearn.model_selection import train_test_split
from src.DimondPricePrediction.exception import CustomException
import sys
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str =os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str  = os.path.join("artifacts","test.csv")





class Data_Ingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("Dataset has been read successfully")

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)

            data.to_csv(self.ingestion_config.raw_data_path,index=False)


            logging.info("I have save the raw dataset in the artifact folder")


            logging.info("Train/Test Split is starting ")

            train_data,test_data = train_test_split(data, test_size= 0.25)
            logging.info("Train/Test Split completed successfully")



            train_data.to_csv(self.ingestion_config.train_data_path,index=False)


            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion part completed")


        except:
            logging.info("Exception Ocurred during data ingestion stage")
            raise CustomException()