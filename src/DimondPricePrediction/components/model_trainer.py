import pandas as pd
import numpy as np
import os
import sys


from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException
from dataclasses import dataclass
from src.DimondPricePrediction.utils.utils import save_object
from src.DimondPricePrediction.utils.utils import evaluate_model 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass
class Modeltrainerconfig():
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class Model_trainer:
    def __init__(self):
        self.Modeltrainerconfig = Modeltrainerconfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info('Splitting the dependent and independent variables from train and test data set')
            X_train, X_test, y_train, y_test = (train_arr[:,:-1],test_arr[:,:-1],train_arr[:,-1],test_arr[:,-1])
            models = {'LinearRegression':LinearRegression(),'Lasso':Lasso(),'Ridge':Ridge(),"ElasticNet":ElasticNet()}

            model_report:dict = evaluate_model(X_train,y_train, X_test,y_test,models)
            print(model_report)
            print('\n',"="*20,'\n')
            logging.info(f'Model Report:{model_report}')

            # to get the best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            save_object(file_path=self.Modeltrainerconfig.trained_model_file_path,obj = best_model)

            
        except Exception as e:
            logging.info('Excpetion Ocurred at model training')
            raise CustomException(e,sys)

    