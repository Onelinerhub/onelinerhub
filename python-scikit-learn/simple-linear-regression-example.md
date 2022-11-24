# Simple linear regression example

```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = metrics.r2_score(y_test, y_pred)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `linear_model.LinearRegression` - initialize linear regression model
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `metrics.r2_score(` - calculate [R2 score](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score) to evaluate model quality (`1` is best, `0` is worst)

group: linear

## Example: 
```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = metrics.r2_score(y_test, y_pred)
print(r2)
```
```
0.4575313287098933

```

