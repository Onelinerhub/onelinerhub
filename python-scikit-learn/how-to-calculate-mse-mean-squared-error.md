# How to calculate MSE (mean squared error)

```python
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = metrics.mean_squared_error(y_test, y_pred)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `.mean_squared_error(` - calculates MSE for given test and predicted values

group: errors

## Example: 
```python
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = metrics.mean_squared_error(y_test, y_pred)
print(mse)
```
```
2941.8583095885656

```

