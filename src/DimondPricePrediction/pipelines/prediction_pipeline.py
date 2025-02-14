import os
import sys
import pandas as pd
from src.DimondPricePrediction.logger.logger import logging
from src.DimondPricePrediction.exception.exception import customException
from src.DimondPricePrediction.utils.utils import load_object


class PredictPipeline:

    
    def __init__(self):
        print("init.. the object")

    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")   # we are taking preprocessing from artifact because Once the model is trained, it's beneficial to persist the trained model as an artifact. This allows you to reuse the model for future predictions without having to retrain it every time
            model_path=os.path.join("artifacts","model.pkl")    # we are taking model from artificat

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_fea=preprocessor.transform(features)
            pred=model.predict(scaled_fea)

            return pred

        except Exception as e:
            raise customException(e,sys)


class CustomData:
    def __init__(self,
                 carat:float,                     # it can be changed
                 depth:float,                     # we are initializing variable from app.py
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
            
    def get_data_as_dataframe(self):                    # this data will get or collect from app.py that user will input in the app and will convert it in dataframe
        try:
            custom_data_input_dict = {
                'carat':[self.carat],      # it can be changed
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customException(e,sys)