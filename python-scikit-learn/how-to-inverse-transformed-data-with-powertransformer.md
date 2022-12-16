# How to inverse transformed data with PowerTransformer

```python
from sklearn import preprocessing

pt = preprocessing.PowerTransformer()
data = [[1, 2], [3, 2], [4, 5]]
pt.fit(data)

transformed = pt.transform(data)
original = pt.inverse_transform(transformed)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.PowerTransformer(` - create power transformation model
- `.fit(` - train transformation model
- `.transform(` - transform original data and return transformed data
- `transformed` - transformed data
- `.inverse_transform(` - inverse transformed data to original state
- `original` - will contain inversed transformed data (basically = original `data`)

group: power-transform

## Example: 
```python
from sklearn import preprocessing
pt = preprocessing.PowerTransformer()
data = [[1, 2], [3, 2], [4, 5]]
pt.fit(data)

trasnformed = pt.transform(data)
print(pt.inverse_transform(trasnformed))
```
```
[[1. 2.]
 [3. 2.]
 [4. 5.]]

```

