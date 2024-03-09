import os
import sys
import pandas as pd

from src.logger.logging import logging
from src.exceptions.exceptions import customexception
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

obj=DataIngestion()
train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()
train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

model_trainer=ModelTrainer()
model_trainer.initiate_model_training(train_arr,test_arr)

model_evaluation=ModelEvaluation()
model_evaluation.initiate_model_evaluation(train_arr,test_arr)