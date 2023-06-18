# How do I set up an ODBC driver to connect to an SQLite database?
// plain

1. Download and install the ODBC driver for SQLite. This can be found [here](https://www.sqlite.org/download.html).

2. Create a System DSN in the Windows ODBC Data Source Administrator. This can be done by going to Control Panel > Administrative Tools > Data Sources (ODBC).

3. Select the "System DSN" tab and click "Add".

4. Select the SQLite driver from the list and click "Finish".

5. Enter a name for the DSN and click "OK".

6. Enter the full path to the SQLite database file in the Database field and click "OK".

7. Test the connection by using the following code block in a Python script:

```
import pyodbc

conn = pyodbc.connect('DRIVER={SQLite};DSN=my_dsn;Database=C:\\path\\to\\my\\database.db')

cursor = conn.cursor()

cursor.execute('select * from my_table')

for row in cursor:
    print(row)
```

## Output example


```
('value1', 'value2', 'value3')
('value4', 'value5', 'value6')
```

onelinerhub: [How do I set up an ODBC driver to connect to an SQLite database?](https://onelinerhub.com/sqlite/how-do-i-set-up-an-odbc-driver-to-connect-to-an-sqlite-database)