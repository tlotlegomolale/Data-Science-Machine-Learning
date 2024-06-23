import pandas as pd

movies = pd.read_csv('movies.csv')

# Save the counts to genre_counts
genre_counts = movies.genre.value_counts()
print(genre_counts)
