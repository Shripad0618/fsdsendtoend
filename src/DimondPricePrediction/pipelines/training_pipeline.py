from src.DimondPricePrediction.components.data_ingestion import Data_Ingestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import Model_trainer



import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException
import pandas as pd

obj = Data_Ingestion()

train_data_path, test_data_path= obj.initiate_data_ingestion() 
data_transformation = DataTransformation()

train_arr,test_arr = data_transformation.intialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=Model_trainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)




