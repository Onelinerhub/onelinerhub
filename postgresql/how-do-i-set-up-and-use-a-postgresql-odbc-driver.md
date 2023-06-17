# How do I set up and use a PostgreSQL ODBC driver?
// plain

1. Download and install the PostgreSQL ODBC driver of your choice from [here](https://www.postgresql.org/ftp/odbc/versions/).
2. Create a System DSN in the ODBC Data Source Administrator. You can do this by opening the ODBC Data Source Administrator (`odbcad32.exe`) and clicking the "Add" button.
3. Select the driver you just installed in the "Create New Data Source" window.
4. Enter the necessary information, such as the server name, port number, database name, user name, and password.
5. Test the connection to make sure it is working correctly.
6. Use the ODBC driver in your code. For example, in Python you can use the `pyodbc` library to connect to the database:
```
import pyodbc
conn = pyodbc.connect('DSN=mydsn;UID=myuser;PWD=mypassword')
```
7. Execute SQL queries against the database.
```
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable')
rows = cursor.fetchall()
for row in rows:
    print(row)
```

## Output example

```
(1, 'foo', 'bar')
(2, 'baz', 'qux')
```

onelinerhub: [How do I set up and use a PostgreSQL ODBC driver?](https://onelinerhub.com/postgresql/how-do-i-set-up-and-use-a-postgresql-odbc-driver)