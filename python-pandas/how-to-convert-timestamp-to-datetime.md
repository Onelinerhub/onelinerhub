# How to convert timestamp to datetime

```python
import pandas as pd

df = pd.DataFrame({
  'timestamp': ['1655977822', '1655977821', '1655977803'],
  'value': [1,2,3]
})

df['date'] = pd.to_datetime(df['timestamp'], unit='s')

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `unit='s'` - needed to treat given value as unix timestamp
- `'date'` - column with datetime type

group: datetime

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'timestamp': ['1655977822', '1655977821', '1655977803'],
  'value': [1,2,3]
})

df['date'] = pd.to_datetime(df['timestamp'], unit='s')

print(df)
```
```
    timestamp  value                date
0  1655977822      1 2022-06-23 09:50:22
1  1655977821      2 2022-06-23 09:50:21
2  1655977803      3 2022-06-23 09:50:03

```

