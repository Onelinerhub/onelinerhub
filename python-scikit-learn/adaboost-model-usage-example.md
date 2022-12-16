# Adaboost model usage example

```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.AdaBoostClassifier()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```


group: adaboost

## Example: 
```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.AdaBoostClassifier()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.9736842105263158

```

