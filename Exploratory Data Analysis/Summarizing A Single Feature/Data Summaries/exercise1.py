import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print(mean_budget)

# Save the median to med_budget
med_budget = movies.production_budget.median()
print(med_budget)

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()
print(mode_budget)

# Save the trimmed mean to trmean_budget
from scipy.stats import trim_mean

trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2)
print(trmean_budget)

