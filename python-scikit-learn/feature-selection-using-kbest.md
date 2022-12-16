# Feature selection using KBest

```python
from sklearn import datasets, feature_selection

X, y = datasets.load_digits(return_X_y=True)

Xs = feature_selection.SelectKBest(feature_selection.chi2, k=20).fit_transform(X, y)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.load_digits(` - returns [digits dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) for classification
- `.SelectKBest(` - select features according to the k highest scores
- `feature_selection.chi2` - use [chi2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html) as feature scoring function
- `.fit_transform(` - train and reduce given dataset to the selected number of features
- `k=20` - we want to have `20` best features for our dataset

group: feature-selection

## Example: 
```python
from sklearn import datasets, feature_selection

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

Xs = feature_selection.SelectKBest(feature_selection.chi2, k=20).fit_transform(X, y)
print(Xs.shape)
```
```
(1797, 64)
(1797, 20)

```

