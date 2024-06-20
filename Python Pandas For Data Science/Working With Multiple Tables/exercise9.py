import codecademylib3
import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

# Concatenate the two menus to form a new menu
menu = pd.concat([bakery, ice_cream])

print(menu)
