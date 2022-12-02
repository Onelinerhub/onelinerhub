# Logistic regression

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.LogisticRegression()` - creates logistics regression model
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `y_pred` - target variable predicted values by our model (values to evaluate)

group: logistic

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)
```
```
[1 2 1 0 2 1 2 2 0 2 1 0 0 2 0 1 0 1 1 2 0 0 0 1 1 0 0 1 1 1 1 2 0 2 0 1 2
 0]

```

