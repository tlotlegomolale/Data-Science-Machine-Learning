import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print(orders)
print(products)

merged_df = pd.merge(orders, products)

print(merged_df)
