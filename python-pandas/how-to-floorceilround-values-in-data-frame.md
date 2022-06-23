# How to round all values in dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204.10, 304.99, 404.5, 405.5, 305.90]
})

df = df.round()
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

df = df.round()
print(df)
```
```
  phone  price
0   ip5  204.0
1   ip6  305.0
2   ip8  404.0
3   sms  406.0
4    xi  306.0

```

