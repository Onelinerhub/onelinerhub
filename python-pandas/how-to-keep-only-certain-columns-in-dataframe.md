# How to keep only certain columns in dataframe

### In order to keep only specific columns, we can select needed columns and overwrite our dataframe:

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df = df[['Phone', 'Color']]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `['Phone', 'Color']` - list of columns to keep in `df` dataframe

group: fetch_columns

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df = df[['Phone', 'Color']]

print(df)
```
```
  Phone  Color
0   ip5    red
1   ip6    red
2   ip8   gray
3   sms  black
4    xi    red

```

