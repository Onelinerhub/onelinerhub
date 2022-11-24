# Linear regression with multiple variables

### In order to use multiple feature variables with linear regression we can just use 2-dimensional arrays as in below `X` variable example:

```python
from sklearn import linear_model

X = [[1,2], [2,1], [2,3], [3,2], [4,5]]
y = [3, 3, 5, 6, 9]

model = linear_model.LinearRegression()
model.fit(X, y)

r2 = model.score(X,y)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `linear_model.LinearRegression` - initialize linear regression model
- `X = ` - declare feature dataset with 2 variables and 5 objects
- `.fit(` - train model with a given features and target variable dataset
- `score` - trained model `R2` score for a given (test) dataset

group: linear

## Example: 
```python
from sklearn import linear_model

X = [[1,2], [2,1], [2,3], [3,2], [4,5]]
y = [3, 3, 5, 6, 9]

model = linear_model.LinearRegression()
model.fit(X, y)

r2 = model.score(X,y)

print(r2)
```
```
0.981789802289282

```

