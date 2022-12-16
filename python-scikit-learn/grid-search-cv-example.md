# Grid search CV example

```python
from sklearn import svm, datasets, model_selection

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

clf = model_selection.GridSearchCV(svm.SVC(), parameters)
clf.fit(iris.data, iris.target)

results = clf.cv_results_
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `load_iris` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `parameters` - parameters dictionary to run grid search accross
- `.GridSearchCV(` - creates GridSearchCV model
- `svm.SVC()` - use [SVC](https://onelinerhub.com/python-scikit-learn/svc-classifier-example) model as an estimator
- `.fit(` - train transformation model
- `.cv_results_` - dictionary with results after model training and parameters search

group: grid-search

## Example: 
```python
from sklearn import svm, datasets, model_selection

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

clf = model_selection.GridSearchCV(svm.SVC(), parameters)
clf.fit(iris.data, iris.target)

print(clf.cv_results_['params'])
```
```
[{'C': 1, 'kernel': 'linear'}, {'C': 1, 'kernel': 'rbf'}, {'C': 10, 'kernel': 'linear'}, {'C': 10, 'kernel': 'rbf'}]

```

