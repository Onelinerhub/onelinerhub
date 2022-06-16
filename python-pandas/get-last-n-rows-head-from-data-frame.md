# Get last N rows (tail) from data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

rows = data.tail(3)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.tail(` - returns last given amount of rows
- `(3)` - return last 3 rows
- `rows` - will contain selected rows

group: n_rows

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

rows = data.tail(3)
print(rows)
```
```
  Phone  Phone Price
2   ip8          404
3   sms          405
4    xi          305

```

