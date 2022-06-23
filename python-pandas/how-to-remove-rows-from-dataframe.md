# How to remove rows from dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.drop([1,3], inplace=True)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.drop(` - removes specified row from dataframe
- `inplace=True` - will save resulting dataframe to the current variable
- `[1,3]` - will drop second and forth rows (indexes starts at `0`)

group: remove_row

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.drop([1,3], inplace=True)
print(df)
```
```
  Phone  Price Color
0   ip5    204   red
2   ip8    404  gray
4    xi    305   red

```

