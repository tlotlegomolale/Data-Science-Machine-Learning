import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
print(visits.head())
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
print(cart.head())
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
print(checkout.head())
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(purchase.head())

# Combine visits and cart using a left merge.
visits_cart = pd.merge(visits,cart, how='left')
all_visits = len(visits_cart)
print(all_visits)

# How many of the timestamps are null for the column cart_time? What do these null rows mean? -> 1652 of the website's visitors did not put anything in their cart.
empty_cart = len(visits_cart[visits_cart.cart_time.isnull()])
print(empty_cart)

# What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print('Percent of users who visited Cool T-Shirts but did not place a t-shirt in their cart: ', 100*float(empty_cart)/all_visits)

# Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout, how='left')
all_cart = len(cart_checkout)
no_checkout = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print('Percentage of users who put items in their cart, but did not proceed to checkout: ', 100*float(no_checkout)/all_cart)

# Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data. Examine the result using print and head.
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head())

# What percentage of users proceeded to checkout, but did not purchase a t-shirt? -> 16.89%
checkout = len(all_data[all_data.checkout_time.notnull()])
print(checkout)
no_purchase = len(all_data[(all_data.purchase_time.isnull()) & (all_data.checkout_time.notnull())])
print(no_purchase)
print('Percentage of users who proceeded to checkout, but did not purchase a t-shirt: ', 100*float(no_purchase)/checkout)

# Which step of the funnel is weakest -> the first one (users who visited the website but did not place a t-shirt in their cart): 82.6%.

# Using the giant merged DataFrame all_data that you created, let us calculate the average time from initial visit to final purchase. 
all_data['time_to_purchase'] = all_data['purchase_time']- all_data['visit_time']
print(all_data['time_to_purchase'])
print(all_data.time_to_purchase.mean())
