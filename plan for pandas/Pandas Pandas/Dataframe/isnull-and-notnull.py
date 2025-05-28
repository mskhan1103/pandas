import numpy as np
import pandas as pd
students=[[10,20,22,22],
          [11,2,211,np.nan],
          [3,4,5,6]]
std=pd.DataFrame(students,columns=["a","b","c","d"])
print(std)

#is null
print(std.isnull())

#not null
print(std.notnull())

#hasnan
print(std["d"].hasnans)


#dropna
print(std.dropna())


students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)


print(students.isnull())
print(students.notnull())
print(students["name"].hasnans)



# dropna -> used to remove all the nan values
print(students.dropna()) # pre-built attribute is that dropna used is how = "any" which means it will delete all the rows that have atleast one nan value..
print(students.dropna(how='all')) # here it will delete only those rows that are compltely null.
##################################
print(students.dropna(subset=['name']))