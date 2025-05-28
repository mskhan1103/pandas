import pandas as pd
import numpy as np
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'David'],
    'Age': [25, 30, np.nan, 25, 30, 35],
    'Score': [85, 90, 95, 85, np.nan, 70]
})
print("Sample DataFrame:\n", df)
# 1. value_counts() - Count repeated rows in a series and data frame means count frequency count.
print("1. value_counts:\n", df['Name'].value_counts())

# 2. sort_values() - Sort by values
print("\n2. sort_values by Score:\n", df.sort_values(by='Score'))

# 3. rank() - Rank values (NaNs get NaN rank)
print("\n3. rank of Score:\n", df['Score'].rank())

# 4. sort_index() - Sort DataFrame by index
df_sorted = df.sort_index(ascending=False)
print("\n4. sort_index (descending):\n", df_sorted)

# 5. set_index() - Set 'Name' as index
df_indexed = df.set_index('Name')
print("\n5. set_index to Name:\n", df_indexed)

# 6. rename() - Rename columns and index
print("\n6. rename columns:\n", df.rename(columns={'Score': 'Marks'}))

# 7. reset_index() - Reset index to default integers
df_reset = df_indexed.reset_index()
print("\n7. reset_index:\n", df_reset)

# 8. unique() and nunique()
print("\n8. unique Names:", df['Name'].unique())
print("   nunique Names:", df['Name'].nunique())

# 9. isnull(), notnull(), hasnans
print("\n9. isnull:\n", df.isnull())
print("   notnull:\n", df.notnull())
print("   Score has NaNs:", df['Score'].hasnans)

# 10. dropna() - Drop rows with any NaN
print("\n10. dropna:\n", df.dropna())

# 11. fillna() - Fill NaNs with a value
print("\n11. fillna (Score=0, Age=999):\n", df.fillna({'Score': 0, 'Age': 999}))

# 12. drop_duplicates() - Remove duplicate rows
print("\n12. drop_duplicates:\n", df.drop_duplicates())

# 13. drop() - Drop a column
print("\n13. drop column 'Age':\n", df.drop(columns='Age'))

# 14. apply() - Apply function to column
df['Score_x2'] = df['Score'].apply(lambda x: x * 2 if pd.notnull(x) else x)
print("\n14. apply lambda to double Score:\n", df)

# 15. isin() - Check if elements in list
print("\n15. isin ['Alice', 'David']:\n", df['Name'].isin(['Alice', 'David']))

# 16. corr() - Correlation between numeric columns
print("\n16. corr:\n", df.corr(numeric_only=True))

# 17. nlargest and nsmallest
print("\n17. nlargest Score:\n", df['Score'].nlargest(2))
print("    nsmallest Score:\n", df['Score'].nsmallest(2))

# 18. insert() - Insert new column at position 1
df.insert(1, 'Country', ['US', 'UK', 'US', 'US', 'UK', 'US'])
print("\n18. insert column 'Country':\n", df)

# 19. copy() - Create a deep copy of the DataFrame
df_copy = df.copy()
df_copy.loc[0, 'Name'] = 'Changed'
print("\n19. copy - Original DataFrame remains unchanged:\n", df)




# working with csv files
ipl=pd.read_csv(r"Dataframe/ipl-matches.csv")

# 1 count_value function examples 
# find which player has won most potm -> in finals and qualifiers
print(ipl.head(1))
#ipl = pd.read_csv('ipl-matches.csv')
#ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()
print(ipl[~ipl["MatchNumber"].str.isdigit()]['Player_of_Match'].value_counts())

#toss decision plot
print(ipl["TossDecision"].value_counts().plot(kind="pie"))
print(ipl["TossDecision"].value_counts())

# how many matches each team has played
print(ipl['Team2'].value_counts()+ ipl['Team1'].value_counts().sort_values(ascending=False))
"""
ipl=pd.read_csv(r"Dataframe\ipl-matches.csv")
print(ipl.head(2))


print(ipl.value_counts())
"""