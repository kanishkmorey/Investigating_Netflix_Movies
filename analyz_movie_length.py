# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')

netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

netflix_movies = netflix_subset[["title","country","genre","release_year","duration"]]

short_movies = netflix_movies[netflix_movies["duration"] < 60]

colors = []
for index, row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append("blue")
    elif row["genre"] == "Documentaries":
        colors.append("green")
    elif row["genre"] == "Stand-Up":
        colors.append("orange")
    else:
        colors.append("red")

fig, ax = plt.subplots()

scatter = ax.scatter(netflix_movies["release_year"], netflix_movies["duration"], c=colors)

ax.set_xlabel("Release year")
ax.set_ylabel("Duration (min)")
ax.set_title("Movie Duration by Year of Release")

plt.show()

answer = "no"