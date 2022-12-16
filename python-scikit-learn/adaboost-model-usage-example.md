# Adaboost classifier model usage example

```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.AdaBoostClassifier()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `.AdaBoostClassifier()` - create AdaBoost model
- `.fit(` - train model with a given features and target variable dataset
- `score` - trained model accuracy score for a given (test) dataset

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

