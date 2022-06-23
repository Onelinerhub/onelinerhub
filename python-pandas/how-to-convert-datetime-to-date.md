# How to convert datetime to date

```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2000 14:43:24', '3/11/2000 14:43:24', '3/12/2000 14:43:24'],
  'value': [2, 3, 4]
})

df['date'] = pd.to_datetime(df['date_time_str']).dt.date
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `date_time_str` - string column with date & time
- `'date'` - column will contain date
- `.dt.date` - extracts date from datetime column

group: datetime

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2000 14:43:24', '3/11/2000 14:43:24', '3/12/2000 14:43:24'],
  'value': [2, 3, 4]
})

df['date'] = pd.to_datetime(df['date_time_str']).dt.date
print(df)
```
```
        date_time_str  value        date
0  3/10/2000 14:43:24      2  2000-03-10
1  3/11/2000 14:43:24      3  2000-03-11
2  3/12/2000 14:43:24      4  2000-03-12

```

