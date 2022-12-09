# Get Lasso model coefficients

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.Lasso()
model.fit(X_train, y_train)

coeffs = model.coef_
sparse = model.sparse_coef_
intercept = model.intercept_  
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.Lasso(` - create Lasso model object
- `.fit(` - train model with a given features and target variable dataset
- `.coef_` - returns list of coefficients of a trained model
- `.intercept_` - value of linear model intercept after training
- `sparse_coef_` - sparse representation of the fitted coefficients

group: lasso

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.Lasso()
model.fit(X_train, y_train)

coeffs = model.coef_
sparse = model.sparse_coef_
intercept = model.intercept_  

print(coeffs, sparse, intercept)
```
```
[  0.          -0.         378.42448976  22.84904289   0.
   0.          -0.           0.         302.34461535   0.        ]   (0, 2)	378.4244897581937
  (0, 3)	22.8490428882718
  (0, 8)	302.3446153480934 151.67182691818425

```

