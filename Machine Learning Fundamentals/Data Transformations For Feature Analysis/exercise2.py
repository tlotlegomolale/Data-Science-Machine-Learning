import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')

## add code below
## create ages variable
ages = coffee['age']

## get min and print
min_age = np.min(ages)
print(min_age)

## get max and print
max_age = np.max(ages)
print(max_age)

## print the range
print(max_age - min_age)

## find the mean
mean_age = np.mean(ages)
print(mean_age)

## center ages
centered_ages = ages - mean_age
print(centered_ages)

## graph it
plt.hist(centered_ages)
plt.show();
