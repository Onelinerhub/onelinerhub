# How to drop duplicates from dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'Phone':       ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df.drop_duplicates()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.drop_duplicates(` - drops given dataframe duplicates (by default, find duplicates based on all columns values)

group: duplicates

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone':       ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df.drop_duplicates()

print(df)
```
```
  Phone  Price
0   ip5    204
1   ip6    304
2   ip8    404
3   sms    405

```

