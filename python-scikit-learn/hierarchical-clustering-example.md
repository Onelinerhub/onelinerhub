# Hierarchical clustering example

```python
from sklearn import datasets, cluster

X, _ = datasets.load_iris(return_X_y=True)
model = cluster.AgglomerativeClustering(n_clusters = 3)

clusters = model.fit_predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `.AgglomerativeClustering(` - create agglomerative clustering model (hierarchical clustering model)
- `n_clusters` - number of clusters we want to see
- `.fit_predict(` - trains model and returns predicted cluster labels

group: cluster

## Example: 
```python
from sklearn import datasets, cluster

X, _ = datasets.load_iris(return_X_y=True)
model = cluster.AgglomerativeClustering(n_clusters = 3)
clusters = model.fit_predict(X)
print(clusters)
```
```
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 2 2 2 0 2 2 2 2
 2 2 0 0 2 2 2 2 0 2 0 2 0 2 2 0 0 2 2 2 2 2 0 0 2 2 2 0 2 2 2 0 2 2 2 0 2
 2 0]

```

