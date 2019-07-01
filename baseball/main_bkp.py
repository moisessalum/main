import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


# Read the data
file_path = 'c:/Users/mrodriguez/Desktop/1991_2018.csv'
df_full = pd.read_csv(file_path, index_col=0)

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
           'home_score',
           'park_id']
df = df_full[columns]

# Define a new column with the name of the winning team
df['winner_team'] = np.where(df['visiting_score'] > df['home_score'], df['visiting_team'], df['home_team'])

# Separate target from predictors
y = df['winner_team']
X = df.drop(['winner_team'], axis=1)
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# Select object columns
object_cols = [col for col in X.columns if X[col].dtype == "object"]

# Apply label encoder
label_encoder = LabelEncoder()
label_X_valid = X_valid
label_X_train = X_train
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]
for col in object_cols:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_valid[col])

# Set scores to zero
X_valid['home_score'] = 0
X_valid['visiting_score'] = 0

# Naive Bayes Classifier
nb = GaussianNB()
nb.fit(X_train, y_train)
preds_nb = nb.predict(X_valid)
print("NB: ", accuracy_score(y_valid, preds_nb))

# Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(X_train, y_train)
preds_rf = clf.predict(X_valid)
print("RFC: ", accuracy_score(y_valid, preds_rf))

# Bagging Classifier
bc = BaggingClassifier(KNeighborsClassifier(), max_samples=0.5, max_features=0.5)
bc.fit(X_train, y_train)
preds_bc = bc.predict(X_valid)
print("BC: ", accuracy_score(y_valid, preds_bc))

# AdaBoost Classifier
abc = AdaBoostClassifier(n_estimators=100)
abc.fit(X_train, y_train)
preds_abc = abc.predict(X_valid)
print("AB: ", accuracy_score(y_valid, preds_abc))

# Gradient Boosting Classifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
preds_gbc = gbc.predict(X_valid)
print("GBC: ", accuracy_score(y_valid, preds_gbc))
