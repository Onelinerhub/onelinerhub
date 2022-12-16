# Feature selection using RFE

```python
from sklearn import datasets, svm, feature_selection

X, y = datasets.make_friedman1(n_samples=50, n_features=10)

selector = feature_selection.RFECV(svm.SVR(kernel="linear"), step=1, cv=5)
selector = selector.fit(X, y)

ranks = selector.ranking_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.make_friedman1(` - creates Friedman #1 regression dataset
- `.RFECV(` - creates RFE feature selection model
- `svm.SVR(` - we use SVR model as estimator for RFE
- `.fit(` - train model
- `selector.ranking_` - returns features rankings

group: feature-selection

## Example: 
```python
from sklearn import datasets, svm, feature_selection

X, y = datasets.make_friedman1(n_samples=50, n_features=10)

selector = feature_selection.RFECV(svm.SVR(kernel="linear"), step=1, cv=5)
selector = selector.fit(X, y)
print(selector.ranking_)
```
```
[1 1 3 1 1 1 1 2 1 1]

```

