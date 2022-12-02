# Scaling data using StandardScaler

```python
from sklearn import datasets, preprocessing

data = datasets.load_diabetes(scaled=False).data

scl = preprocessing.StandardScaler()
scl.fit(data)
data_scaled = scl.transform(data)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `.StandardScaler(` - Scales each feature than values are distributed in `-1...1` range
- `scl.fit(` - fit scaler
- `scl.transform(` - scale data using trained scaler

group: scaler

## Example: 
```python
from sklearn import datasets, preprocessing

data = datasets.load_diabetes(scaled=False).data
print(data[0])

scl = preprocessing.StandardScaler()
scl.fit(data)
data_scaled = scl.transform(data)

print(data_scaled[0])
```
```
[ 59.       2.      32.1    101.     157.      93.2     38.       4.
   4.8598  87.    ]
[ 0.80050009  1.06548848  1.29708846  0.45984057 -0.92974581 -0.73206462
 -0.91245053 -0.05449919  0.41853093 -0.37098854]

```

