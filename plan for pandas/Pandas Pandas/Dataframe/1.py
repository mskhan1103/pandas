import numpy as np
import pandas as pd
# data frame using list

lst=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
s=pd.DataFrame(lst)
print(s)

# data frame using dictionary
dict={
    "name": ["salman", "ali", "ahmed", "sara", "sana"],
    "age": [20, 21, 22, 23, 24],
    "city": ["karachi", "lahore", "islamabad", "peshawar", "quetta"],
    "country": ["pakistan", "india", "bangladesh", "nepal", "bhutan"],
    "sports": ["cricket", "football", "hockey", "tennis", "badminton"],
}
s=pd.DataFrame(dict)
print(s)
#import attributes of data frame
print(s.size) # size of data frame
print(s.shape) # shape of data frame
print(s.dtypes) # data types of data frame
print(s.index) # index of data frame
print(s.columns) # columns of data 
# frame
print(s.values) # values of data frame
print(s.name) # name of data frame
print(s.head()) # first 5 values of data frame
print(s.head(2)) # first 2 values of data frame
print(s.tail()) # last 5 values of data frame




#read csv file
ipl=pd.read_csv(r"Dataframe/ipl-matches.csv")
print(ipl)


movies=pd.read_csv(r"Dataframe/movies.csv")
print(movies)

# shape attributes of data frame
print("shape of ipl csv file is: ",ipl.shape) # shape of data frame
# dtypes of data frame
print("dtypes of ipl csv file is: ",ipl.dtypes) # data types of data frame


print("movies coloumns",movies.columns)# coloumns of data frame

# head and tail of data frame
print("head of ipl csv file is: ",ipl.head()) # first 5 values of data frame
print("head of ipl csv file is: ",ipl.head(2)) # first 2 values of data frame
print("tail of ipl csv file is: ",ipl.tail()) # last 5 values of data frame
print("tail of ipl csv file is: ",ipl.tail(2)) # last 

# Filtering data frame
# find all the final winners
mask = ipl['MatchNumber'] == 'Final'
new_df = ipl[mask]
new_df[['Season','WinningTeam']]

print(ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']])

print(ipl.head(1))

# how many matches has csk won in kolkata
#ipl["City"]=="kolkata" & ipl["WinnningTeam"]=="csk"
#print(ipl[ipl["City"]=="kolkata" & ipl["WinningTeam"]=="csk"].shape[0])
winningteam=ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0]
print("CSK won",winningteam,"matches in kolkata")


#(ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100
print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)

# movies with rating higher than 8 and votes>10000
print(movies.head(1))
print(movies[(movies["imdb_rating"]>8) & (movies["imdb_votes"]>10000)].shape[0])