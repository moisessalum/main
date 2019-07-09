import pandas as pd
from datetime import datetime
import numpy as np


def get_new_record(df=None, team=None, index=None):
    # Update team record
    team_visit_games_array = df[df['visiting_team']==row[team+'_team']].index.values
    team_home_games_array = df[df['home_team']==row[team+'_team']].index.values
    team_all_games_array = np.concatenate((team_visit_games_array, team_home_games_array), axis=None)
    team_all_games_array.sort()
    team_current_game_ndarray_position = np.where(team_all_games_array==index)[0][0]
    if team_current_game_ndarray_position == 0:
        df[team+'_record'] = 0
    elif team_current_game_ndarray_position != 0:
        current_played_games = team_all_games_array[:team_current_game_ndarray_position]
        game_results = df['winner_team'][df.index.isin(current_played_games)]
        current_record = len(np.where(game_results==row[team+'_team'])[0])
        df.at[index, team+'_record'] = current_record

def consecutive_wins_loss(df=None, team=None, index=None):
    # Get consecutive standings
    team_visit_games_array = df[df['visiting_team']==row[team+'_team']].index.values
    team_home_games_array = df[df['home_team']==row[team+'_team']].index.values
    team_all_games_array = np.concatenate((team_visit_games_array, team_home_games_array), axis=None)
    team_all_games_array.sort()
    team_current_game_ndarray_position = np.where(team_all_games_array==index)[0][0]
    if team_current_game_ndarray_position == 0:
        df[team+'_consecutive_record'] = 0
    elif team_current_game_ndarray_position != 0:
        current_played_games = team_all_games_array[:team_current_game_ndarray_position]
        game_results = df['winner_team'][df.index.isin(current_played_games)]
        current_record = np.where(game_results==row[team+'_team'], '1', '-1')
        current_record = current_record.astype(np.int)
        current_record_flip = np.flip(current_record)
        get_first_value = current_record_flip[0]
        consecutive_record = 0
        for i in current_record_flip:
            if i == get_first_value:
                consecutive_record += get_first_value
            else:
                break
        df.at[index, team+'_consecutive_record'] = consecutive_record


# Read data
df = pd.read_csv('1991_2018.csv', index_col=0)

# Convert dates and create new columns
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df = df.sort_index()

# Add won games to each team by year
year_list_df = []
# unique_year = df['year'].unique()
unique_year = [1991]
for year in unique_year:
    df_year = df[df['year'] == year]
    df_year['winner_team'] = np.where(df_year['visiting_score'] > df_year['home_score'],
                                      df_year['visiting_team'],
                                      df_year['home_team'])
    df_year['winner_home_visit'] = np.where(df_year['visiting_score'] > df_year['home_score'],
                                            'visiting_team',
                                            'home_team')
    for index, row in df_year.iterrows():
        get_new_record(df=df_year, team='visiting', index=index)
        get_new_record(df=df_year, team='home', index=index)
        consecutive_wins_loss(df=df_year, team='visiting', index=index)
        consecutive_wins_loss(df=df_year, team='home', index=index)
    print('Done', year)
    year_list_df.append(df_year)

# Write CSV
result = pd.concat(year_list_df)
result.to_csv('result.csv')
