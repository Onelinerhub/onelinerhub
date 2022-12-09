# How to save ML model to file

```python
import pickle
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open('/tmp/model.ml', 'wb'))
```

- `pickle.dump(` - saves given model to the given file
- `/tmp/model.ml` - path to the file to save model to
- `open(` - opens file descriptor (to write data to it)

group: load-save


