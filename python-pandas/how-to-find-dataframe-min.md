# How to find dataframe min

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305],
  'size':  [100, 101, 101, 99, 95]
})

result = df.min()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.min()` - finds min values for all columns of a dataframe
- `result` - series with resulting values

group: aggregates

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305],
  'size':  [100, 101, 101, 99, 95]
})

result = df.min()
print(result)
```
```
phone    ip5
price    204
size      95
dtype: object

```

