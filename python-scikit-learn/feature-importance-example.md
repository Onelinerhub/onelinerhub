# Feature importance example

### For most models, `feature_importances_` model attribute is available after training:

```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.RandomForestClassifier()
model.fit(X_train, y_train)

fi = model.feature_importances_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.RandomForestClassifier(` - creates random forest classification model
- `.fit(` - train model with a given features and target variable dataset
- `.feature_importances_` - returns trained model feature importance list

group: feature-importance

## Example: 
```python
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.RandomForestClassifier()
model.fit(X_train, y_train)

fi = model.feature_importances_
print(fi)
```
```
[0.11663411 0.03627566 0.39945207 0.44763817]

```

