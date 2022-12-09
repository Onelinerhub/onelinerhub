# Clustering example

```python
from sklearn import datasets, cluster

X, y = datasets.load_iris(return_X_y=True)
model = cluster.KMeans(n_clusters = 3)
model.fit(X)

clusters = model.predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `.KMeans(` - create KMeans clustering model
- `n_clusters` - number of clusters we want to see
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset

group: cluster

## Example: 
```python
from sklearn import datasets, cluster

X, y = datasets.load_iris(return_X_y=True)
model = cluster.KMeans(n_clusters = 3)
model.fit(X)

clusters = model.predict(X)
print(clusters)
```
```
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 0 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 0 2 0 0 0 0 2 0 0 0 0
 0 0 2 2 0 0 0 0 2 0 2 0 2 0 0 2 2 0 0 0 0 0 2 0 0 0 0 2 0 0 0 2 0 0 0 2 0
 0 2]

```

