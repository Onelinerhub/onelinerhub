# How to use datetime type

```python
import pandas as pd

df = pd.DataFrame({
  'date_str': ['3/10/2000', '3/11/2000', '3/12/2000'],
  'value': [2, 3, 4]
})

df['date'] = pd.to_datetime(df['date_str'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `date_str` - string column with date
- `'date'` - column with datetime type

group: datetime

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'date_str': ['3/10/2022', '3/11/2022', '3/12/2021'],
  'value': [1,2,3]
})

df['date'] = pd.to_datetime(df['date_str'])

print(df)
```
```
    date_str  value       date
0  3/10/2022      1 2022-03-10
1  3/11/2022      2 2022-03-11
2  3/12/2021      3 2021-03-12

```

