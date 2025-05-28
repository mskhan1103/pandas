import pandas as pd 
import numpy as np
"""
A CSV (Comma-Separated Values) file is a simple text file used to store tabular data,
 such as a spreadsheet or database table, in plain text format. Each line in the file 
 represents a row of data, and values in each row are separated by commas. The first 
 line often contains column headers (field names), followed by rows of actual data. 
 CSV files are widely used because they are lightweight, easy to read, and can be 
 opened by many programs like Excel, Google Sheets, and programming languages like
 Python using libraries such as pandas. They are ideal for data exchange between different applications.
"""
# read csv file
ipl=pd.read_csv(r"Dataframe/ipl-matches.csv")
movies=pd.read_csv(r"Dataframe/movies.csv")

print(ipl)
print(movies)
