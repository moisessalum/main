import pandas as pd
from datetime import datetime

# Read data
df = pd.read_csv('1991_2018.csv', index_col=0)

# Convert dates and create new columns
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df = df.sort_values(by='date')

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
        if row['visiting_score'] > row['home_score']:
            # df_year[row['visiting_team']] = df_year[row['visiting_team']] + 1
            print(ix)
            index_list = df_year.loc[df_year['visiting_team']==row['visiting_team']].index.values
            print(index_list)
            list_value = index_list.index(ix)
            print(list_value)
        else:
            df_year[row['home_team']] = df_year[row['home_team']] + 1
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


