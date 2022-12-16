# Decision tree classifier example

```python
from sklearn import datasets, tree, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
```


group: decision_tree

## Example: 
```python
from sklearn import datasets, tree, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
```
0.9736842105263158

```

