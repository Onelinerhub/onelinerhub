# How to inverse transform PCA reduced data

```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)
pca = decomposition.PCA(n_components=3)

pca.fit(X)
reduced = pca.transform(X)
inversed = pca.inverse_transform(reduced)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `decomposition.PCA(` - create PCA dimensionality reduction model
- `n_components` - reduce to the given number of components (3 in our case)
- `.fit(` - train reduction model model
- `.transform(` - transform original data and return reduced dimensions data
- `.inverse_transform(` - inverse transform back to original number of dimensions

group: pca

## Example: 
```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)
pca = decomposition.PCA(n_components=3)

pca.fit(X)
reduced = pca.transform(X)
inversed = pca.inverse_transform(reduced)

print('Reduced:  ', reduced.shape)
print('Invresed: ', inversed.shape)

print(inversed[0:5])
```
```
Reduced:   (150, 3)
Invresed:  (150, 4)
[[5.09928623 3.50072335 1.40108561 0.1982949 ]
 [4.86875839 3.03166108 1.4475168  0.12536791]
 [4.69370023 3.20638436 1.30958161 0.18495067]
 [4.6238432  3.07583667 1.46373578 0.25695828]
 [5.0193263  3.58041421 1.37060574 0.24616799]]

```

