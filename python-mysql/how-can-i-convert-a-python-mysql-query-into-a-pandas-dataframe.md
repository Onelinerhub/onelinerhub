# How can I convert a Python MySQL query into a pandas DataFrame?
// plain

To convert a Python MySQL query into a pandas DataFrame, first install the `mysql-connector-python` library. Then, create a connection to the MySQL database using the `connect()` method. After that, execute the SQL query using the `execute()` method. Finally, create a `pandas.DataFrame()` object and pass the result of the query to the `DataFrame()` constructor.

## Example code

```python
import mysql.connector
import pandas as pd

# create connection
connection = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="database"
)

# execute query
cursor = connection.cursor()
cursor.execute("SELECT * FROM table")

# create DataFrame
df = pd.DataFrame(cursor.fetchall())
```

## Code explanation

- `import mysql.connector`: imports the mysql-connector-python library
- `connection = mysql.connector.connect()`: creates a connection to the MySQL database
- `cursor.execute("SELECT * FROM table")`: executes the SQL query
- `df = pd.DataFrame(cursor.fetchall())`: creates a pandas DataFrame object from the query result

## Helpful links
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Pandas DataFrame Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

onelinerhub: [How can I convert a Python MySQL query into a pandas DataFrame?](https://onelinerhub.com/python-mysql/how-can-i-convert-a-python-mysql-query-into-a-pandas-dataframe)