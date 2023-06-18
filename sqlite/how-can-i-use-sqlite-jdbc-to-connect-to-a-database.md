# How can I use SQLite JDBC to connect to a database?
// plain

SQLite JDBC is a Java Database Connectivity (JDBC) driver for SQLite, a lightweight, disk-based database. To connect to an SQLite database using JDBC, you need to have the SQLite JDBC driver and Java set up on the machine where the code will be executed.

The following example shows how to connect to an SQLite database using JDBC:

```java
//Register the driver
Class.forName("org.sqlite.JDBC");

//Open the connection
Connection conn = DriverManager.getConnection("jdbc:sqlite:C:/sqlite/db/mydb.db");
```

## Code explanation


1. Class.forName("org.sqlite.JDBC"): This line registers the SQLite JDBC driver.
2. DriverManager.getConnection("jdbc:sqlite:C:/sqlite/db/mydb.db"): This line opens the connection to the database.

## Helpful links

- [SQLite JDBC Driver](https://bitbucket.org/xerial/sqlite-jdbc)
- [Connecting to an SQLite Database](https://www.sqlitetutorial.net/sqlite-java/sqlite-jdbc/)

onelinerhub: [How can I use SQLite JDBC to connect to a database?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-jdbc-to-connect-to-a-database)