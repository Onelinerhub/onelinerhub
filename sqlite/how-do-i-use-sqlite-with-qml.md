# How do I use SQLite with QML?
// plain

Using SQLite with QML is possible by using the QtSql module. This module provides a database connection and query interface for QML.

The following example code shows how to create a connection to a SQLite database and execute a query:

```javascript
import QtQuick 2.0
import QtSql 2.0

// Create a SQLite database connection
var db = Qt.createQmlObject("QSqlDatabase", Qt.application, "myDatabase");
db.driverName = "QSQLITE";
db.databaseName = "myDatabase.sqlite";
db.open();

// Execute a query
var query = Qt.createQmlObject("QSqlQuery", Qt.application, "myQuery");
query.exec("SELECT * FROM myTable;");
```

The code above will create a connection to a SQLite database named `myDatabase.sqlite` and execute a query to select all records from the `myTable` table.

The query results can then be accessed using the `QSqlQuery` API, for example:

```javascript
while(query.next()) {
    var name = query.value("name");
    console.log("Name: " + name);
}
```

This code will loop through all the query results and print out the value of the `name` column.

For more information, see the following links:

- [QtSql Module Documentation](https://doc.qt.io/qt-5/qtsql-index.html)
- [QSqlDatabase Class Documentation](https://doc.qt.io/qt-5/qsqldatabase.html)
- [QSqlQuery Class Documentation](https://doc.qt.io/qt-5/qsqlquery.html)

onelinerhub: [How do I use SQLite with QML?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-with-qml)