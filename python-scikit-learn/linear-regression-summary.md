# Linear regression summary

```python
import numpy as np
from sklearn import datasets, linear_model

X, y = datasets.load_diabetes(return_X_y=True)

model = linear_model.LinearRegression()
model.fit(X, y)

intercept = model.intercept_
coefs = model.coef_
score = model.score(X, y)

```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `linear_model.LinearRegression` - initialize linear regression model
- `.fit(` - train model with a given features and target variable dataset
- `intercept` - value of linear model intercept after training
- `coefs` - list of trained coefficients
- `score` - trained model `R2` score

group: linear

## Example: 
```python
import numpy as np
from sklearn import datasets, linear_model

X, y = datasets.load_diabetes(return_X_y=True)

model = linear_model.LinearRegression()
model.fit(X, y)

intercept = model.intercept_
coefs = model.coef_
score = model.score(X, y)

print('Intercept:', intercept)
print('Coefs:', coefs)
print('R2:', score)
```
```
Intercept: 152.13348416289597
Coefs: [ -10.0098663  -239.81564367  519.84592005  324.3846455  -792.17563855
  476.73902101  101.04326794  177.06323767  751.27369956   67.62669218]
R2: 0.5177484222203498

```

