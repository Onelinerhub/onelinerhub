# How do I use the PostgreSQL JDBC driver?
// plain

The PostgreSQL JDBC driver is a Java library used to connect to a PostgreSQL database. To use it, you must include the driver jar in your classpath and then use the JDBC API to create a connection.

## Example code

```
// Load the PostgreSQL JDBC driver
Class.forName("org.postgresql.Driver");

// Establish a connection
String url = "jdbc:postgresql://localhost:5432/dbname";
String username = "username";
String password = "password";
Connection conn = DriverManager.getConnection(url, username, password);
```

The code above:
1. Loads the PostgreSQL JDBC driver class `org.postgresql.Driver`.
2. Establishes a connection to a PostgreSQL database using the `DriverManager.getConnection()` method. This method takes the database URL, username, and password as parameters.

## Helpful links
- PostgreSQL JDBC Driver Documentation: https://jdbc.postgresql.org/documentation/head/index.html
- JDBC API Documentation: https://docs.oracle.com/javase/8/docs/api/java/sql/package-summary.html

onelinerhub: [How do I use the PostgreSQL JDBC driver?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-jdbc-driver)