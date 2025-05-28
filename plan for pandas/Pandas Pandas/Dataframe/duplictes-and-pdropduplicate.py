import numpy as pd
import pandas as pd

# duplicates
temp = pd.Series([1,1,1,2,3,3,4,4])
print(temp)
# It will remove all the duplicates.
print(temp.drop_duplicates())
print(temp.drop_duplicates())

tem = pd.Series([1,2,3,4,4])
print(tem.drop_duplicates(keep="last"))