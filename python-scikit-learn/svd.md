# Using SVD to reduce dimensions example

```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)

svd = decomposition.TruncatedSVD(n_components=2)
svd.fit(X)
X = svd.transform(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `.TruncatedSVD(` - creates dimensionality reduction model based on truncated SVD
- `.fit(` - train reduction model
- `.transform(` - transform original data and return reduced dimensions data

group: pca

## Example: 
```python
from sklearn import decomposition, datasets

X, y = datasets.load_iris(return_X_y=True)
print('Original:', X.shape)

svd = decomposition.TruncatedSVD(n_components=2)
svd.fit(X)
X = svd.transform(X)

print('Reduced: ', X.shape)
```
```
Original: (150, 4)
Reduced:  (150, 2)

```

