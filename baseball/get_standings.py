import pandas as pd
from datetime import datetime
import numpy as np


def get_new_record(winner=None, df=None, ix=None):
    # Update team record
    try:
        winner = row['visiting_team']
        all_visit_games_array = df_year[df_year['visiting_team']==winner].index.values
        all_home_games_array = df_year[df_year['home_team']==winner].index.values
        all_team_games = np.concatenate((all_visit_games_array, all_home_games_array), axis=None)
        current_index = np.where(all_team_games==ix)[0][0]
        if current_index == 0:
            pass
        elif current_index > 0:
            previous_index = current_index - 1
            previous_game = all_team_games[previous_index]
            print("PG", previous_game)
            previous_record = df[winner].iloc[previous_game]
            print("Prev rec", previous_record)
            next_index = current_index + 1
            next_game = all_team_games[next_index]
            # print("Next ix", next_index)
            next_record = previous_record + 1
            # print("Next rec", next_record)
            df_year[winner].iloc[next_game] = next_record
            print(df_year[winner].iloc[next_game])
    except Exception as e:
        print("Visiting score exception:", e)


# Read data
df = pd.read_csv('1991_2018.csv', index_col=0)

# Convert dates and create new columns
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df = df.sort_index()

# Get teams list and add to df
teams = df['home_team'].unique()
for x in teams:
    df[x] = 0

# Add won games to each team by year
year_list_df = []
# unique_year = df['year'].unique()
unique_year = [1991]
for year in unique_year:
    df_year = df[df['year'] == year]
    for ix, row in df_year.iterrows():
        print(ix)
        # print(row['visiting_team'])
        # print(row['home_team'])
        if row['visiting_score'] > row['home_score']:
            winner = row['visiting_team']
            get_new_record(winner=winner, df=df_year, ix=ix)
        elif row['visiting_score'] < row['home_score']:
            winner = row['home_team']
            get_new_record(winner=winner, df=df_year, ix=ix)
    print('Done', year)
    year_list_df.append(df_year)

# Write CSV
result = pd.concat(year_list_df)
result.to_csv('result.csv')




# print(df.tail())


# years = range(1991, 2018)

# df_list = []
# for i in years:
    # df_n = pd.read_csv('GL{}.txt'.format(i), header=None)
    # df_list.append(df_n)

# result = pd.concat(df_list, ignore_index=True)

# result.columns = columns

# df = df.append(result, ignore_index=True)
# df.to_csv('historic_1991_2018.csv')


