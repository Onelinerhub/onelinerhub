# How to replace values in data frame

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df['Phone'] = df["Phone"].replace("ip6", "Iphone 6")
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df["Phone"]` - column to find and replace values in
- `.replace(` - replace values in given column
- `"ip6"` - value to find
- `"Iphone 6"` - value to replace by

group: replace

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df['Phone'] = df["Phone"].replace("ip6", "Iphone 6")
print(df)
```
```
      Phone  Phone Price
0       ip5          204
1  Iphone 6          304
2       ip8          404
3       sms          405
4        xi          305

```

