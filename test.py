"""

import os

path = "notebooks/research.ipynb"


dir, file = os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open (file,"w") as f:
    pass
"""



from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

CustomData_obj = CustomData(1.52,"Premium","F","VS2",62.2,58.0,7.27,7.33,4.55)

print(CustomData_obj.get_data_as_dataframe())