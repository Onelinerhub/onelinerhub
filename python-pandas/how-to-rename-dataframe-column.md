# How to rename dataframe column

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.rename(columns = {'Price':'Phone Price'}, inplace=True)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.rename(` - renames columns
- `'Price'` - column name to rename
- `'Phone Price'` - new column name to rename to
- `inplace=True` - will rename column(s) and save result to current dataframe variable

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.rename(columns = {'Price':'Phone Price'}, inplace = True)

print(df)
```
```
  Phone  Phone Price  Color
0   ip5          204    red
1   ip6          304    red
2   ip8          404   gray
3   sms          405  black
4    xi          305    red

```

