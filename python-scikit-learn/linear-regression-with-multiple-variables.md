# Linear regression with multiple variables

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
- `.fit(` - train model with a given features and target variable dataset
- `.predict(` - predict target variable based on given features dataset
- `metrics.r2_score(` - calculate [R2 score](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score) to evaluate model quality (`1` is best, `0` is worst)

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

