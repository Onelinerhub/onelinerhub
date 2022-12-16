# How to use label encoder

```python
import pandas as pd
from sklearn import preprocessing

ages = [50, 51, 52, 45, 40, 56]
countries = ['USA', 'Ukraine', 'Ukraine', 'UK', 'UK']

df = pd.DataFrame(list(zip(ages, countries)), columns=['Age', 'Country'])

labelencoder = preprocessing.LabelEncoder()
df['Country'] = labelencoder.fit_transform(df['Country'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `pd.DataFrame(` - sample dataframe to apply one hot encoding to
- `.LabelEncoder()` - create label encoder object
- `labelencoder.fit_transform(` - encodes given column (list of values)
- `df['Country']` - we want to encode `Country` column

group: encoder

## Example: 
```python
import pandas as pd
from sklearn import preprocessing

ages = [50, 51, 52, 45, 40, 56]
countries = ['USA', 'Ukraine', 'Ukraine', 'UK', 'UK']

df = pd.DataFrame(list(zip(ages, countries)), columns=['Age', 'Country'])
print(df)

labelencoder = preprocessing.LabelEncoder()
df['Country'] = labelencoder.fit_transform(df['Country'])
print(df)
```
```
   Age  Country
0   50      USA
1   51  Ukraine
2   52  Ukraine
3   45       UK
4   40       UK
   Age  Country
0   50        1
1   51        2
2   52        2
3   45        0
4   40        0

```

