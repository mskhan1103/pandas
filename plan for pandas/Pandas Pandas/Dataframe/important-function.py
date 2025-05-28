# data frame using dictionary
import pandas as pd
import numpy as np
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
