# How do I use SQLite with Qt?
// plain

SQLite is a popular open source database engine that can be used with Qt. To use SQLite with Qt, you must first create a database connection using the QSqlDatabase class. Then, you can create a query using the QSqlQuery class and execute it to perform database operations, such as inserting, updating, and deleting data.

Below is an example of how to use SQLite with Qt:

```
// Create a database connection
QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
db.setDatabaseName("test.db");

// Open the connection
if (!db.open()) {
    qDebug() << "Error: connection with database fail";
} else {
    qDebug() << "Database: connection ok";
}

// Create a query
QSqlQuery query;

// Execute the query
query.exec("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)");

// Output
qDebug() << "Table created!";
```

## Output example

```
Database: connection ok
Table created!
```

The code above does the following:

1. Creates a database connection using the QSqlDatabase class.
2. Opens the connection.
3. Creates a query using the QSqlQuery class.
4. Executes the query to create a table.
5. Outputs a message when the table is created.

For more information, please refer to the following links:

- [Qt SQL Module](https://doc.qt.io/qt-5/sql-index.html)
- [QSqlDatabase Class Reference](https://doc.qt.io/qt-5/qsqldatabase.html)
- [QSqlQuery Class Reference](https://doc.qt.io/qt-5/qsqlquery.html)

onelinerhub: [How do I use SQLite with Qt?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-with-qt)