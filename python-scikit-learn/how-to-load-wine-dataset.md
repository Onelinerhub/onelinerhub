# How to load wine dataset

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_wine(return_X_y=True)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `X, y` - loaded features data (`X`) and target variable (`y`) values
- `datasets` - predefined datasets to play with
- `load_wine` - loads [wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html) dataset

group: datasets

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_wine(return_X_y=True)

print(X.shape)
print(y.shape)
```
```
(178, 13)
(178,)

```

