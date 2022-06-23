# How to find duplicates in data frame

```python
import pandas as pd

df = pd.DataFrame({
  'Phone':       ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df[df.duplicated()]

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.duplicated(` - find duplicated rows and return boolean array (which can be used to filter dataframe)
- `df[` - filter dataframe based on given expression

group: duplicates

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone':       ['ip5', 'ip6', 'ip8', 'sms', 'ip5'],
  'Price': [204,   304,   404,   405,   204  ]
})

df = df[df.duplicated()]

print(df)
```
```
  Phone  Price
4   ip5    204

```

