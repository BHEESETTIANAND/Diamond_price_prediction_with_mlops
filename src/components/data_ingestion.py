import pandas as pd
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split
from pathlib import Path
from dataclasses import dataclass
from src.logger.logging import logging
from src.exceptions.exceptions import customexception
import mlflow
import mlflow.sklearn


@dataclass
class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts", "raw_data.csv")
    train_data_path:str=os.path.join("artifacts", "train_data.csv")
    test_data_path:str=os.path.join("artifacts", "test_data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
        
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data=pd.read_csv("D:/New folder/Downloads/gemstone.csv")
            logging.info("data frame was readed")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("saved raw data frame")
            
            logging.info("splitting of data into train test data started")
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("data was successfully splitted into train and test data")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("data ingestion completed")
            
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
        except Exception as e:
            logging.info("error occured while ingesting the data")
            raise customexception(e,sys)
        
        
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()