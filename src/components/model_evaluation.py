import os
import sys
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import pickle
from src.utils.utils import load_object
from urllib.parse import urlparse
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from src.logger.logging import logging
from src.exceptions.exceptions import customexception


class ModelEvaluation:
    def __init__(self):
        logging.info("model evaulation started")
        
    def eval_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        logging.info("evaluation metrics captured")
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_arr,test_arr):
        try:
            x_test,y_test=(test_arr[:,:-1],test_arr[:,-1])
            model_path=os.path.join("artifacts","model.pkl")
            model=load_object(model_path)
            logging.info("model has registered")
            
            tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type_store)
            
            with mlflow.start_run():
                prediction=model.predict(x_test)
                (rmse,mae,r2)=self.eval_metrics(y_test,prediction)
                
                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)
                
                if tracking_url_type_store!="file":
                    mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
                    
                else:
                    mlflow.sklearn.log_model(model,"model")
                    
        except Exception as e:
            logging.info("error occured in model evaluation")
            raise customexception(e,sys)
                    
