# Logistic regression feature importance

### Feature importance for logistic regression can be roughly estimated by using trained model coefficients (make sure all features have the same scale or are normalized):

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

for f, im in enumerate(model.coef_[0]):
  print('Feature', (f+1), 'importance is', im)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.LogisticRegression()` - creates logistics regression model
- `.fit(` - train model with a given features and target variable dataset
- `.coef_` - returns list of coefficients of a trained model

group: logistic

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

for f, im in enumerate(model.coef_[0]):
  print('Feature', (f+1), 'importance is', im)
```
```
Feature 1 importance is -0.4410527873205119
Feature 2 importance is 0.9142380692659069
Feature 3 importance is -2.3368916600655116
Feature 4 importance is -0.996933531643161

```

