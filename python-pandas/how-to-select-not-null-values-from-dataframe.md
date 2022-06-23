# How to select not null values from dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', None, 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['phone'].notna()]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.notna()` - finds all values that are not `NaN`
- `found` - will contain filtered dataframe

group: null

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', None, 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[df['phone'].notna()]
print(found)
```
```
  phone  price
0   ip5    204
1   ip6    304
3   sms    405
4    xi    305

```

