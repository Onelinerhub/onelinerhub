# How do I use the Amazon Redshift JDBC driver with Maven?
// plain

Using the Amazon Redshift JDBC driver with Maven is a straightforward process. First, you need to add the driver as a Maven dependency in your pom.xml file:

```
<dependency>
    <groupId>com.amazon.redshift</groupId>
    <artifactId>redshift-jdbc42</artifactId>
    <version>1.2.45.1060</version>
</dependency>
```

Once the dependency is added, you can use the driver in your code:

```
// Create the connection
String url = "jdbc:redshift://<host>:<port>/<database>";
String user = "<user>";
String password = "<password>";
Connection con = DriverManager.getConnection(url, user, password);

// Execute a query
Statement stmt = con.createStatement();
String query = "SELECT * FROM my_table";
ResultSet rs = stmt.executeQuery(query);

// Iterate through the result set
while (rs.next()) {
    System.out.println(rs.getString("column_name"));
}

// Clean up
rs.close();
stmt.close();
con.close();
```

The code above will connect to the specified Redshift database, execute the query and iterate through the results.

## Code explanation


1. Adding the driver as a Maven dependency in your pom.xml file - `<dependency>...</dependency>`
2. Creating the connection - `Connection con = DriverManager.getConnection(url, user, password)`
3. Executing a query - `ResultSet rs = stmt.executeQuery(query)`
4. Iterating through the result set - `while (rs.next()) {...}`
5. Clean up - `rs.close(); stmt.close(); con.close();`

## Helpful links

- [Amazon Redshift JDBC Driver Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)
- [Maven Dependency Documentation](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

onelinerhub: [How do I use the Amazon Redshift JDBC driver with Maven?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-jdbc-driver-with-maven)