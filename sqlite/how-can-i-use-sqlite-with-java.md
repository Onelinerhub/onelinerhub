# How can I use SQLite with Java?
// plain

SQLite is a popular open source SQL database engine that is used for storing structured data in mobile devices, web browsers, and operating systems. It can be used with Java through the SQLite JDBC driver.

The following example code shows how to connect to an SQLite database, create a table, insert data into the table, and query the table:

```
// Load the SQLite JDBC driver
Class.forName("org.sqlite.JDBC");

// Connect to the database
Connection connection = DriverManager.getConnection("jdbc:sqlite:test.db");

// Create the table
Statement statement = connection.createStatement();
statement.executeUpdate("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)");

// Insert data
statement.executeUpdate("INSERT INTO people VALUES ('John', 30)");
statement.executeUpdate("INSERT INTO people VALUES ('Jane', 25)");

// Query the table
ResultSet results = statement.executeQuery("SELECT * FROM people");
while (results.next()) {
  System.out.println("Name: " + results.getString("name"));
  System.out.println("Age: " + results.getInt("age"));
}
```

## Output example

```
Name: John
Age: 30
Name: Jane
Age: 25
```

The code above consists of the following parts:

1. Load the SQLite JDBC driver: The `Class.forName` method is used to load the SQLite JDBC driver.
2. Connect to the database: The `DriverManager.getConnection` method is used to connect to the database.
3. Create the table: The `executeUpdate` method is used to create the table.
4. Insert data: The `executeUpdate` method is used to insert data into the table.
5. Query the table: The `executeQuery` method is used to query the table.
6. Process the result: The `next` and `getXXX` methods are used to process the result.

For more information, please refer to the [SQLite JDBC Driver](https://github.com/xerial/sqlite-jdbc) and [SQLite Java Tutorial](https://www.sqlitetutorial.net/sqlite-java/).

onelinerhub: [How can I use SQLite with Java?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-java)