# Nearest neighbors classifier example

```python
from sklearn import datasets, neighbors, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```


group: nn

## Example: 
```python
from sklearn import datasets, neighbors, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)
```
```
[1 0 0 1 0 1 0 1 1 2 0 1 0 2 2 2 1 2 2 0 1 2 0 0 0 2 1 1 2 0 1 1 1 1 2 2 2
 1]

```

