# Convert bunch object to dataframe

```python
from sklearn import datasets
import pandas as pd

data = datasets.load_iris()

df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `load_iris()` - loads [Iris](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) dataset
- `.DataFrame(` - create new dataframe from given data
- `columns` - list of columns to use for dataframe
- `data['feature_names']` - list of loaded data features (we're using them as columns in dataframe)
- `data['target']` - target variable values

## Example: 
```python
from sklearn import datasets
import pandas as pd

data = datasets.load_iris()

df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']

print(df.head())
```
```
   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target
0                5.1               3.5  ...               0.2       0
1                4.9               3.0  ...               0.2       0
2                4.7               3.2  ...               0.2       0
3                4.6               3.1  ...               0.2       0
4                5.0               3.6  ...               0.2       0

[5 rows x 5 columns]

```

