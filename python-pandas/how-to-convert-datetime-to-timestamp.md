# How to convert datetime to timestamp

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'date_time_str': ['3/10/2022 14:43:24', '3/11/2022 14:43:24', '3/12/2022 14:43:24'],
  'value': [1,2,3]
})

df['timestamp'] = pd.to_datetime(df['date_time_str']).values.astype(np.int64) // 10 ** 9
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_datetime(` - convert given column values to datetime type (will automatically parse given strings)
- `date_time_str` - string column with date & time
- `'timestamp'` - column will contain timestamp
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.values.astype(np.int64)` - converts datetime to int to get timestamp

group: datetime

## Example: 
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'date_time_str': ['3/10/2022 14:43:24', '3/11/2022 14:43:24', '3/12/2022 14:43:24'],
  'value': [1,2,3]
})

df['timestamp'] = pd.to_datetime(df['date_time_str']).values.astype(np.int64) // 10 ** 9
print(df)
```
```
        date_time_str  value   timestamp
0  3/10/2022 14:43:24      1  1646923404
1  3/11/2022 14:43:24      2  1647009804
2  3/12/2022 14:43:24      3  1647096204

```

