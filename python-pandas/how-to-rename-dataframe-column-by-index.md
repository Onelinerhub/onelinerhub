# How to rename dataframe column by index

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

names = list(df.columns)
names[1] = d 
df.columns = names
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df.columns` - list of all columns
- `names = list(df.columns)` - save columns list to `names` variable
- `names[1]` - refers to second column (indexes start from `0`)
- `'Phone Price'` - new name for second column
- `df.columns = names` - set new column names

group: rename

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

names = list(df.columns)
names[1] = 'Phone Price'
df.columns = names

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

