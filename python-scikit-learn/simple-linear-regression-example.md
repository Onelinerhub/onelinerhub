# Simple linear regression example

```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = metrics.r2_score(y_test, y_pred)
```


group: linear

## Example: 
```python
import numpy as np
from sklearn import datasets, linear_model, model_selection, metrics

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = metrics.r2_score(y_test, y_pred)
```

