# How to change values in a column based on condition

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data.loc[data['Phone Price'] < 400, 'Phone Price'] = data['Phone Price'] + 25;

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.loc[` - locates rows based on filter and updates with given values
- `data['Phone Price'] < 400` - filter to update column values on
- `'Phone Price'` - column name to update values
- `data['Phone Price'] + 25` - new value expression

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data.loc[data['Phone Price'] < 400, 'Phone Price'] = data['Phone Price']+25;

print(data)
```
```
  Phone  Phone Price
0   ip5          229
1   ip6          329
2   ip8          404
3   sms          405
4    xi          330

```

