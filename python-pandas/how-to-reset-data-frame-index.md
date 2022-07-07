# How to reset data frame index

```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df = df.set_index('Id')
df = df.reset_index()

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.set_index(` - uses specified column as index for dataframe rows
- `.reset_index()` - resets index to default values

group: index

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df = df.set_index('Id')
print(df)

df = df.reset_index()
print(df)
```
```
   Phone  Phone Price
Id                   
1    ip5          204
10   ip6          304
12   ip8          404
15   sms          405
34    xi          305
   Id Phone  Phone Price
0   1   ip5          204
1  10   ip6          304
2  12   ip8          404
3  15   sms          405
4  34    xi          305

```

