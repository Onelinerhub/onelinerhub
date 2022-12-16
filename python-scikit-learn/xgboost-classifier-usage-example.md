# Xgboost classifier usage example

```python
from sklearn import datasets, model_selection
import xgboost as xgb

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = xgb.XGBClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import xgboost as xgb` - Loads [lib:XGBoost](https://xgboost.readthedocs.io/en/stable/) module
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `xgb.XGBClassifier(` - creates XGBoost classification model
- `.fit(` - train transformation model
- `.predict(` - predict target variable based on given features dataset

group: xgboost

## Example: 
```python
from sklearn import datasets, model_selection
import xgboost as xgb

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = xgb.XGBClassifier()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.9736842105263158

```

