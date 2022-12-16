# How to use n_jobs for parallel training

### The `n_jobs` parameter can be used to speed-up model training thanks to multiple parallel search jobs being executed:

```python
from sklearn import datasets, neighbors, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3, n_jobs=5)
model.fit(X_train, y_train)

```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.KNeighborsClassifier(` - K neighbors classification model
- `n_jobs` - number of parallel jobs to run for neighbors search (5 in our case)

## Example: 
```python
from sklearn import datasets, neighbors, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = neighbors.KNeighborsClassifier(3, n_jobs=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(y_pred)
```
```
[1 2 1 0 2 1 1 2 2 1 1 2 2 2 2 0 2 0 0 0 0 2 2 2 0 0 1 1 0 0 1 2 0 2 1 2 1
 0]

```

