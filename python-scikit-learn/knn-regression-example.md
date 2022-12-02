# KNN regression example

```python
from sklearn import datasets, neighbors, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsRegressor(10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.KNeighborsRegressor(` - KNN regression model based on nearest neighbors approach
- `(10)` - number of neighbors to interpolate based on
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

group: knn

## Example: 
```python
from sklearn import datasets, neighbors, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsRegressor(10)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = metrics.r2_score(y_test, y_pred)
print(r2)
```
```
0.550945869459051

```

