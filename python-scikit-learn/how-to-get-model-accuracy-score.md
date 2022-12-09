# How to get model accuracy score

```python
from sklearn import datasets, neighbors, model_selection, metrics

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = metrics.accuracy_score(y_pred, y_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.KNeighborsClassifier(` - K neighbors classification model
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `.accuracy_score(` - accuracy classification score

group: scores

## Example: 
```python
from sklearn import datasets, neighbors, model_selection, metrics

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = metrics.accuracy_score(y_pred, y_test)
print(accuracy)
```
```
0.9473684210526315

```

