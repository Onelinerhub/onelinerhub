# How do I use the PostgreSQL JDBC driver with Maven?
// plain

Using the PostgreSQL JDBC driver with Maven is very simple. First, you need to add the driver to your `pom.xml` file as a Maven dependency:

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.2</version>
</dependency>
```

Then, you can use the driver in your Java code. For example, the following code connects to a PostgreSQL database and prints out the version of the database:

```java
// Load the JDBC driver
Class.forName("org.postgresql.Driver");

// Establish a connection
Connection conn = DriverManager.getConnection("jdbc:postgresql://hostname:port/dbname", "username", "password");

// Print out the version of the database
try (Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT version()")) {
    if (rs.next()) {
        System.out.println(rs.getString(1));
    }
}
```

The output of the above code is the version of the PostgreSQL database, for example:

```
PostgreSQL 11.2
```

For more information on using the PostgreSQL JDBC driver with Maven, see the [official documentation](https://jdbc.postgresql.org/documentation/head/jdbc-maven.html).

onelinerhub: [How do I use the PostgreSQL JDBC driver with Maven?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-jdbc-driver-with-maven)