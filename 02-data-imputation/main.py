# done by avaya
# Problem 1 - Data Imputations

import pandas as pd

# load dataset
da_se = pd.read_csv('medical_students_dataset.csv')

# check info
da_se.info()

# identify missing (null) values
print(f"\nNull values:\n{da_se.isnull().sum()}\n")

da_se_numerical = da_se.select_dtypes(include=['float64'])
da_se_categorical = da_se.select_dtypes(include=['object'])

# Using mean value to fill missing values for numerical columns because the most values had very little difference
da_se_numerical_mean = da_se_numerical.fillna(da_se_numerical.mean())
print(da_se_numerical_mean)

# Dropping missing values in categorical column because of difficulty in guessing the values because of its binary type
da_se_categorical_drop = da_se_categorical.dropna()
print(da_se_categorical_drop)

# checking for any duplicate values
print(f"There are {da_se.duplicated().sum()} duplicate items.")

# managin duplicate items
no_duplicates = da_se.drop_duplicates()
print("Duplicate items dropped!")
print("Checking duplicate items...")
no_duplicates.info()
print(f"Now, there are {no_duplicates.duplicated().sum()} duplicate items.")