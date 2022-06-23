# How to query dataframe using multiple conditions

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[(df['price'] > 300) & (df['price'] < 400)]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df['price'] > 304` - first expression for filter
- `df['price'] < 400` - second expression for filter
- ` & ` - logical `and` to use both expressions for filtering
- `found` - will contain filtered dataframe

group: query

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[(df['price'] > 300) & (df['price'] < 400)]
print(found)
```
```
  phone  price
1   ip6    304
4    xi    305

```

