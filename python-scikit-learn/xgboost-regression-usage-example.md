# Xgboost regression usage example

```python
from sklearn import datasets, model_selection
import xgboost as xgb

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = xgb.XGBRegressor()
model.fit(X_train, y_train)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import xgboost as xgb` - Loads [lib:XGBoost](https://xgboost.readthedocs.io/en/stable/) module
- `load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `xgb.XGBRegressor(` - creates XGBoost regression model
- `.fit(` - train transformation model
- `.predict(` - predict target variable based on given features dataset

group: xgboost

## Example: 
```python
from sklearn import datasets, model_selection
import xgboost as xgb

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = xgb.XGBRegressor()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.35751336429972946

```

