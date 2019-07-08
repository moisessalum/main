import pandas as pd
from datetime import datetime
import numpy as np


def get_new_record(winner=None, df=None, current_game_index=None):
    # Update team record
    try:
        all_visit_games_array = df[df['visiting_team']==winner].index.values
        all_home_games_array = df[df['home_team']==winner].index.values
        all_team_games = np.concatenate((all_visit_games_array, all_home_games_array), axis=None)
        all_team_games.sort()
        print("Curr:",current_game_index)
        print(all_team_games)
        current_game_ndarray_position = np.where(all_team_games==current_game_index)[0][0]
        if current_game_ndarray_position == 0:
            pass
        elif current_game_ndarray_position > 0:
            previous_game_ndarray_position = current_game_ndarray_position - 1
            next_game_ndarray_position = current_game_ndarray_position + 1
            previous_game = all_team_games[previous_game_ndarray_position]
            print("Prev:",previous_game)
            next_game = all_team_games[next_game_ndarray_position]
            print("Next",next_game)
            previous_record = df[winner].loc[previous_game]
            next_record = previous_record + 1
            print(next_record)
            df.at[next_game, winner] = next_record
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
# teams = df['home_team'].unique()
# for x in teams:
    # df[x] = 0

# Add won games to each team by year
year_list_df = []
# unique_year = df['year'].unique()
unique_year = [1991]
for year in unique_year:
    df_year = df[df['year'] == year]
    df_year['winner_team'] = np.where(df_year['visiting_score'] > df_year['home_score'],
                                      df_year['visiting_team'],
                                      df_year['home_team'])
    for index, row in df_year.iterrows():
        print(index)
        visit_team_visit_games_array = df_year[df_year['visiting_team']==row['visiting_team']].index.values
        visit_team_home_games_array = df_year[df_year['home_team']==row['visiting_team']].index.values
        visit_team_all_games_array = np.concatenate((visit_team_visit_games_array, visit_team_home_games_array), axis=None)
        home_team_visit_games_array = df_year[df_year['visiting_team']==row['home_team']].index.values
        home_team_home_games_array = df_year[df_year['home_team']==row['home_team']].index.values
        home_team_all_games_array = np.concatenate((home_team_visit_games_array, home_team_home_games_array), axis=None)
        visit_team_all_games_array.sort()
        home_team_all_games_array.sort()
        # print(index)
        # print(visit_team_all_games_array)
        # print(home_team_all_games_array)
        visit_team_current_game_ndarray_position = np.where(visit_team_all_games_array==index)[0][0]
        home_team_current_game_ndarray_position = np.where(home_team_all_games_array==index)[0][0]
        # print("VTP:", visit_team_current_game_ndarray_position)
        # print("HTP:", home_team_current_game_ndarray_position)
        if visit_team_current_game_ndarray_position == 0:
            df_year['visit_record'] = 0
        elif visit_team_current_game_ndarray_position > 0:
            visit_current_played_games = visit_team_all_games_array[:visit_team_current_game_ndarray_position]
            visit_game_results = df_year['winner_team'][df_year.index.isin(visit_current_played_games)]
            visit_current_record = len(np.where(visit_game_results==row['visiting_team'])[0])
            df_year.at[index, 'visit_record'] = visit_current_record





        # all_home_games_array = df[df['home_team']==winner].index.values
        # all_team_games = np.concatenate((all_visit_games_array, all_home_games_array), axis=None)


        # if row['visiting_score'] > row['home_score']:
            # winner = row['visiting_team']
            # get_new_record(winner=winner, df=df_year, current_game_index=ix)
        # elif row['visiting_score'] < row['home_score']:
            # winner = row['home_team']
            # get_new_record(winner=winner, df=df_year, current_game_index=ix)
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


