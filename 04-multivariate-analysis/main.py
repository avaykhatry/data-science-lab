# Multivariate Analysis
# by Avaya Khatri

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')
df.info()

# Problem 1. Bi-variate Analysis (Scatter Plot)
plt.figure(figsize=(8,6))
plt.scatter(df['Age'], df['Fare'], c=df['Survived'], cmap='bwr', alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Fare vs Age colored by Survival (0=Not Survived, 1=Survived)")
plt.colorbar(label="Survived")
plt.show()

# Problem 2. Multivariate Analysis (Pair Plot)
# select columns
subset = df[['Age', 'Fare', 'Pclass', 'Survived']]

# pair plot with survival as hue
sns.pairplot(subset, hue='Survived', diag_kind='kde', palette='bwr')
plt.suptitle("Pair Plot: Age, Fare, Pclass vs Survived", y=1.02)
plt.show()

# Problem 3. Multivariate Analysis (Covariance Heatmap)
# select numerical columns
num_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# compute correlation matrix
corr_matrix = df[num_cols].corr()

# heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0)
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

print(corr_matrix)

