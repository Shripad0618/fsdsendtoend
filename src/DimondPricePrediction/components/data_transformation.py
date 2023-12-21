import os
import numpy as np
import pandas as pd
import sys

from dataclasses import dataclass
from src.DimondPricePrediction.components.data_ingestion import Data_Ingestion
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import CustomException

from src.DimondPricePrediction.utils.utils import save_object

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

@dataclass

class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.DataTransformationConfig = DataTransformationConfig()

    def get_data_tranformation(self):
        try:
            logging.info('Data Transformation Inititated')
            # Define which columns should be ordinal-encoded and which should be scaled
            categoricals_cols = ['cut','color','clarity']
            numerical_cols  = ['carat','depth','table','x','y','z']

            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipepline inititated')

            ## Numerical Pipeline

            num_pipeline = Pipeline(steps=[

                ('imputer',SimpleImputer(strategy='median')),
                ("scaler",StandardScaler())
            ])

            ## Categorical Pipeline

            cat_pipeline = Pipeline(steps=[('imputer',SimpleImputer(strategy='most_frequent')),
                                           ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                                           ('scaler',StandardScaler())
                                           ])
            
            preprocessor = ColumnTransformer([('num_piepline',num_pipeline,numerical_cols),
                                              ('cat_pipeline',cat_pipeline,categoricals_cols)
            ])

            return preprocessor
        
        except Exception as e:
            logging.info("Exception Ocurred in the intitate data transformation")
            raise CustomException(e,sys)
        


    def intialize_data_transformation(self, train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)


            logging.info("Read train and test data completed")

            preprocessing_obj = self.get_data_tranformation()

            target_column_name = 'price'
            drop_columns  = [target_column_name,'id']


            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]


            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]


            logging.info("Applying preprocessing object on training and testing dataset")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Preprocessor application completed")
            logging.info("Converting array dataframe to numpy object")


            """regarding np.c_(), this is a shorthand notation for the numpy.concatenate() function along the second axis, which is typically used for concatenating arrays along the second axis (columns).
            It is particularly useful when you want to concatenate two arrays along their second axis, creating a new array.
            import numpy as np

            # Creating two arrays
            array1 = np.array([1, 2, 3])
            array2 = np.array([4, 5, 6])

            # Using np.c_ to concatenate along the second axis (columns)
            result = np.c_[array1, array2]

            print(result)
            [[1 4]
            [2 5]
            [3 6]]
            """
            train_arr = np.c_(input_feature_train_arr,np.array(target_feature_train_df))
            test_arr = np.c_(input_feature_test_arr,np.array(target_feature_test_df))

            save_object(file_path= self.DataTransformationConfig.preprocessor_obj_file_path,obj = preprocessing_obj)

            logging.info("Pre Processing pickle file saved")

            return(train_arr,test_arr)
        

        except Exception as e:
            logging.info("Exception Ocurred in the intitate Data transofrmation")

            raise CustomException(e,sys)

