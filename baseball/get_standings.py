import requests
from bs4 import BeautifulSoup
import pandas as pd
from table_columns import columns


df = pd.read_csv('/Users/moisessalum/Desktop/GL2018.TXT')

# df.columns = columns


print(df.shape)
print(df)
