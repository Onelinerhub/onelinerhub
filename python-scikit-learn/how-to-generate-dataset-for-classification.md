# How to generate dataset for classification

```python
import numpy as np
from sklearn import datasets

X, y = datasets.make_classification(100, 5, n_classes=2)

```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `X, y` - loaded features data (`X`) and target variable (`y`) values
- `datasets` - predefined datasets to play with
- `make_classification` - generates dataset for classification models
- `100` - number of generated objects
- `5` - number of features
- `n_classes` - number of generated classes

group: generate

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.make_classification(100, 5, n_classes=2)

print(X.shape)
print(y)
```
```
(100, 5)
[1 1 1 1 0 0 1 1 0 0 0 0 1 0 1 1 1 1 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0
 0 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1 1 0 1 0 1 0 1 1 1 0 1 1 0 1 1 0 1 1 1
 0 1 0 0 0 1 0 1 0 0 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 1]

```

