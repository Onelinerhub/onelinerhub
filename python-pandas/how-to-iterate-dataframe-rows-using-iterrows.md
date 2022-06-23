# How to iterate dataframe rows using iterrows()

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

for index, series in df.iterrows():
  print(index, series['phone'], series['price'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.iterrows()` - allows iterating over dataframe rows as a pair of `index` and `series`
- `index` - will contain row index
- `series` - will contain row columns values

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

for index, series in df.iterrows():
  print(index, series['phone'], series['price'])
```
```
0 ip5 204
1 ip6 704
2 ip8 404
3 sms 405
4 xi 305

```

