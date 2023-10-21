# LIBRARIES
import pandas as pd
from dataclasses import dataclass
import os
from sklearn.model_selection import train_test_split # Dividing into X_train, X_test, y_train,y_test
import zipfile
import numpy as np
from data_transformation import CosineSimilarityCalculator,scaling



@dataclass
class DataIngestionConfig:
    base_data_path: str = '../../../artifacts/'
    X_train_data_path: str = os.path.join(base_data_path, 'X_train.csv')
    X_test_data_path: str = os.path.join(base_data_path, 'X_test.csv')
    y_test_data_path: str = os.path.join(base_data_path, 'y_test.csv')
    y_train_data_path: str = os.path.join(base_data_path, 'y_train.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        self.tf_idf = CosineSimilarityCalculator()
        self.scaling = scaling()

    def initiate_data_ingestion(self):
        
        #DataFrame
        df = pd.read_csv(os.path.join(self.ingestion_config.base_data_path, "processed_data.csv"))
        
        # Independent columns and dependent column
        X = df.drop("pl_name", axis = 1)
        y = df["pl_name"]
        
        # Cosine Similarity
        y = self.tf_idf.cosine(y)

        # Splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Standardization
        self.scaling.scale_and_export_data(X_train, X_test)

        # Save them as csv file
        X_train.to_csv(self.ingestion_config.X_train_data_path,index=False,header=True)
        X_test.to_csv(self.ingestion_config.X_test_data_path,index=False,header=True)
 

        y_train.to_csv(self.ingestion_config.y_train_data_path,index=False,header=True)
        y_test.to_csv(self.ingestion_config.y_test_data_path,index=False,header=True)

        return(
            self.ingestion_config.X_train_data_path,
            self.ingestion_config.y_test_data_path,
            self.ingestion_config.y_train_data_path,
            self.ingestion_config.X_test_data_path
        )
