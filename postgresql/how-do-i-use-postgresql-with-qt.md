# How do I use PostgreSQL with Qt?
// plain

Qt is a powerful cross-platform application development framework. PostgreSQL is an open-source object-relational database system. It is possible to use PostgreSQL with Qt to create powerful database applications.

The easiest way to use PostgreSQL with Qt is to use Qt's SQL classes. Qt has a set of classes to access and manage databases. To use PostgreSQL with Qt, you need to install the PostgreSQL driver for Qt.

Once the PostgreSQL driver is installed, you can create a connection to the PostgreSQL server and execute SQL commands. The following example code creates a connection to a PostgreSQL server and executes a simple SQL query:

```
#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlError>

int main(int argc, char *argv[])
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
    db.setHostName("localhost");
    db.setDatabaseName("mydb");
    db.setUserName("postgres");
    db.setPassword("secret");

    if (!db.open()) {
        qDebug() << "Error: connection with database fail";
    } else {
        qDebug() << "Database: connection ok";
    }

    QSqlQuery query;
    query.exec("SELECT * FROM mytable");

    while (query.next()) {
        qDebug() << query.value(0).toString() << query.value(1).toString();
    }
}
```

## Output example

```
Database: connection ok
foo bar
```

The code above:

1. Includes the `QSqlDatabase` and `QSqlQuery` classes that are needed to access and manage databases.
2. Creates a connection to the PostgreSQL server and sets the connection parameters.
3. Executes a simple SQL query.
4. Iterates over the query result and prints the values.

For more information, please refer to the following links:

- [Qt SQL Documentation](https://doc.qt.io/qt-5/sql-index.html)
- [Using PostgreSQL with Qt](https://doc.qt.io/qt-5/sql-driver.html#using-postgresql-with-qt)
- [PostgreSQL Qt Driver Documentation](https://www.postgresql.org/docs/current/qt5-connector.html)

onelinerhub: [How do I use PostgreSQL with Qt?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-with-qt)