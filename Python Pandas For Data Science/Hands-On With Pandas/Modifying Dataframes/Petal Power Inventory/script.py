import codecademylib3
import pandas as pd

# Load the inventory data
inventory = pd.read_csv("inventory.csv")

# Display the first 10 rows of the inventory DataFrame
print("First 10 rows of inventory:")
print(inventory.head(10))

# Select rows for the Staten Island location
staten_island = inventory[inventory['location'] == 'Staten Island']
print("\nStaten Island inventory:")
print(staten_island)

# Extract the product descriptions for the Staten Island location
product_request = staten_island['product_description']
print("\nProduct descriptions for Staten Island:")
print(product_request.head(10))

# Select rows where location is Brooklyn and product type is seeds
seed_request = inventory.loc[
    (inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')
]
print("\nSeed products at Brooklyn location:")
print(seed_request.head(10))

# Add a column 'in_stock' indicating if the product is in stock
inventory['in_stock'] = inventory['quantity'] > 0

# Add a column 'total_value' equal to price multiplied by quantity
inventory['total_value'] = inventory['price'] * inventory['quantity']
print("\nInventory with 'in_stock' and 'total_value' columns:")
print(inventory.head(10))

# Define a lambda function to combine product type and description
combine_lambda = lambda row: f"{row.product_type} - {row.product_description}"

# Add a column 'full_description' using the combine_lambda function
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print("\nInventory with 'full_description' column:")
print(inventory.head(10))
