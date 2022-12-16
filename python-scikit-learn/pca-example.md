# PCA dimensionality reduction example

```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)
pca = decomposition.PCA(n_components=3)

pca.fit(X)
X = pca.transform(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `decomposition.PCA(` - create PCA dimensionality reduction model
- `n_components` - reduce to the given number of components (3 in our case)
- `.fit(` - train reduction model model
- `.transform(` - transform original data and return reduced dimensions data

group: pca

## Example: 
```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)
print('Original:', X.shape)

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

print('Reduced: ', X.shape)
```
```
Original: (150, 4)
Reduced:  (150, 3)

```

