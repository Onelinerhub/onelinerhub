# How to convert datetime to year

```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2022 14:43:24', '3/11/2022 14:43:24', '3/12/2022 14:43:24'],
  'value': [1,2,3]
})

df['year'] = pd.to_datetime(df['date_time_str']).dt.year
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `date_time_str` - string column with date & time
- `'year'` - column will contain year
- `.dt.year` - extracts year from datetime column

group: datetime

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'date_time_str': ['3/10/2000 14:43:24', '3/11/2000 14:43:24', '3/12/2000 14:43:24'],
  'value': [2, 3, 4]
})

df['year'] = pd.to_datetime(df['date_time_str']).dt.year
print(df)
```
```
        date_time_str  value  year
0  3/10/2000 14:43:24      2  2000
1  3/11/2000 14:43:24      3  2000
2  3/12/2000 14:43:24      4  2000

```

