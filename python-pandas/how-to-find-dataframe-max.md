# How to find dataframe max

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305],
  'size':  [100, 101, 101, 99, 95]
})

result = df.max()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.max()` - finds max values for all columns of a dataframe
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

result = df.max()
print(result)
```
```
phone     xi
price    405
size     101
dtype: object

```

