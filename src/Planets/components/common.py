# LIBRARIES
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from categorized_cosine_similarity import CosineSimilarityCalculator
from data_ingestion import DataIngestion, DataIngestionConfig
from dataclasses import dataclass

# Fixing the column names
def rename_columns(data_df, long_name_series):

    '''
    The function is get used to renaming the columns based on another dataset.
    '''
    # Create a dictionary to map old column names to new column names
    column_name_mapping = dict(zip(data_df.columns, long_name_series))
    
    # Rename the columns of the DataFrame using the mapping
    data_df.rename(columns=column_name_mapping, inplace=True)


def splitting_median(data):
    """
    My computer is not enough to make the whole proccess for NaN values, I am going to create a 
    function to fill the columns with their medians.
    """
    data.fillna[data.median()]
    return data



class class_prediction_cosine_similarity:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def prediction_cosine_similarity_calculation(self,number_of_prediction):
        base_data_path = '../../../artifacts/'
        
        
        df = pd.read_csv(base_data_path,"data.csv")
        y = df["pl_name"]
        # CosineSimilarityCalculator sınıfını oluşturun
        calculator = CosineSimilarityCalculator()

        # Benzerlik eşiği belirleyin (varsayılan olarak 0.2)
        similarity_threshold = 0.2

        # Verileri gruplara ayırın ve sonuçları alın
        result_df = calculator.group_similar_values(y, similarity_threshold)

        path_to_file = base_data_path,"Cosine_similarity.csv"
        result_df.to_csv(path_to_file)

        result_dict_plus = dict(zip(result_df['Group'], result_df['Values']))
    # Belirli bir grubun değerlerini alın
        if number_of_prediction in result_dict_plus:
            prediction_planet = result_dict_plus[number_of_prediction][0]
            
            return prediction_planet
        else:
            print(f"No prediction found for group {number_of_prediction}")
            return None


