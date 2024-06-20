import codecademylib3
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

orders_products = pd.merge(
	orders,
	products.rename(columns={'id':'product_id'})
)
print(orders_products)
