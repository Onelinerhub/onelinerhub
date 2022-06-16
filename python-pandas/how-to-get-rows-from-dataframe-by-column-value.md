# How to get rows from dataframe by column value

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

row = data[data['Phone'] == 'ip8'].iloc(0)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.iloc[` - returns row by given integer position (starts from `0`)
- `[2]` - selects 3rd row (index starts from `0`)

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

row = data[data['Phone'] == 'ip8']
print(row)
```
```
  Vendor Phone  Price  Used
2     US   ip8    102    80

```

