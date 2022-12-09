# K means clustering example

```python
from sklearn import datasets, cluster

X, _ = datasets.load_iris(return_X_y=True)
model = cluster.KMeans(n_clusters = 3)
model.fit(X)

clusters = model.predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.KMeans(` - create KMeans clustering model
- `n_clusters` - number of clusters we want to see
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

group: cluster


