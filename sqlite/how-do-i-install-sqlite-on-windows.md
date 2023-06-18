# How do I install SQLite on Windows?
// plain

1. Download the latest version of [SQLite](https://www.sqlite.org/download.html) for Windows, and extract the zip file to the desired folder.

2. Install the pre-release version of the [SQLite ODBC driver](https://www.ch-werner.de/sqliteodbc/) for Windows.

3. Open the Windows command prompt and navigate to the folder where you extracted the SQLite zip file.

4. Enter the following command to create a new database: `sqlite3 test.db`.

5. Enter `.tables` to view the tables in the database.

6. Enter `.quit` to exit the SQLite command prompt.

7. To access the database from a programming language, use the `sqlite3` module. For example, in Python:

```
import sqlite3
conn = sqlite3.connect('test.db')
c = conn.cursor()
```

The output of this code will be a connection object.

onelinerhub: [How do I install SQLite on Windows?](https://onelinerhub.com/sqlite/how-do-i-install-sqlite-on-windows)