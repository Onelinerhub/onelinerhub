# Sklearn usage example (scikit-learn import)

```python
from sklearn import datasets
iris = datasets.load_iris()
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `datasets` - predefined datasets to play with
- `load_iris()` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset

group: install

## Example: 
```python
from sklearn import datasets
iris = datasets.load_iris()
print(iris.data.shape)
```
```
(150, 4)

```

