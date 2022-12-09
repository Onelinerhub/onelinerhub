# How to evaluate cross validation based on cross_val_score()

```python
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]
lasso = linear_model.Lasso()

cvs = cross_val_score(lasso, X, y)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets.load_diabetes` - loads sample [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) database
- `linear_model.Lasso` - creates [Lasso model](https://en.wikipedia.org/wiki/Lasso_(statistics))
- `cross_val_score(` - evaluates a score by cross-validation
- `lasso` - model to use for cross-validation

## Example: 
```python
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]
lasso = linear_model.Lasso()

cvs = cross_val_score(lasso, X, y)
print(cvs)
```
```
[0.29828675 0.2241492  0.15480127 0.25519733 0.17108715]

```

