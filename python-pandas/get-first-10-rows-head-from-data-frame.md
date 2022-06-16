# Get first 10 rows (head) from data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

rows = data.head(10)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.head(` - returns first given amount of rows
- `(10)` - return first 10 rows
- `rows` - will contain selected rows

group: n_rows

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

rows = data.head(10)
print(rows)
```
```
  Phone  Phone Price
0   ip5          204
1   ip6          304
2   ip8          404
3   sms          405
4    xi          305

```

