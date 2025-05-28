import numpy as np  # this np and pd is called as alias means synonyms
import pandas as pd

movies=pd.read_csv(r"C:\Users\HTC\Documents\Pandas Pandas\groubby\imdb-top-1000.csv")
print(type(movies))
print(movies.columns)
genres=movies.groupby("Genre")
print(genres)

# applying some aggregate function on the groups we have formed through genres.
"""
print(genres.sum())
print(genres.min())
print(genres.max())
print(genres.mean())
print(genres.median())
#etc
"""
# find top 3 movies based on total earnings(Gross)
print(genres["Gross"].sum().sort_values(ascending=False).head(3))



# find the genres with the higest avg imdb_rating each

print(genres["IMDB_Rating"].mean().sort_values(ascending=False))


# find the director with most popularity
print(movies.groupby("Director")["No_of_Votes"].sum().sort_values(ascending=False))


# find no of movies done by each actor
print(movies["Star1"].value_counts())

#or
print(movies.groupby("Star1")["Star1"].count().sort_values(ascending=False))


# find total no of groups in groupby object.
print(len(genres))

# how to find rows within each group
print(genres.size())



# first()  -> it will print ist movie in each genres
print(genres.first())

#last()
print(genres.first())

#nth()
print(genres.nth(3)) # -> it means we want to print 4th movie in each .

# nunoque() -> it will give us the no of unique values in each group.
print(genres.nunique())

"""
# loops on groupby object
# 
for group,data in genres:
    print(data)
# highest rated movie in each genre
df = pd.DataFrame(columns=movies.columns)
for group,data in genres:
  df = df.append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

print(df)
"""

# split --> apply --> combine.
#print(genres.apply(min))

# custom apply function for groupby onject.
def foo(group):
    return group["Series_Title"].str.startswith("A").sum()

print(genres.apply(foo))

# find ranking of each movie in the group according to IMDB score
def rank(group):
    group["Rank"]=group["IMDB_Rating"].rank(ascending=False)
    return group

print(genres.apply(rank))
# describe function.
print(genres.describe())


# multiple aggregate function in accordance to each group type using dictionary
print(genres.agg({
    'Runtime':'mean',
    'IMDB_Rating':'mean',
    'No_of_Votes':'sum',
    'Gross':'sum',
    'Metascore':'min'
}))


# using lists for applying aggragate function.
print(genres.agg(["min","size"]))


# combining both list and dictionary

print(genres.agg({
    'Runtime':['mean','median'],
    'IMDB_Rating':'mean',
    'No_of_Votes':'sum',
    'Gross':['sum','median'],
    'Metascore':'min'
}))
