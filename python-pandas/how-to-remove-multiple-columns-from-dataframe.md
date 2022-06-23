# How to remove multiple columns from dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.drop(['Price', 'Color'], inplace=True, axis=1)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.drop(` - drops selected column from dataframe
- `['Price', 'Color']` - list of columns to remove
- `inplace=True` - will remove column and overwrite current dataframe variable
- `axis=1` - used to ask Pandas to drop column (not row)

group: drop_column

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.drop(['Price', 'Color'], inplace=True, axis=1)
print(df)
```
```
  Phone
0   ip5
1   ip6
2   ip8
3   sms
4    xi

```

