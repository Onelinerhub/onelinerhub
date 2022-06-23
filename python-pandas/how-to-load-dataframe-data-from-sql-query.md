# How to load dataframe data from SQL query

```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://test:test@localhost/test?charset=utf8mb4")

import pandas as pd
df = pd.read_sql('SELECT * FROM phones WHERE Color = "red"', engine, 'index')

```

- `sqlalchemy` - lib to work with databases
- `create_engine` - creates database connection with specified credentials
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `.read_sql(` - creates dataframe and loads data from database
- `SELECT * FROM phones WHERE Color = "red"` - SQL query to get the data ([`phones` table was previously created from dataframe](/python-pandas/how-to-save-dataframe-to-mysql))
- `engine` - database connection
- `'index'` - name of the index column

group: sql

## Example: 
```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://test:test@localhost/test?charset=utf8mb4")

import pandas as pd
df = pd.read_sql('SELECT * FROM phones', engine, 'index')

print(df)
```
```
      Phone  Price  Color
index                    
0       ip5    204    red
1       ip6    304    red
2       ip8    404   gray
3       sms    405  black
4        xi    305    red

```

