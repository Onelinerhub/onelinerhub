# How to add row to data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data = data.append({'Phone': 'Nokia', 'Phone Price': 50}, ignore_index = True)

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.append(` - appends given row to dataframe
- `{'Phone': 'Nokia', 'Phone Price': 50}` - sample dict to append to dataframe
- `ignore_index = True` - new row index will be created automatically 

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

data = data.append({'Phone': 'Nokia', 'Phone Price': 50}, ignore_index = True)

print(data)
```
```
   Phone  Phone Price
0    ip5          204
1    ip6          304
2    ip8          404
3    sms          405
4     xi          305
5  Nokia           50

```

