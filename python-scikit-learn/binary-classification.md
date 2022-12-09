# Binary classification

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `load_breast_cancer` - loads [breast cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) dataset
- `.LogisticRegression(` - creates logistics regression model
- `max_iter` - specify maximum number of iterations for model training
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.958041958041958

```

