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

