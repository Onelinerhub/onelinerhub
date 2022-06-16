# How to count dataframe NaN rows

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', None, 'KR', None],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

res = len(data[data['Vendor'].isna()])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `len(` - returns length (rows count) of a given dataframe
- `.isna()` - filters only `NaN` values
- `Vendor` - column to find `NaN` values in
- `res` - will contain final count

group: count

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', None, 'KR', None],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

res = len(data[data['Vendor'].isna()])
print(res)
```
```
2

```

