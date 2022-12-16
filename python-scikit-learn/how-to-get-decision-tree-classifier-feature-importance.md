# How to get decision tree classifier feature importance

```python
from sklearn import datasets, tree, model_selection, metrics

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

fi = model.feature_importances_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.DecisionTreeClassifier(` - creates decision tree classifier model
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `.feature_importances_` - returns trained model feature importance list

group: decision_tree

## Example: 
```python
from sklearn import datasets, tree, model_selection, metrics

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = tree.DecisionTreeClassifier()
model.fit(X_train, y_train)

fi = model.feature_importances_
print(fi)
```
```
[0.         0.         0.42490918 0.57509082]

```

