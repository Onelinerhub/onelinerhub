# Fill empty data frame values with fillna()

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

data = data.fillna(100)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.fillna(` - fills `NaN` values with given value
- `100` - in our case we replace `NaN` values with `100`

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, None, 405, None]
})

data = data.fillna(100)

print(data)
```
```
  Vendor Phone  Phone Price
0     US   ip5        204.0
1     US   ip6        304.0
2     US   ip8        100.0
3     KR   sms        405.0
4     KR    xi        100.0

```

