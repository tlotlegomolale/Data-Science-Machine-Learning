import pandas as pd 

## add code below
## set up dataframe
coffee = pd.read_csv('starbucks_customers.csv')

## print the column names
print(coffee.columns)

## get information on your data
print(coffee.info())
