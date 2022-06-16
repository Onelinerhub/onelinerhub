# Convert dataframe column values to list

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

lst = data['Phone Price'].tolist()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `'Phone Price'` - column to convert to list
- `.tolist()` - converts given column to list
- `lst` - will contain final list

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

list = data['Phone Price'].tolist()
print(list)
```
```
[204, 304, 404, 405, 305]

```

