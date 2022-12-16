# How to resample with replacement

```python
from sklearn import utils

X = [1,2,2,4,3,6,7,3,9]
Xr = utils.resample(X, n_samples=5, random_state=, replace=True)


```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `utils.resample(` - resample given dataset in a consistent way
- `n_samples` - number of samples to get for result
- `random_state` - random seed to get repeatable results
- `replace=True` - use resampling with replacement, this is `True` by default

group: resample

## Example: 
```python
from sklearn import utils

X = [1,2,2,4,3,6,7,3,9]
Xr = utils.resample(X, n_samples=5, random_state=1, replace=True)

print(Xr)
```
```
[6, 9, 6, 1, 1]

```

