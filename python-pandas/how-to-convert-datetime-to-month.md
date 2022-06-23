# How to convert datetime to month

```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2000 14:43:24', '3/11/2000 14:43:24', '3/12/2000 14:43:24'],
  'value': [2, 3, 4]
})

df['month'] = pd.to_datetime(df['date_time_str']).dt.month
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `date_time_str` - string column with date & time
- `'month'` - column will contain month
- `.dt.month` - extracts month from datetime column

group: datetime

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2000 14:43:24', '3/11/2000 14:43:24', '3/12/2000 14:43:24'],
  'value': [2, 3, 4]
})

df['month'] = pd.to_datetime(df['date_time_str']).dt.month
print(df)
```
```
        date_time_str  value  date
0  3/10/2000 14:43:24      2     3
1  3/11/2000 14:43:24      3     3
2  3/12/2000 14:43:24      4     3

```

