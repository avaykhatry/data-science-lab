# Data Cleaning and Transformation
# done by Avaya Khatri

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('titanic.csv')
# dataset.info()

# Problem 1. create dataframe
subsetted_dataset = dataset[['Name', 'Pclass', 'Sex', 'Age', 'Fare', 'Survived']].copy()
# print(subsetted_dataset.head())

subsetted_dataset_pclass_one = subsetted_dataset[subsetted_dataset['Pclass'] == 1]
print(subsetted_dataset_pclass_one['Fare'].describe())

# Problem 2. null values in 'Age' column
print(f"There are {subsetted_dataset['Age'].isnull().sum()} null values.")

print(subsetted_dataset)

## dropping them from dataframe
subsetted_dataset_dropna = subsetted_dataset.dropna(subset=['Age'])
print(subsetted_dataset_dropna)

# Problem 3. one-hot encoding

# 1. One-hot encode 'Embarked'
embarked_dummies = pd.get_dummies(dataset['Embarked'], prefix='Embarked')

# 2. Add new columns to DataFrame
new_dataset = pd.concat([dataset, embarked_dummies], axis=1)

# 3. Drop original 'Embarked' column
new_dataset.drop(columns=['Embarked'], inplace=True)

# 4. Print first few rows
print(new_dataset.head())

# Problem 4. comparing mean survival and visualization
print(dataset.groupby('Sex')['Survived'].mean())

# Plot
dataset.groupby('Sex')['Survived'].mean().plot(kind='bar', color=['olive', 'maroon'])
plt.title("Survival Rates by Gender")
plt.ylabel("Mean Survival Rate")
plt.show()

#Problem 5. survival by port of embarkation
print(dataset.groupby('Embarked')['Survived'].mean())

# Plot
dataset.groupby('Embarked')['Survived'].mean().plot(kind='bar', color=['violet', 'indigo', 'purple'])
plt.title("Survival Rates by Port of Embarkation")
plt.ylabel("Mean Survival Rate")
plt.show()

# Problem 6. 
# Break Age into 5 quantiles
dataset['AgeGroup'] = pd.qcut(dataset['Age'], 5)

# Compare survival means by Pclass & AgeGroup
survival_rates = dataset.groupby(['Pclass', 'AgeGroup'])['Survived'].mean()
print(survival_rates)

# Pivot for easier plotting
pivot_table = dataset.pivot_table(values='Survived', index='AgeGroup', columns='Pclass')

# Plot
pivot_table.plot(kind='bar')
plt.title("Survival Rates by Age Group & Passenger Class")
plt.ylabel("Mean Survival Rate")
plt.xlabel("Age Group")
plt.legend(title="Pclass")
plt.show()