# How to select null values from dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', None, 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['phone'].isna()]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.isna()` - finds all `NaN` values
- `found` - will contain filtered dataframe

group: null

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', None, 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['phone'].isna()]
print(found)
```
```
  phone  price
2  None    404

```

