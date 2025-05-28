import numpy as np
import pandas as pd
students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
print(students)
# dropna -> means deleting of nan values.
print(students.dropna())# it will remove all the rows bc it have default attribute of how="any".
print(students.dropna(how="all"))
print(students["name"].dropna())
print(students.dropna(subset=["name"]))
print(students.dropna(subset=["name","college"]))


#fillna -> menas filling of nan values.
print(students.fillna("unknown"))

print(students['name'].fillna('unknown'))

print(students['name'].fillna(method='bfill')) # backward fill.
print(students['name'].fillna(method='ffill')) # forward fill.