import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# Your manager wants to know which ad platform is getting you the most views. How many views (i.e., rows of the table) came from each utm_source?
views = ad_clicks.groupby('utm_source').user_id.count().reset_index().rename(columns = {'user_id': 'views'})
print(views)

# Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].apply(lambda row: False if pd.isnull(row) else True)
print(ad_clicks.head())

# We want to know the percent of people who clicked on ads from each utm_source. Start by grouping by utm_source and is_click and counting the number of user_id's in each of those groups. Save your answer to the variable clicks_by_source. 
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)
# Now let's pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.Save your results to the variable clicks_pivot.
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id')
print(clicks_pivot.head())
# Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source. Was there a difference in click rates for each source? - Facebook and Google have slightly higher click rates.
clicks_pivot['percent_clicked'] = 100*clicks_pivot[True] / (clicks_pivot[True]+clicks_pivot[False])
print(clicks_pivot.head())

# Were approximately the same number of people shown both adds? -> My answer: yes.
a_or_b = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(a_or_b)

# Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.
ad_efficiency = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
print(ad_efficiency)
ad_efficiency_pivot = ad_efficiency.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()
ad_efficiency_pivot['percentage_clicks'] = 100*ad_efficiency_pivot[True] / (ad_efficiency_pivot[True]+ad_efficiency_pivot[False])
print(ad_efficiency_pivot)

# The Product Manager for the A/B test thinks that the clicks might have changed by day of the week. Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks.head())
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_clicks = a_clicks.groupby(['day','is_click']).user_id.count().reset_index()
print(a_clicks)
a_clicks = a_clicks.pivot(columns='is_click', index='day', values='user_id').reset_index()
print(a_clicks)
a_clicks['percent'] = 100*a_clicks[True] / (a_clicks[True]+a_clicks[False])
print(a_clicks)
b_clicks = b_clicks.groupby(['day','is_click']).user_id.count().reset_index()
b_clicks = b_clicks.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_clicks['percent'] = 100*b_clicks[True] / (b_clicks[True]+b_clicks[False])
print(b_clicks)

