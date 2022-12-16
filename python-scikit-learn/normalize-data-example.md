# Normalize data example

```python
from sklearn import preprocessing
data = [1,2,3,4,5,6,6,6,3,4,2,4]

norm = preprocessing.normalize([data])
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `data` - list of values to normalize
- `.normalize(` - scales given values to unit norm

group: normalize

## Example: 
```python
from sklearn import preprocessing
data = [1,2,3,4,5,6,6,6,3,4,2,4]

norm = preprocessing.normalize([data])

print(norm)
```
```
[[0.06933752 0.13867505 0.20801257 0.2773501  0.34668762 0.41602515
  0.41602515 0.41602515 0.20801257 0.2773501  0.13867505 0.2773501 ]]

```

