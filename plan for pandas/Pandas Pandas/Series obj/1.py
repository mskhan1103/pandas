
import numpy as np
import pandas as pd

# Create a Series with a list of numbers
s=[1,2,3,4,5,6,7,8,9,10]
s=pd.Series(s)
print(s)

# Create a Series with a list of strings
s=['a','b','c','d','e','f','g','h','i','j']
indx=("i","j","k","l","m","n","o","p","q","r")
s=pd.Series(s,index=indx,name="letters")
print(s)


# Create a Series with a dictionary
a = {
    "name": "salman",
    "age": 20,
    "city": "karachi",
    "country": "pakistan",
    "sports": "cricket",
}

d=pd.Series(a)
print(d)

# custom index
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

ms=pd.Series(marks,index=subjects,name="marks")
print(ms)
#attributes of series 
print(ms.size) # size of series
print(ms.shape) # shape of series
print(ms.dtype) # data types of series
print(ms.index) # index of series
print(ms.values) # values of series
print(ms.name) # name of series
print(ms.head()) # first 5 values of series
print(ms.head(2)) # first 2 values of series
print(ms.tail()) # last 5 values of series
print(ms.tail(2)) # last 2 values of series
print(ms.is_unique) # check if series is unique or not returns boolean value (true or false)
#print(ms.is_monotonic) # check if series is monotonic or not returns boolean value (true or false)


#Series using read_csv
abc=pd.read_csv(r"C:\Users\HTC\Documents\Pandas Pandas\ipl-matches.csv")
abc=abc.squeeze(True) # convert dataframe to series
#print(abc)



# series methods 
#generate series with about 1000 random numbers
abc=pd.Series(np.random.randn(1000))
# 1. head() - returns the first n rows of the series
print (abc.head(5)) # first 5 rows of the series
print (abc.tail(5)) # last 5 rows of the series
print (abc.sample(5)) # random 5 rows of the series
print (abc.sample(5,random_state=1)) # random 5 rows of the series with random state
#value counts
print(abc.value_counts()) # count of unique values in the series

# generte a series of batsman name and runs scored by them
import pandas as pd
import numpy as np
batsman = ['sachin', 'virat', 'dhoni', 'sachin', 'virat', 'dhoni', 'sachin', 'virat', 'dhoni']
runs = [100, 200, 300, 400, 500, 600, 700, 800, 900]
batsman = pd.Series(batsman)
runs = pd.Series(runs)
print(batsman)
#sort function
print(runs.sort_values()) # sort the series in ascending order
print(runs.sort_values(ascending=True)) # sort the series in ascending order

print(runs.plot(kind='bar')) # plot the series in bar chart


lst = [1, 2, 3]
result = lst * 2  # This duplicates the list, not element-wise multiply
print(result)     # Output: [1, 2, 3, 1, 2, 3]

import numpy as np

arr = np.array([1, 2, 3])
result = arr * 2  # Vectorized operation
print(result)     # Output: [2 4 6]
