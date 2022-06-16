# How to convert dataframe to list of dicts

### As opposed to converting single [column values to list](/python-pandas/convert-dataframe-column-values-to-list) we can also convert full dataframe to list:

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

list = data.to_dict('records')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_dict(` - converts given dataframe to dict
- `'records'` - will generate dict based on rows, not columns
- `list` - final list of dicts

group: to_list

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

list = data.to_dict('records')

print(list)
```
```
[{'Vendor': 'US', 'Phone': 'ip5', 'Phone Price': 204.0}, {'Vendor': 'US', 'Phone': 'ip6', 'Phone Price': 304.0}, {'Vendor': 'US', 'Phone': 'ip8', 'Phone Price': nan}, {'Vendor': 'KR', 'Phone': 'sms', 'Phone Price': 405.0}, {'Vendor': 'KR', 'Phone': 'xi', 'Phone Price': nan}]

```

