import pandas as pd

# reading 1 csv file from the website
df_premier21 = pd.read_csv(
    'https://www.football-data.co.uk/mmz4281/2122/E0.csv')
# showing dataframe
# print(df_premier21)
# rename columns
df_premier21.rename(columns={'FTHG': 'home_goals',
                    'FTAG': 'away_goals'}, inplace=True)
# show dataframe
print(df_premier21)
