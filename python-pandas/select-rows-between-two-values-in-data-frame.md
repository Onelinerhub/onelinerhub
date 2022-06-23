# Select dataframe rows between two values

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['price'].between(300,400)]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.between(300,400)` - finds rows with `price` value between `300` and `400`
- `found` - will contain filtered dataframe

group: query

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['price'].between(300,400)]
print(found)
```
```
  phone  price
1   ip6    304
4    xi    305

```

