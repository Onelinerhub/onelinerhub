# How can I use SQLite with Maui?
// plain

SQLite is a lightweight, open source, relational database management system (RDBMS) that can be used with Maui. It is a self-contained, serverless, zero-configuration, transactional SQL database engine.

To use SQLite with Maui, you need to install the SQLite3 library. You can then use the SQLite3 C++ API to create a database and perform various operations on it.

For example, the following code snippet creates a database and a table in it:

```
#include <sqlite3.h>

int main()
{
    sqlite3 *db;
    int rc;

    // Open/create a database
    rc = sqlite3_open("test.db", &db);

    // Create a table
    char *sql = "CREATE TABLE IF NOT EXISTS test_table(id INTEGER PRIMARY KEY, name TEXT);";
    rc = sqlite3_exec(db, sql, 0, 0, 0);

    // Close the database
    sqlite3_close(db);

    return 0;
}
```

This code creates a database named `test.db` and a table named `test_table` with two columns `id` and `name`, where `id` is the primary key.

You can then use SQLite3 C++ API to perform various operations like inserting data into the table, querying the table, updating the data, and deleting the data.

## Helpful links

- [SQLite3 C++ API Documentation](https://www.sqlite.org/c3ref/intro.html)
- [SQLite3 Tutorial](https://www.sqlitetutorial.net/sqlite-cpp/)

onelinerhub: [How can I use SQLite with Maui?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-maui)