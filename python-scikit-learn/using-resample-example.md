# Using resample example

```python
from sklearn import utils

X = [1,2,2,3,2,1,1,3]
Xr = utils.resample(X, n_samples=6, random_state=1)


```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `utils.resample(` - resample given dataset in a consistent way
- `n_samples` - number of samples to get for result
- `random_state` - random seed to get repeatable results

group: resample

## Example: 
```python
from sklearn import utils

X = [1,2,2,3,2,1,1,3]
Xr = utils.resample(X, n_samples=6, random_state=1)

print(Xr)
```
```
[1, 3, 2, 1, 3, 2]

```

