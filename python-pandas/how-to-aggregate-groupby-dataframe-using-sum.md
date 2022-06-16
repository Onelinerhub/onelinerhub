# How to aggregate (groupby) dataframe using sum

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

res = data.groupby(['Vendor']).sum()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.groupby(` - groups given dataframe by list of columns
- `.sum()` - calculate sums for grouped values
- `res` - will contain aggregated dataframe

group: aggregate

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

res = data.groupby(['Vendor']).sum()
print(res)
```
```
        Phone Price
Vendor             
KR              710
US              912

```

