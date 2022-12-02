# How to load Boston housing dataset

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_breast_cancer(return_X_y=True)
```

- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `X, y` - loaded features data (`X`) and target variable (`y`) values
- `datasets` - predefined datasets to play with
- `load_breast_cancer` - loads [breast cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) dataset

group: datasets

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_breast_cancer(return_X_y=True)

print(X.shape)
print(y.shape)
```
```
(569, 30)
(569,)

```

