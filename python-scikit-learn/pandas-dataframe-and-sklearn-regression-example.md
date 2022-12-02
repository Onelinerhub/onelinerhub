# Pandas dataframe and Sklearn regression example

```python
import pandas as pd
from sklearn import linear_model, model_selection

data = pd.read_csv('/var/www/examples/housing.csv')

X = data.loc[:, ['housing_median_age', 'total_rooms']]
y = data.median_house_value

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `pd.read_csv` - read data from csv file into dataframe
- `['housing_median_age', 'total_rooms']` - select those columns to be used as features
- `data.median_house_value` - target variable
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `linear_model.LinearRegression` - initialize linear regression model
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

group: pandas

## Example: 
```python
import pandas as pd
from sklearn import linear_model, model_selection

data = pd.read_csv('/var/www/examples/housing.csv')

X = data.loc[:, ['housing_median_age', 'total_rooms']]
y = data.median_house_value

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(len(y_pred))
```
```
5160

```

