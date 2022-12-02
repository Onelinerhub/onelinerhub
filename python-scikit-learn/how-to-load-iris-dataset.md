# How to load Iris dataset

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `X, y` - loaded features data (`X`) and target variable (`y`) values
- `datasets` - predefined datasets to play with
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset

group: datasets

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True)

print(X.shape)
print(y.shape)
```
```
(150, 4)
(150,)

```

