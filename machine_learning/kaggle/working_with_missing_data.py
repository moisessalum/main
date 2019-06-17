import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer


# Read the data
X_full = pd.read_csv('train_missing.csv', index_col='Id')
X_test_full = pd.read_csv('test_missing.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full['SalePrice']
X_full.drop(['SalePrice'], axis=1, inplace=True)

# Only use numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# Get shape of training data
# print(X_train.shape)
missing_val_count_by_column = (X_train.isnull().sum())

# Create a function to compare different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# First approach, drop columns with missing values
# Get columns with missing values and drop them
cols_with_miss = [col for col in X_train.columns if X_train[col].isnull().any()]
reduced_X_train = X_train.drop(cols_with_miss, axis=1)
reduced_X_valid = X_valid.drop(cols_with_miss, axis=1)

print('MAE for the dropped columns approach')
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))

# Second approach, imputation
imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(imputer.transform(X_valid))

# Rename columns
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

print('MAE for the imputed approach')
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
