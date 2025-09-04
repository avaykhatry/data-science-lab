#.   Done by Avaya Khatri
##.  4
###. Warming Up Exercise

# Problem 1 - Data read, write and inspect
# Working with bank.csv

import pandas as pd

# load the dataset
dataset1 = pd.read_csv('bank.csv')

# columns with dtypes=object
object_column_1 = dataset1['job']
object_column_2 = dataset1['marital']
object_column_3 = dataset1['education']
object_column_4 = dataset1['default']
object_column_5 = dataset1['housing']
object_column_6 = dataset1['loan']
object_column_7 = dataset1['contact']
object_column_8 = dataset1['month']
object_column_9 = dataset1['poutcome']
object_column_10 = dataset1['y']

# check info
# dataset1.info()

# unique values
print(object_column_1.unique())
print(object_column_2.unique())
print(object_column_3.unique())
print(object_column_4.unique())
print(object_column_5.unique())
print(object_column_6.unique())
print(object_column_7.unique())
print(object_column_8.unique())
print(object_column_9.unique())
print(object_column_10.unique())

# check for total null values
print(dataset1.isnull().sum())

#  Drop all the columns with dtypes object and store in new DataFrame, also write the DataFrame in ”.csv” with name ”banknumericdata.csv”
numeric_dataset = dataset1.drop(columns=['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome', 'y'])
numeric_dataset.to_csv('banknumericdata.csv')
print("\nSuccessfully created 'banknumericdata.csv'!\n")

# Read ”banknumericdata.csv” and Find the summary statistics.
bank_numeric_data = pd.read_csv('banknumericdata.csv')
bank_numeric_data.info()
print(bank_numeric_data.describe())