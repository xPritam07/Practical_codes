import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
ratings = pd.read_csv("rating.csv")
ratings.head()
movies = pd.read_csv("movies.csv")
movies.head()
n_ratings = len(ratings)
n_movies = len(ratings['movieId'].unique())
n_users =len(ratings['userId'].unique())
print(f"Number of ratings: {n_ratings}")
print(f"Number ofunique movieId's: {n_movies}")
print(f"Number of unique users: {n_users}")
print(f"Average ratings per user: {round(n_ratings/n_users, 2)}")
print(f"Average ratings per movie: {round(n_ratings/n_movies, 2)}")