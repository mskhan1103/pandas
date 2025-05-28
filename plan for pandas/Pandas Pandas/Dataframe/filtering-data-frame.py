# Filtering data frame
# find all the final winners

import pandas as pd
import numpy as np
ipl=pd.read_csv(r"Dataframe/ipl-matches.csv")
movies=pd.read_csv(r"Dataframe/movies.csv")
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


# Action movies with rating higher than 7.5
#print(movies[movies["genres"].str.split("|").apply(lambda x:"Action" in x) & (movies["imbd_rating"]>7.5)])
#print(movies[movies["genres"].str.contains("Action")])


# write a function that can return the track record of 2 teams against each other
def track_record(team1, team2):
    # Filter matches where either team1 or team2 played against each other
    matches = ipl[((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | 
                  ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))]
    
    # Count wins for each team
    team1_wins = matches[matches['WinningTeam'] == team1].shape[0]
    team2_wins = matches[matches['WinningTeam'] == team2].shape[0]
    total_matches = matches.shape[0]
    
    # Print the track record
    print(f"Track record between {team1} and {team2}:")
    print(f"{team1} won {team1_wins} matches.")
    print(f"{team2} won {team2_wins} matches.")
    print(f"Total matches played: {total_matches}")

# Example usage
track_record("Chennai Super Kings", "Royal Challengers Bangalore")


# here is the detailed version
def track_record(team1, team2):
    # Filter matches where either team1 or team2 played against each other
    matches = ipl[((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | 
                  ((ipl['Team1'] == team2) & (ipl['Team2'] == team1))]
    
    # Count wins for each team
    team1_wins = matches[matches['WinningTeam'] == team1].shape[0]
    team2_wins = matches[matches['WinningTeam'] == team2].shape[0]
    total_matches = matches.shape[0]
    
    # Count tied matches and no results
    tied_matches = matches[matches['WinningTeam'].isna()].shape[0]  # Assuming NaN for ties/no results
    no_results = matches[matches['Result'] == 'No Result'].shape[0] if 'Result' in matches.columns else 0

    # Calculate win percentages
    team1_win_percentage = (team1_wins / total_matches) * 100 if total_matches > 0 else 0
    team2_win_percentage = (team2_wins / total_matches) * 100 if total_matches > 0 else 0

    # Print the track record
    print(f"Track record between {team1} and {team2}:")
    print(f"{team1} won {team1_wins} matches ({team1_win_percentage:.2f}%).")
    print(f"{team2} won {team2_wins} matches ({team2_win_percentage:.2f}%).")
    print(f"Tied matches: {tied_matches}")
    print(f"No results: {no_results}")
    print(f"Total matches played: {total_matches}")

# Example usage
track_record("Chennai Super Kings", "Royal Challengers Bangalore")


# Find all matches played in Mumbai
print("matches played in mumbai is",ipl[ipl["City"]=="Mumbai"].shape[0])

# Find all matches won by Mumbai Indians
print("matches won by mubai indians",ipl[ipl["WinningTeam"]=="Mumbai Indians"].shape[0])

# Matches where TossWinner is the same as WinningTeam
toss_and_match_wins = ipl[ipl['TossWinner'] == ipl['WinningTeam']]
print(toss_and_match_wins)

# Find matches won by a margin of more than 50 runs
big_wins = ipl[(ipl['WinMargin'] > 50) & (ipl['WinMarginType'] == 'runs')]
print(big_wins)

# Find matches where MS Dhoni was the Player of the Match
dhoni_pom = ipl[ipl['Player_of_Match'] == 'MS Dhoni']
print(dhoni_pom)

# Find all matches played in the 2020 season
season_2020 = ipl[ipl['Season'] == 2020]
print(season_2020)


# Find all matches where Royal Challengers Bangalore played
rcb_matches = ipl[(ipl['Team1'] == 'Royal Challengers Bangalore') | (ipl['Team2'] == 'Royal Challengers Bangalore')]
print(rcb_matches)

# Find all matches that ended with no result
no_result_matches = ipl[ipl['Result'] == 'No Result']
print(no_result_matches)

# Find all matches where Kolkata Knight Riders lost
kkr_losses = ipl[(ipl['Team1'] == 'Kolkata Knight Riders') | (ipl['Team2'] == 'Kolkata Knight Riders')]
kkr_losses = kkr_losses[kkr_losses['WinningTeam'] != 'Kolkata Knight Riders']
print(kkr_losses)


# Find movies with more than 50,000 votes
popular_movies = movies[movies['imdb_votes'] > 50000]
print(popular_movies)

# Find movies with IMDb rating between 7 and 8
rating_range_movies = movies[(movies['imdb_rating'] >= 7) & (movies['imdb_rating'] <= 8)]
print(rating_range_movies)

# Find all movies directed by Christopher Nolan
nolan_movies = movies[movies['director'] == 'Christopher Nolan']
print(nolan_movies)

# Find all movies released in 2020
movies_2020 = movies[movies['release_year'] == 2020]
print(movies_2020)