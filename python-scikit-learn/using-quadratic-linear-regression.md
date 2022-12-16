# Using quadratic linear regression

### Quadratic regression can be achieved by using `PolynomialFeatures` to prepare dataset for polynomial form:

```python
from sklearn import preprocessing, linear_model
import numpy as np

data = np.array([[1, 1], [2, 4], [3, 9], [4, 15], [5, 21], [6, 36]])
X = np.array(data[:,0]).reshape(-1,1)
y = data[:,1]

poly = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
Xp = poly.fit_transform(X)

model = linear_model.LinearRegression()
model.fit(Xp, y)

y_pred = model.predict(Xp)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `.PolynomialFeatures(` - create polynomial object to prepare our dataset for polynomial form
- `poly.fit_transform(` - transform original dataset to polynomial form
- `linear_model.LinearRegression` - initialize linear regression model
- `.fit(` - train transformation model
- `.predict(` - predict target variable based on given features dataset

group: linear

## Example: 
```python
from sklearn import preprocessing, linear_model
import numpy as np

data = np.array([[1, 1], [2, 4], [3, 9], [4, 15], [5, 21], [6, 36]])
X = np.array(data[:,0]).reshape(-1,1)
y = data[:,1]

poly = preprocessing.PolynomialFeatures(degree=2, include_bias=False)
Xp = poly.fit_transform(X)

model = linear_model.LinearRegression()
model.fit(Xp, y)

print(model.predict(Xp))
```
```
[ 1.57142857  3.62857143  7.97142857 14.6        23.51428571 34.71428571]

```

