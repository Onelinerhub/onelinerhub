# How to replace strings in dataframe column

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df['Phone'] = df["Phone"].replace("ip", "Iphone", regex=True)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df["Phone"]` - column to find and replace values in
- `.replace(` - replace values in given column
- `"ip"` - substring to find
- `"Iphone"` - value to replace by
- `regex=True` - enables searching for substrings in string values

group: replace

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df['Phone'] = df["Phone"].replace("ip", "Iphone", regex=True)
print(df)
```
```
     Phone  Phone Price
0  Iphone5          204
1  Iphone6          304
2  Iphone8          404
3      sms          405
4       xi          305

```

