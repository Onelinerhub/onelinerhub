# How to load ML model from file

```python
import pickle
from sklearn import datasets, linear_model

X, y = datasets.load_diabetes(return_X_y=True)
model = pickle.load(open('/tmp/model.ml', 'rb'))

y_pred = model.predict(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `pickle.load(` - loads data from given file
- `open(` - opens file descriptor (for reading in our case)
- `/tmp/model.ml` - path to file to load model from
- `.predict(` - predict target variable based on given features dataset

group: load-save

## Example: 
```python
import pickle
from sklearn import datasets, linear_model

X, y = datasets.load_diabetes(return_X_y=True)
model = pickle.load(open('/tmp/model.ml', 'rb'))

y_pred = model.predict(X)

print(model.score(X, y))
```
```
0.506799948108825

```

