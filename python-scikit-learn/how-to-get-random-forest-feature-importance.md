# How to get random forest feature importance

```python
import numpy as np
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.RandomForestClassifier()
model.fit(X_train, y_train)

feature_importance = model.feature_importances_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `model_selection.train_test_split` - splits given `X` and `y` datasets to test (25% of values by default) and train (75% of values by default) subsets
- `.RandomForestClassifier(` - creates random forest classification model
- `.fit(` - train model with a given features and target variable dataset
- `.feature_importances_` - returns trained model feature importance list

group: random-forest

## Example: 
```python
import numpy as np
from sklearn import datasets, ensemble, model_selection

X, y = datasets.load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

model = ensemble.RandomForestClassifier()
model.fit(X_train, y_train)

feature_importance = model.feature_importances_
print(feature_importance)
```
```
[0.09302528 0.03341848 0.38972412 0.48383212]

```

