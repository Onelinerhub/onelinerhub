# How to add column to data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data['Color'] = ['black', 'black', 'black', 'red', 'red']
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `['Color']` - adds `Color` column to dataframe

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data['Color'] = ['black', 'black', 'black', 'red', 'red']

print(data)
```
```
  Phone  Phone Price  Color
0   ip5          204  black
1   ip6          304  black
2   ip8          404  black
3   sms          405    red
4    xi          305    red

```

