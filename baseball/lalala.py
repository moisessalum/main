import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Read the data
df_full = pd.read_csv('c:/Users/mrodriguez/Desktop/2000_2018.csv')
df_drop = df_full.drop(df_full.columns[0], axis=1)

# Select columns to work on
columns = ['game_number',
           'day_of_week',
           'visiting_team',
           'visiting_league',
           'visiting_team_game_number',
           'home_team',
           'home_league',
           'home_team_game_number',
           'visiting_score',
           'home_score']
df = df_drop[columns]

# Define a new column with the name of the winning team
df['winner_team'] = np.where(df['visiting_score'] > df['home_score'], df['visiting_team'], df['home_team'])

# Separate target from predictors
y = df['winner_team']
X = df
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# Apply label encoder
label_encoder = LabelEncoder()
label_X_train = X_train
label_X_valid = X_valid
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]
for col in object_cols:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_valid[col])

# Model
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(X_train, y_train)

print(X_valid.columns)
# preds = clf.predict(X_valid)
# print(preds)
# print(accuracy_score(y_valid, preds))
