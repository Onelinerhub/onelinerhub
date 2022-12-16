# How to get Elasticnet feature importance

### For ElasticNext model we can use trained coefficients to evaluate feature importance:

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.ElasticNet()
model.fit(X_train, y_train)

fi = model.coef_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.ElasticNet(` - creates [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html) training model
- `.fit(` - train model with a given features and target variable dataset
- `.coef_` - returns list of coefficients of a trained model

group: elasticnet

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.ElasticNet()
model.fit(X_train, y_train)

fi = model.coef_
print(fi)
```
```
[ 0.15675432  0.          3.33520417  2.10046188  0.44089256  0.27115722
 -2.23505284  2.37683059  3.24743807  1.85651586]

```

