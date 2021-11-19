# How to get data from Mysql

```python
import mysql.connector

connection = mysql.connector.connect(host='localhost', database='db', user='user', password='pwd')
cursor = connection.cursor()
cursor.execute('SELECT * FROM users')

records = cursor.fetchall()
```

- `import mysql.connector` - library to work with Mysql
- `mysql.connector.connect` - connect to Mysql using specified credentials
- `connection.cursor()` - get cursor object to execute SQL queries
- `cursor.execute` - run specified SQL query
- `cursor.fetchall()` - will return all found rows into list
- `SELECT * FROM users` - example SQL query

group: mysql


## Additional keywords
- query
- fetch
- sql
- rows
