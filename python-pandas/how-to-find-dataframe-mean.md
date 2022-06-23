# How to find dataframe mean

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305],
  'size':  [100, 101, 101, 99, 95]
})

result = df.mean()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.mean()` - finds mean for all numeric columns of a dataframe
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

result = df.mean()
print(result)
```
```
price    324.4
size      99.2
dtype: float64

```

