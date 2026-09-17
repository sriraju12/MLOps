import pandas as pd


df = pd.read_csv('matches.csv')

# print(df.info())

# print(df.columns)

# print(df.isnull().sum())

df['city'] = df['city'].fillna('unknown')

df['player_of_match'] = df['player_of_match'].fillna('no award')

df['winner'] = df['winner'].fillna('no winner')

print(df.isnull().sum())

df = df.drop(['umpire1','umpire2'], axis=1)

print(df.columns)

# we need to find how many matches played in a season from starting to till now

season_result = df['season'].value_counts().sort_index()

print(season_result)

# which teamns wins more matches 

team_wins = df['winner'].value_counts()

print(team_wins)

# how many matches ended with no result

match_result = (df['winner'] == "no winner").sum()
print(match_result)


# how many teams win match that they won toss

match_wins = (df['toss_winner'] == df['winner']).sum()
print(match_wins)

# find player of match count

mom = df['player_of_match'].value_counts()
print(mom)

# toss decision like after winning the toss they choose bat or ball

toss_wins =  df['toss_decision'].value_counts()
print(toss_wins)

# which team wins most finals

wins = df[df['match_type'] == 'Final']['winner'].value_counts()
print(wins)




