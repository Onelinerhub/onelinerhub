# How to use melt() example

```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

melted = pd.melt(df, id_vars =['Phone'], value_vars =['Phone Price'])

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.melt(` - transofrms given dataframe from pivot form (index/column/value) to "wide" form (index/var-name/var-value)
- `id_vars =['Phone']` - columns to use as index
- `value_vars =['Phone Price']` - column to use for variable/value rows

group: melt

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

melted = pd.melt(df, id_vars =['Phone'], value_vars =['Phone Price'])

print(melted)
```
```
  Phone     variable  value
0   ip5  Phone Price    204
1   ip6  Phone Price    304
2   ip8  Phone Price    404
3   sms  Phone Price    405
4    xi  Phone Price    305

```

