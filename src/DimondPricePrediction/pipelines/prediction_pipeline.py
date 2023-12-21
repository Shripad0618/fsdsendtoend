import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import save_object

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass

class Modeltrainerconfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')


class Modeltrainer:
    def __init__(self):
        self.model_trainer_config = Modeltrainerconfig()

    def predict(self,features):
        try:
            logging.info('Splitting the dependent and Independent variables from train and test data')
            X_train,y_train, X_test,y_test = (train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])

            models = {'LinearRegression':LinearRegression(),'Lasso':Lasso(),'Ridge':Ridge(),"ElasticNet":ElasticNet()}

            model_report:dict = evaluate_model()
        except:
            pass