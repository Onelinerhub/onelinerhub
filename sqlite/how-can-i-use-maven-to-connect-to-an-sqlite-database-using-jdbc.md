# How can I use Maven to connect to an SQLite database using JDBC?
// plain

Maven can be used to connect to an SQLite database using JDBC. To do this, you will need to add the SQLite JDBC driver to your project's pom.xml file. This can be done by adding the following dependency:

```
<dependency>
    <groupId>org.xerial</groupId>
    <artifactId>sqlite-jdbc</artifactId>
    <version>3.30.1</version>
</dependency>
```

Once the driver is added, you can create a connection to the database using the following code:

```
String dbURL = "jdbc:sqlite:<path-to-sqlite-database>";
Connection conn = DriverManager.getConnection(dbURL);
```

The code above will create a connection to the SQLite database specified in the dbURL string. You can then use this connection to execute SQL statements, query the database, and perform other operations.

## Code explanation


1. Adding the SQLite JDBC driver to the pom.xml file: This is done by adding the dependency listed above. This will allow your project to use the SQLite JDBC driver.

2. Creating a connection to the database: This is done by creating a string containing the path to the database and passing it to the `DriverManager.getConnection()` method. This will create a `Connection` object which can be used to execute SQL statements and query the database.

## Helpful links

- [SQLite JDBC Driver](https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc)
- [Java Database Connectivity (JDBC)](https://docs.oracle.com/javase/tutorial/jdbc/index.html)

onelinerhub: [How can I use Maven to connect to an SQLite database using JDBC?](https://onelinerhub.com/sqlite/how-can-i-use-maven-to-connect-to-an-sqlite-database-using-jdbc)