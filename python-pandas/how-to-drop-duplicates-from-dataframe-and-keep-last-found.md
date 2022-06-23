# How to drop duplicates from dataframe and keep last found

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df.drop_duplicates(keep='last')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.drop_duplicates(` - drops given dataframe duplicates (by default, find duplicates based on all columns values)
- `keep='last'` - will keep last found duplicate instead of first

group: duplicates

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone':       ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df.drop_duplicates(keep='last')

print(df)
```
```
  Phone  Price
1   ip6    304
2   ip8    404
3   sms    405
4   ip5    204

```

