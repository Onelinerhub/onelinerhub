# Grid search CV example

```python
from sklearn import svm, datasets, model_selection

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

clf = model_selection.GridSearchCV(svm.SVC(), parameters)
clf.fit(iris.data, iris.target)

results = clf.cv_results_.keys()
```


group: grid-search

## Example: 
```python
from sklearn import svm, datasets, model_selection

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

clf = model_selection.GridSearchCV(svm.SVC(), parameters)
clf.fit(iris.data, iris.target)

print(clf.cv_results_)
```
```
{'mean_fit_time': array([0.00048242, 0.00052795, 0.00040908, 0.0004529 ]), 'std_fit_time': array([9.56704095e-05, 2.61316334e-05, 2.06203266e-05, 1.91588874e-05]), 'mean_score_time': array([0.00024114, 0.00028515, 0.00022287, 0.0002389 ]), 'std_score_time': array([2.78815620e-05, 1.28604670e-05, 9.46182387e-06, 5.83419568e-06]), 'param_C': masked_array(data=[1, 1, 10, 10],
             mask=[False, False, False, False],
       fill_value='?',
            dtype=object), 'param_kernel': masked_array(data=['linear', 'rbf', 'linear', 'rbf'],
             mask=[False, False, False, False],
       fill_value='?',
            dtype=object), 'params': [{'C': 1, 'kernel': 'linear'}, {'C': 1, 'kernel': 'rbf'}, {'C': 10, 'kernel': 'linear'}, {'C': 10, 'kernel': 'rbf'}], 'split0_test_score': array([0.96666667, 0.96666667, 1.        , 0.96666667]), 'split1_test_score': array([1.        , 0.96666667, 1.        , 1.        ]), 'split2_test_score': array([0.96666667, 0.96666667, 0.9       , 0.96666667]), 'split3_test_score': array([0.96666667, 0.93333333, 0.96666667, 0.96666667]), 'split4_test_score': array([1., 1., 1., 1.]), 'mean_test_score': array([0.98      , 0.96666667, 0.97333333, 0.98      ]), 'std_test_score': array([0.01632993, 0.02108185, 0.03887301, 0.01632993]), 'rank_test_score': array([1, 4, 3, 1], dtype=int32)}

```

