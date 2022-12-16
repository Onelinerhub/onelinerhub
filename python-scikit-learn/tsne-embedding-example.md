# TSNe embedding example

```python
import numpy as np
from sklearn import manifold

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
Xe = manifold.TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(X)
```

- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.TSNE(` - creates T-distributed Stochastic Neighbor Embedding model
- `n_components=2` - reduce dataset to 2 features
- `.fit_transform(` - train and transform given dataset
- `Xe` - will contain embedded dataset

## Example: 
```python
import numpy as np
from sklearn.manifold import TSNE

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
print(X.shape)

Xe = TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(X)
print(Xe.shape)
```
```
(4, 3)
(4, 2)

```

