# Using quantile transformer example

```python
from sklearn import preprocessing

qt = preprocessing.QuantileTransformer(n_quantiles=3)
data = [[1, 2], [3, 2], [4, 5]]
qt.fit(data)

transformed = qt.transform(data)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.QuantileTransformer(` - creates [quantile transformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html) model
- `n_quantiles` - number of quantiles to be computed
- `.fit(` - train transformation model
- `.transform(` - transform original data and return transformed data

## Example: 
```python
from sklearn import preprocessing

qt = preprocessing.QuantileTransformer(n_quantiles=3)
data = [[1, 2], [3, 2], [4, 5]]
qt.fit(data)

transformed = qt.transform(data)
print(transformed)
```
```
[[0.  0. ]
 [0.5 0. ]
 [1.  1. ]]

```

