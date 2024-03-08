import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logger.logging import logging
from src.exceptions.exceptions import customexception
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


def save_objects(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path) as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info("error occured while saving the object in utils file")
        raise customexception(e,sys)
    
    
def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(x_train.y_train)
            y_test_pred=model.predict(x_test)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score
        return report

    except Exception as e:
        logging.info("error occurred while evaluating the model in utils file")
        raise customexception(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        logging.info("error occurred while loading the object in utils file")
        raise customexception(e,sys)