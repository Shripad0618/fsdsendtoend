from src.DimondPricePrediction.components.data_ingestion import Data_Ingestion

import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException
import pandas as pd

obj = Data_Ingestion()

obj.initiate_data_ingestion()
