# LIBRARIES
import pandas as pd

# Filling missing values with median
def fill_missing_with_median(df):

    '''
    Custom Median Imputation
    '''

    numerical_cols = df.select_dtypes(include=['number']).columns
    df_copy = df.copy()  # Create a copy of the DataFrame
    
    for col in numerical_cols:
        median_value = df_copy[col].median()
        df_copy[col].fillna(median_value, inplace=True)

    return df_copy

# Custom transformer for most frequent categorical value imputation
def fill_missing_with_frequency(df):

    '''
    Custom Categorical Frequency Imputation
    '''

    categorical_cols = df.select_dtypes(exclude=['number']).columns
    df_copy = df.copy()  # Create a copy of the DataFrame containing categorical columns
    
    for col in categorical_cols:
        most_frequent_value = df_copy[col].value_counts().idxmax()
        df_copy[col].fillna(most_frequent_value, inplace=True)

    return df_copy 

# Necessary preprocessing
def result_df_preprocessing(data):
    
    '''
    The function is related to data_transformation.py and applying necessary preprocessing for "result_df"
    '''

    # Dictionaries
    pl_bmassprov_map = {
        'M-R relationship':1,
        'Msin(i)/sin(i)': 2,
        'Msini': 3,
        'Mass': 4
    }
    st_metratio_key_change = {
        '[Fe/H]': 'Fe_H',
        '[M/H]': 'M_H',
        '[m/H]': 'm_H',
        '[Me/H]': 'Me_H',
        "[Fe/H[']": 'Fe_H_Non'
    }

    st_metratio_mapping = {
        'Fe_H':1,
        'M_H':2,
        'm_H':3,
        'Me_H':4,
        'Fe_H_Non':5
    }

    # Mapping, Replacing and Label Encoding
    data["Planet Mass or Mass*sin(i) Provenance"] = data["Planet Mass or Mass*sin(i) Provenance"].map(pl_bmassprov_map)
    data['Stellar Metallicity Ratio'] = data['Stellar Metallicity Ratio'].replace(st_metratio_key_change)
    data["Stellar Metallicity Ratio"] = data["Stellar Metallicity Ratio"].map(st_metratio_mapping)

    data.drop(["RA [sexagesimal]","Discovery Facility","Dec [sexagesimal]","Host Name","Discovery Method","Spectral Type"],axis=1,inplace=True)  
    
    # Return the preprocessed DataFrame instead of saving it to a CSV file
    return data