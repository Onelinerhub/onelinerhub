# How to filter dataframe by column value

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['price'] > 304]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `'price'` - column name to filter based on
- `df['price'] > 304` - expression to filter based on (`price` column values are greater than `304`)
- `df[` - filters dataframe based on given expression and returns filtered rows
- `found` - will contain filtered dataframe

group: query

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['price'] > 304]
print(found)
```
```
  phone  price
2   ip8    404
3   sms    405
4    xi    305

```

