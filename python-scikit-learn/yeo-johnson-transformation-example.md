# Yeo Johnson transformation example

```python
from sklearn import preprocessing

pt = preprocessing.PowerTransformer(method='yeo-johnson')
data = [[1, 2], [3, 2], [4, 5]]
pt.fit(data)

transformed = pt.transform(data)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.PowerTransformer(` - create power transformation model
- `method='yeo-johnson'` - use Yeo Johnson transformation method
- `.fit(` - train transformation model
- `.transform(` - transform original data and return transformed data

group: power-transform

## Example: 
```python
from sklearn import preprocessing
pt = preprocessing.PowerTransformer(method='yeo-johnson')
data = [[1, 2], [3, 2], [4, 5]]
pt.fit(data)
print(pt.lambdas_)
print(pt.transform(data))
```
```
[ 1.38668178 -3.10053309]
[[-1.31616039 -0.70710678]
 [ 0.20998268 -0.70710678]
 [ 1.1061777   1.41421356]]

```

