# How to get single row from dataframe by column value

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

row = data[data['Phone'] == 'ip8'].iloc[0]

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `'Phone'` - column name to filter by
- `ip8` - column value to find rows by
- `.iloc[0]` - will return first row from filtered dataframe
- `row` - will contain single found row

group: fetch_by_col

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

row = data[data['Phone'] == 'ip8'].iloc[0]
print(row)
```
```
Vendor     US
Phone     ip8
Price     102
Used       80
Name: 2, dtype: object

```

