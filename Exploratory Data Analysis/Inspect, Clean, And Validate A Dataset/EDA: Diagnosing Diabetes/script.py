import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())
print(diabetes_data.info())

#Do any of the columns include null values
print(diabetes_data.isnull().values.any())

#Data Summation
print(diabetes_data.describe())

# replace instances of 0 with NaN
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

# find whether columns contain null values after replacements are made
diabetes_data.isnull().values.any()

# print rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# print unique values of Outcome column
print(diabetes_data['Outcome'].unique())

diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O',0)
diabetes_data['Outcome'] = diabetes_data['Outcome'].apply(pd.to_numeric)
diabetes_data['Outcome'].unique()
print(diabetes_data.describe())
