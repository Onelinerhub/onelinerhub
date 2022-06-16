# How to get first row from data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

first = data.loc[0]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.loc[` - locates rows based on filter and replaces with given values
- `[0]` - selects first row

group: fetch

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

first = data.loc[0]
print(first)
```
```
Vendor     US
Phone     ip5
Price     204
Used      150
Name: 0, dtype: object

```

