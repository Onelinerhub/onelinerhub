# Adaboost regression example

```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.AdaBoostRegressor()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `.AdaBoostRegressor(` - creates adaptive boosting regression model
- `.fit(` - train model with a given features and target variable dataset
- `.score(` - returns model accuracy score

group: adaboost

## Example: 
```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.AdaBoostRegressor()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.3076113179240463

```

