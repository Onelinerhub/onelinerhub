# How to define threshold for logistic regression

### In order to define threshold for logistic regression we have to use `predict_proba()` method which predicts probabilities for each class/object and pick only classes with higher value than set by us:

```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)
y_pred_prob = model.predict_proba(X_test)

threshold = 0.9
y_pred = []
for probs in y_pred_prob:
  cls = None
  for c, p in enumerate(probs):
    if p >= threshold:
      cls = c
      break
  y_pred.append(cls)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.LogisticRegression()` - creates logistics regression model
- `.fit(` - train model with a given features and target variable dataset
- `.predict_proba(` - predict classes probabilities for a given sample
- `y_pred_prob` - list of predicted classes probabilities for each object
- `threshold` - minimum probability (confidence) level for predicting a class
- `if p > threshold:` - pick only those classes which have higher probability than `threshold` value
- `y_pred` - will contain predicted classes with a given threshold value (and `None` if no confident class was found for an object)

group: logistic

## Example: 
```python
from sklearn import datasets, linear_model, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = linear_model.LogisticRegression()
model.fit(X_train, y_train)
y_pred_prob = model.predict_proba(X_test)

threshold = 0.9
y_pred = []
for probs in y_pred_prob:
  cls = None
  for c, p in enumerate(probs):
    if p >= threshold:
      cls = c
      break
  y_pred.append(cls)
  
print(y_pred)
```
```
[2, 2, None, None, None, None, 0, 0, None, 1, 2, 2, 2, None, 2, None, 0, 0, 1, 2, 0, None, 1, 1, 0, 2, 0, 1, None, None, 2, 0, None, 0, 0, 0, 1, 0]

```

