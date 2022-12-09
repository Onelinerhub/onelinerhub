# Using Lasso model example

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.Lasso()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```


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

