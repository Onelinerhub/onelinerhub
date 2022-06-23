# How to save dataframe to Mysql

```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://test:test@localhost/test?charset=utf8mb4")

import pandas as pd
df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.to_sql('phones', engine)
```

- `sqlalchemy` - lib to work with databases
- `create_engine` - creates database connection with specified credentials
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_sql(` - saves current dataframe to the specified table using given db connection
- `'phones'` - name of the table to save dataframe to (table will be automatically created)

group: sql

## Example: 
```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://test:test@localhost/test?charset=utf8mb4")

import pandas as pd
df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

df.to_sql('phones', engine)

print('ok, written "phones" table')
```
```
ok, written "phones" table

```

