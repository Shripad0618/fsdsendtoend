import os
import sys

import pandas as pd
import numpy as np

from src.DimondPricePrediction.exception import CustomException
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import load_object
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

@dataclass


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            model_path = os.path.join("artifacts","model.pkl")


            preprocessor_obj = load_object(preprocessor_path)
            model_obj = load_object(model_path)


            scaled_data = preprocessor_obj.transform(features)
            pred = model_obj.predict(scaled_data)

            return pred 


        except Exception as e:
            raise CustomException(e,sys)
        
@dataclass
class CustomData:
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float
    


    def get_data_as_dataframe(self):
            try:
                logging.info("Single value prediction input is bein taken")
                custom_data_input_dict = {
                    'carat':[self.carat],
                    'cut':[self.cut],
                    'color':[self.color],
                    'clarity':[self.clarity],
                    'depth':[self.depth],
                    'table':[self.table],
                    'x':[self.x],
                    'y':[self.y],
                    'z':[self.z] }
                """
                carat,cut,color,clarity,depth,table,x,y,z
                1.52,Premium,F,VS2,62.2,58.0,7.27,7.33,4.55"""
                
                df = pd.DataFrame(custom_data_input_dict)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise CustomException(e,sys)

            