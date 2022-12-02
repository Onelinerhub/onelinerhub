# How to split dataset to test and train samples

```python
from sklearn import datasets, model_selection

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.66)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `train_size` - portion of objects to use for train sample (66% in our case)

## Example: 
```python
from sklearn import datasets, model_selection

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.66)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
```
```
(291, 10)
(291,)
(151, 10)
(151,)

```

