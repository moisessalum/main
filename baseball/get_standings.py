import pandas as pd


df = pd.read_csv('c:/Users/mrodriguez/Desktop/GL2018.csv')
columns = df.columns

years = range(2000, 2018)

df_list = []
for i in years:
    df_n = pd.read_csv('c:/users/mrodriguez/Desktop/GL{}.txt'.format(i), header=None)
    df_list.append(df_n)

result = pd.concat(df_list)

result.columns = columns

df = df.append(result)
df.to_csv('c:/Users/mrodriguez/Desktop/2000_2018.csv')
