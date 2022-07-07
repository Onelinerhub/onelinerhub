# How to use multiple conditions in mask()

```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df = df.mask((df['Phone Price'] > 400) | (df['Phone Price'] < 300), None)

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.mask(` - masks rows by given filter with specified value 
- `df['Phone Price'] > 400` - first condition to check
- `df['Phone Price'] < 300` - another condition to check
- ` | ` - logical `or` (use `&` for logical `and`)
- `None` - value to replace found values by

group: mask

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df = df.mask((df['Phone Price'] > 400) | (df['Phone Price'] < 300), None)

print(df)
```
```
     Id Phone  Phone Price
0   NaN  None          NaN
1  10.0   ip6        304.0
2   NaN  None          NaN
3   NaN  None          NaN
4  34.0    xi        305.0

```

