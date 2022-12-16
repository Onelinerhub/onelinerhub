# Using OneClassSVM for outliers detection example

```python
from sklearn import svm

X = [[0.32], [0.31], [0], [0.32], [0.31], [1], [0.32], [0.31]]

m = svm.OneClassSVM(gamma='auto').fit(X)
detected = m.predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `X = ` - example values set to detect outliers for
- `.OneClassSVM(` - creates unsupervised outlier detection model
- `.fit(` - train transformation model
- `.predict(` - predict target variable based on given features dataset
- `detected` - will contain a list of attributed outliers (`-1`) and values that are ok (`1`)

## Example: 
```python
from sklearn import svm

X = [[0.32], [0.31], [0], [0.32], [0.31], [1], [0.32], [0.31]]

m = svm.OneClassSVM(gamma='auto').fit(X)
detected = m.predict(X)

print(detected)
```
```
[ 1  1 -1  1  1 -1  1  1]

```

