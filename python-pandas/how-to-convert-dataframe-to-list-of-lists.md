# How to convert dataframe to list of lists

### As opposed to converting single [column values to list](/python-pandas/convert-dataframe-column-values-to-list) we can also convert full dataframe to list:

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

list = data.values
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.values` - returns dataframe values as an multidimensional array

group: to_list

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

list = data.values

print(list)
```
```
[['US' 'ip5' 204.0]
 ['US' 'ip6' 304.0]
 ['US' 'ip8' nan]
 ['KR' 'sms' 405.0]
 ['KR' 'xi' nan]]

```

