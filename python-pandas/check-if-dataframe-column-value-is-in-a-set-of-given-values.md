# Check if dataframe column value is in a set of given values

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

filtered = data[data['Phone Price'].isin([204,205,304,305])]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.isin(` - checks if value is in a given set (list) of values
- `filtered` - will contain filtered dataframe

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

filtered = data[data['Phone Price'].isin([204,205,304,305])]
print(filtered)
```
```
  Phone  Phone Price
0   ip5          204
1   ip6          304
4    xi          305

```

