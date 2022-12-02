# Scaling data using MinMaxScaler

```python
from sklearn import datasets, preprocessing

data = datasets.load_diabetes(scaled=False).data

scl = preprocessing.MinMaxScaler()
scl.fit(data)
data_scaled = scl.transform(data)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `.MinMaxScaler(` - Scales each feature than values are distributed in `0...1` range
- `scl.fit(` - fit scaler
- `scl.transform(` - scale data using trained scaler
- `data_scaled` - will contain scaled dataset

group: scaler

## Example: 
```python
from sklearn import datasets, preprocessing

data = datasets.load_diabetes(scaled=False).data
print(data[0])

scl = preprocessing.MinMaxScaler()
scl.fit(data)
data_scaled = scl.transform(data)

print(data_scaled[0])
```
```
[ 59.       2.      32.1    101.     157.      93.2     38.       4.
   4.8598  87.    ]
[0.66666667 1.         0.58264463 0.54929577 0.29411765 0.25697211
 0.20779221 0.28208745 0.562217   0.43939394]

```

