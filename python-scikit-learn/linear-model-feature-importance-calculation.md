# Linear model feature importance calculation

### For linear models, trained coefficients can be used as feature importance values:

```python
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

fi = model.coef_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.fit(` - train model with a given features and target variable dataset
- `.coef_` - returns list of coefficients of a trained model

group: feature-importance

## Example: 
```python
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

fi = model.coef_
print(fi)
```
```
[   7.4644251  -212.29645468  484.41681905  275.862333   -938.22675656
  587.40072837  114.72619725  120.06905393  872.88971664   45.45492861]

```

