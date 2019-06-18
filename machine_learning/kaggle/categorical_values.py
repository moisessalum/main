import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Read the data
X = pd.read_csv('train.csv', index_col='Id')
X_test = pd.read_csv('test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X['SalePrice']
X.drop(['SalePrice'], axis=1, inplace=True)

# Drop columns with missing values (to keep things simple)
cols_with_miss = [col for col in X.columns if X[col].isnull().any()]
X.drop(cols_with_miss, axis=1, inplace=True)
X_test.drop(cols_with_miss, axis=1, inplace=True)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

def score_model(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Drop columns with categorical data
drop_X_train = X_train.select_dtypes(exclude=['object'])
drop_X_valid = X_valid.select_dtypes(exclude=['object'])

print('MAE for dropping categorical values')
print(score_model(drop_X_train, drop_X_valid, y_train, y_valid))

# Label encoding data approach
# print(X_train['Condition2'].unique())
# print(X_valid['Condition2'].unique())

# Get all categorial columns
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]
good_label_columns = [col for col in object_cols if set(X_train[col]) == set(X_valid[col])]
bad_label_columns = list(set(object_cols)-set(good_label_columns))
# print("Good label columns: ", good_label_columns)
# print("Bad label columns: ", bad_label_columns)

# Drop columns not being encoded and apply label encoder
label_X_train = X_train.drop(bad_label_columns, axis=1)
label_X_valid = X_valid.drop(bad_label_columns, axis=1)
label_encoder = LabelEncoder()
for col in good_label_columns:
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_valid[col])

print('MAE label encoding')
print(score_model(label_X_train, label_X_valid, y_train, y_valid))

# One hot encoding data approach
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))
# print('Columns that will be one hot encoded: ', low_cardinality_cols)
# print('Columns that will be dropped: ', high_cardinality_cols)

OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

print('MAE one hot encoding')
print(score_model(OH_X_train, OH_X_valid, y_train, y_valid))
