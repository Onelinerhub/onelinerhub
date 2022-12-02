# How to get logistic regression coefficients

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

coefs = model.coef_
intercept = model.intercept_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.LogisticRegression()` - creates logistics regression model
- `.fit(` - train model with a given features and target variable dataset
- `.coef_` - returns list of coefficients of a trained model
- `.intercept_` - returns intercept of a trained model

group: logistic

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

print(model.coef_)
print(model.intercept_)
```
```
[[-0.4618142   0.77963275 -2.30767749 -1.00587061]
 [ 0.53252788 -0.46624121 -0.09216546 -0.90155818]
 [-0.07071368 -0.31339155  2.39984295  1.90742879]]
[  9.64409977   2.01960555 -11.66370532]

```

