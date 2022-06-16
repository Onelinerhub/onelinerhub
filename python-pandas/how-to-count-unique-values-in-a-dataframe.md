# How to count unique values in a dataframe

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 204, 405, 204]
})

res = data['Phone Price'].nunique()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `'Phone Price'` - column to count unique values in
- `.nunique()` - returns unique values count in a given dataframe
- `res` - will contain unique values count

group: count

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 204, 405, 204]
})

res = data['Phone Price'].nunique()
print(res)
```
```
3

```

