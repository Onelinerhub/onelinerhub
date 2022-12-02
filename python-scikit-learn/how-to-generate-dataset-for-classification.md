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

X, y = datasets.make_classification(10, 5, n_classes=2)

print(X)
print(y)
```
```
[[-0.50279334  0.32296525  1.57712474 -1.23595662 -0.70293344]
 [-0.34804243 -0.73128341 -0.61576334 -1.81608243 -0.01065777]
 [-2.57201745 -2.83667717  0.04075228  0.70260165 -1.35847009]
 [ 0.6597867   1.28899617  0.99330712  0.52079524  0.0687031 ]
 [-1.24301759 -0.69406941  1.23006131  0.1545228  -0.99389378]
 [ 3.27008105  2.35462642 -2.2905693  -0.41091725  2.35117719]
 [ 1.10362238  0.80466412 -0.75516519 -0.77580869  0.78851679]
 [-0.18167839 -0.85802807 -1.17315523  0.12867272  0.23183838]
 [-2.96998317 -3.31129006 -0.01677569  2.44074352 -1.5508725 ]
 [-0.39381185 -1.01980152 -1.040705   -0.31772904  0.0838142 ]]
[1 0 1 1 1 0 0 0 1 0]

```

