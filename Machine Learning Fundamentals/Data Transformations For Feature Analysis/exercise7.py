import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn 

coffee = pd.read_csv('starbucks_customers.csv')
ages = coffee['age']

## add code below
## print min and max
print(np.min(ages))
print(np.max(ages))

## set bins
age_bins = [12, 20, 30, 40, 71]

## new column
coffee['binned_ages'] = pd.cut(ages, age_bins, right = False)

## print first 10 rows
print(coffee['binned_ages'].head(10))

## graph it
coffee['binned_ages'].value_counts().plot(kind='bar')
plt.show()
