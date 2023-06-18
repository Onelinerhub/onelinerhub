# How can I use SQLite with Kotlin?
// plain

SQLite is a popular open source SQL database that is well-suited for small to medium web applications. It can be used with Kotlin to store and manipulate data in an efficient and secure manner.

To use SQLite with Kotlin, you will need to add the following dependency to your Gradle build file:

```
implementation 'org.xerial:sqlite-jdbc:3.25.2'
```

You can then create a `Connection` object to connect to an existing SQLite database, or create a new one:

```
val connection = DriverManager.getConnection("jdbc:sqlite:<database_name>.db")
```

Once a connection is established, you can use the `Statement` class to execute SQL queries on the database. For example:

```
val statement = connection.createStatement()
val resultSet = statement.executeQuery("SELECT * FROM <table_name>")
```

You can then use the `ResultSet` object to iterate through the query results and process them as needed.

Finally, you can use the `PreparedStatement` class to execute parameterized queries against the database. This is useful for preventing SQL injection attacks:

```
val statement = connection.prepareStatement("SELECT * FROM <table_name> WHERE id=?")
statement.setInt(1, 123)
val resultSet = statement.executeQuery()
```

Here are some useful links for further reading:
- [SQLite JDBC Driver](https://github.com/xerial/sqlite-jdbc)
- [Kotlin SQLite Tutorial](https://www.tutorialkart.com/kotlin-programming/sqlite-kotlin-example/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How can I use SQLite with Kotlin?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-kotlin)