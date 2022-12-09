# Using Lasso model example

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.Lasso()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.Lasso(` - create Lasso model object
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

group: lasso

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.Lasso()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.36219590928106504

```

