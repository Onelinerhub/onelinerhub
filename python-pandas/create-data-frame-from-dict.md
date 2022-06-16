# Create data frame from dict

```python
import pandas as pd

dict = {
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
}
data = pd.DataFrame(dict)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `dict` - dict to create dataframe from
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `data` - will contain created dataframe

group: create

## Example: 
```python
import pandas as pd

dict = {
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
}
data = pd.DataFrame(dict)

print(data)
```
```
  Phone  Phone Price
0   ip5          204
1   ip6          304
2   ip8          404
3   sms          405
4    xi          305

```

