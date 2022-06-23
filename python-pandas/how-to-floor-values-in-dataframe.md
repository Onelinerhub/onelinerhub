# How to floor values in dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204.10, 304.99, 404.5, 405.5, 305.90]
})

df = df.apply(np.floor)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.round()` - will round all numeric column values

group: rounding

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204.10, 304.99, 404.5, 405.5, 305.90]
})

df = df.floor()
print(df)
```

