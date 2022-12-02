# How to generate dataset for regression

```python
import numpy as np
from sklearn import datasets

X, y = datasets.make_regression(100, 5)

```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `X, y` - loaded features data (`X`) and target variable (`y`) values
- `datasets` - predefined datasets to play with
- `make_regression` - generates dataset for regression models
- `100` - number of generated objects
- `5` - number of features

group: generate

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.make_regression(100, 5)

print(X.shape)
print(y.shape)
```
```
(100, 5)
(100,)

```

