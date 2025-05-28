import pandas as pd
import numpy as np

ipl=pd.read_csv(r"Dataframe/ipl-matches.csv")
movies=pd.read_csv(r"Dataframe/movies.csv")
print(ipl)
"""
mask = ipl['MatchNumber'] == 'Final'
new_df = ipl[mask]
new_d=new_df[['Season','WinningTeam']]
print(new_d)
"""

#Challenge 1: Filter by Team
#Get all matches where Mumbai Indians played (either as Team1 or Team2).
#print(ipl[(ipl["Team1"]=="Mubai Indians") | (ipl["Team2"]=="Mumbai Indians")])

#Find the team with the most match wins in total.
#print(ipl["WinningTeam"].value_counts())
#mostwin=ipl["WinningTeam"].value_counts()
#print(mostwin["WiningTeam"][0])
#mostwin = ipl["WinningTeam"].value_counts()
#print(f"The team with the most wins is {mostwin.index[0]} with {mostwin.iloc[0]} wins.")


#Find out in how many matches the toss winner also won the match.
#print(ipl[ipl["TossWinner"]==ipl["WinningTeam"]])



#List all matches played in Mumbai and show the teams involved.
print(ipl[ipl["City"] == "Mumbai"][["Team1", "Team2"]])



