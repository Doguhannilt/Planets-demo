## The Feature Selection and Feature Selection_1 files will be used in the next upgrade of the project

import pandas as pd

class FeatureSelection:
    def Featuremoving(self,X_train, X_test):
        columns_to_remove = [
        "Stellar Mass Lower Unc. [Solar mass]",
        "Gaia Magnitude Lower Unc",
        "Planet Radius [Jupiter Radius]",
        "Stellar Surface Gravity [log10(cm/s**2)]",
        "Insolation Flux Lower Unc. [Earth Flux]",
        "V (Johnson) Magnitude Lower Unc",
        "Orbital Period Lower Unc. [days]",
        "Planet Mass or Mass*sin(i) [Earth Mass] Lower Unc.",
        "Distance [pc] Upper Unc",
        "Planet Radius Lower Unc. [Jupiter Radius]",
        "Planet Radius Upper Unc. [Jupiter Radius]",
        "Ks (2MASS) Magnitude Lower Unc",
        "Planet Mass or Mass*sin(i) [Jupiter Mass] Limit Flag",
        "Gaia Magnitude",
        "Planet Mass or Mass*sin(i) [Jupiter Mass] Lower Unc.",
        "Equilibrium Temperature Limit Flag",
        "Planet Mass or Mass*sin(i) [Jupiter Mass] Upper Unc.",
        "Equilibrium Temperature Lower Unc. [K]",
        "Stellar Mass Upper Unc. [Solar mass]",
        "Distance [pc] Lower Unc",
        "Orbit Semi-Major Axis Lower Unc. [au]",
        "Planet Mass or Mass*sin(i) [Jupiter Mass]",
        "Ks (2MASS) Magnitude",
        "Stellar Metallicity Lower Unc. [dex]",
        "Planet Radius Limit Flag.1"]

        # Remove the features that we select from X_train and X_test
        X_train = X_train.drop(columns=columns_to_remove, errors='ignore')
        X_test = X_test.drop(columns=columns_to_remove, errors='ignore')

        # Indexing
        X_train = X_train.reset_index(drop=True)
        X_test = X_test.reset_index(drop=True)
        print('Feature Selection Successful!')

        return X_train, X_test


    def drop_columns_containing_names(self, X_train, X_test):
        columns_to_remove = [
            "Stellar Mass Lower Unc. [Solar mass]",
            "Gaia Magnitude Lower Unc",
            "Planet Radius [Jupiter Radius]",
            "Stellar Surface Gravity [log10(cm/s**2)]",
            "Insolation Flux Lower Unc. [Earth Flux]",
            "V (Johnson) Magnitude Lower Unc",
            "Orbital Period Lower Unc. [days]",
            "Planet Mass or Mass*sin(i) [Earth Mass] Lower Unc.",
            "Distance [pc] Upper Unc",
            "Planet Radius Lower Unc. [Jupiter Radius]",
            "Planet Radius Upper Unc. [Jupiter Radius]",
            "Ks (2MASS) Magnitude Lower Unc",
            "Planet Mass or Mass*sin(i) [Jupiter Mass] Limit Flag",
            "Gaia Magnitude",
            "Planet Mass or Mass*sin(i) [Jupiter Mass] Lower Unc.",
            "Equilibrium Temperature Limit Flag",
            "Planet Mass or Mass*sin(i) [Jupiter Mass] Upper Unc.",
            "Equilibrium Temperature Lower Unc. [K]",
            "Stellar Mass Upper Unc. [Solar mass]",
            "Distance [pc] Lower Unc",
            "Orbit Semi-Major Axis Lower Unc. [au]",
            "Planet Mass or Mass*sin(i) [Jupiter Mass]",
            "Ks (2MASS) Magnitude",
            "Stellar Metallicity Lower Unc. [dex]",
            "Planet Radius Limit Flag.1"]

        # Find the columns that we want to delete and delete them
        deleted_columns = []
        for column in columns_to_remove:
            if column in X_train.columns:
                X_train = X_train.drop(columns=[column])
                deleted_columns.append(column)
            if column in X_test.columns:
                X_test = X_test.drop(columns=[column])
                deleted_columns.append(column)

        # Print the features that are deleted
        if deleted_columns:
            print(f"Deleted {', '.join(deleted_columns)}")
            print(f"X_train column counts: ", X_train.columns.value_counts().sum())
            print(f"X_test. column counts: ", X_test.columns.value_counts().sum())
        return X_train, X_test

    
# columns_exist_in_X_train = check_columns_existence(X_train, columns_to_remove)
# columns_exist_in_y_train = check_columns_existence(y_train, columns_to_remove)

