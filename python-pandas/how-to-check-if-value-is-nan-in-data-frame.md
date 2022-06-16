# How to check if value is NaN in data frame

```python
import pandas as pd

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, None, 78, None],
  'Phone Price': [204, None, 501, 800, None]
}

data = pd.DataFrame(phoneDataSet)
data_nan = data[data['Phone Price'].isna()]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.isna()` - finds all `NaN` values
- `'Phone Price'` - column to find `NaN` values in
- `data_nan` - will container filtered dataframe

group: nan

## Example: 
```python
import pandas as pd

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, None, 78, None],
  'Phone Price': [204, None, 501, 800, None]
}

data = pd.DataFrame(phoneDataSet)
print( data[data['Phone Price'].isna()] )
```
```
            Phone  Phone ID.  Phone Price
1        iPhone 6        9.0          NaN
4  Galaxy Note 10        NaN          NaN

```

