## The Feature Selection and Feature Selection_1 files will be used in the next upgrade of the project

import pandas as pd

X_train = pd.read_csv("../../../artifacts/X_train.csv")
y_train = pd.read_csv("../../../artifacts/y_train.csv")
threshold=0.7


# Find and remove correlated features
# Note: This function is provided by Krish Naik [Feature Engineering YouTube Playlist]
def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    correlation_list = list(correlation(X_train,threshold))
    return(
        col_corr,
        correlation_list)
