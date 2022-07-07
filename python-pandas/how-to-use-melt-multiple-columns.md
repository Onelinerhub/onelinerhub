# How to use melt() multiple columns

```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

melted = pd.melt(df, id_vars =['Id'], value_vars =['Phone', 'Phone Price'])

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.melt(` - transofrms given dataframe from pivot form (index/column/value) to "wide" form (index/var-name/var-value)
- `id_vars =['Index']` - columns to use as index
- `['Phone', 'Phone Price']` - columns to use for variable/value rows (you can list many columns here)

group: melt

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

melted = pd.melt(df, id_vars =['Id'], value_vars =['Phone', 'Phone Price'])

print(melted)
```
```
   Id     variable value
0   1        Phone   ip5
1  10        Phone   ip6
2  12        Phone   ip8
3  15        Phone   sms
4  34        Phone    xi
5   1  Phone Price   204
6  10  Phone Price   304
7  12  Phone Price   404
8  15  Phone Price   405
9  34  Phone Price   305

```

