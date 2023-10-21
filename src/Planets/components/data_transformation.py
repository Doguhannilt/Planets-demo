import pandas as pd
import os
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler


class DataIngestionConfig:
    def __init__(self, base_data_path):
        self.base_data_path = base_data_path

class DataIngestion(BaseEstimator, TransformerMixin):
    def __init__(self, base_data_path):
        self.config = DataIngestionConfig(base_data_path)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = pd.read_csv(os.path.join(self.config.base_data_path, X))
        return data

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop):
        self.columns_to_drop = columns_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(columns=self.columns_to_drop)

class DropRows(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.dropna()

class MapColumn(BaseEstimator, TransformerMixin):
    def __init__(self, column_name, mapping_dict):
        self.column_name = column_name
        self.mapping_dict = mapping_dict

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X[self.column_name] = X[self.column_name].map(self.mapping_dict)
        return X

class process:
    # Pipeline oluşturma
    base_data_path = '../../../artifacts/'
    pipeline = Pipeline([
        ('data_ingestion', DataIngestion(base_data_path)),
        ('drop_columns', DropColumns(columns_to_drop=["hostname", "sy_mnum", "disc_facility", "disc_telescope", "disc_instrument"])),
        ('drop_rows', DropRows()),
        ('map_pl_letter', MapColumn(column_name="pl_letter", mapping_dict={"b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8})),
        ('map_discoverymethod', MapColumn(column_name="discoverymethod", mapping_dict={'Radial Velocity': 1, 'Imaging': 2, 'Eclipse Timing Variations': 3, 'Transit': 4, 'Astrometry': 5, 'Disk Kinematics': 6, 'Microlensing': 7, 'Orbital Brightness Modulation': 8, 'Pulsation Timing Variations': 9, 'Transit Timing Variations': 10, 'Pulsar Timing': 11})),
        ('map_disc_locale', MapColumn(column_name="disc_locale", mapping_dict={'Ground': 1, 'Space': 2, 'Multiple Locales': 3, 'Multiple Locale': 4}))
    ])

    # Veriyi işleme
    processed_data = pipeline.transform("data.csv")
    output_directory = os.path.expanduser("~")  # User's home directory

    # Save the processed data to the new directory
    output_file_path = os.path.join(output_directory, "processed_data.csv")
    processed_data.to_csv(output_file_path, index=False) 

class CosineSimilarityCalculator:

    def cosine_similarity(self, tfidf_matrix):
        return cosine_similarity(tfidf_matrix, tfidf_matrix)

    def cosine(self, y, similarity_threshold=0.2):
        '''
        y --> Dependent Variable
        '''

        # TF-IDF Vectors
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(y)

        # Calculate cosine similarity using the class method
        cosine_sim = self.cosine_similarity(tfidf_matrix)

        assigned_numbers = {}
        number_counter = 1

        for i in range(len(y)):
            if i not in assigned_numbers:
                assigned_numbers[i] = number_counter
                number_counter += 1
            for j in range(i+1, len(y)):
                if cosine_sim[i][j] >= similarity_threshold:
                    assigned_numbers[j] = assigned_numbers[i]

        # A new column for y
        dependent_variable = [assigned_numbers[i] for i in range(len(y))]

        # Convert dependent_variable to a DataFrame
        df = pd.DataFrame({'pl_name': dependent_variable})

        return df

class scaling:

    def scale_and_export_data(self, X_train, X_test):
        base_data_path = '../../../artifacts/'
        
        # Initialize the StandardScaler
        scaler = MinMaxScaler()

        # Fit and transform X_train
        X_train_scaled = scaler.fit_transform(X_train)

        # Transform X_test (using the same scaler)
        X_test_scaled = scaler.transform(X_test)

        # Convert the scaled arrays back to DataFrames with appropriate column names
        X_train_df = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        X_test_df = pd.DataFrame(X_test_scaled, columns=X_train.columns)

        # Export DataFrames to CSV
        output_file_path = os.path.join(base_data_path, "X_train_df.csv")
        X_train_df.to_csv(output_file_path, index=False) 

        output_file_path = os.path.join(base_data_path, "X_test_df.csv")
        X_test_df.to_csv(output_file_path, index=False)

