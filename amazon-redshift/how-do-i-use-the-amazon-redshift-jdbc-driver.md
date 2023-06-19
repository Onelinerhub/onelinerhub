# How do I use the Amazon Redshift JDBC driver?
// plain

1. Download the Amazon Redshift JDBC driver from the [Amazon Redshift JDBC Driver Download Page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html).

2. Add the downloaded `RedshiftJDBC42-no-awssdk-1.2.45.1069.jar` file to your project's classpath.

3. Create a JDBC connection to your Amazon Redshift cluster using the following code:
```java
String url = "jdbc:redshift://<cluster_endpoint>:<port>/<db_name>";
String user = "<db_user>";
String password = "<db_password>";

Connection conn = DriverManager.getConnection(url, user, password);
```

4. Execute the query against the connection:
```java
String query = "SELECT * FROM information_schema.tables;";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);
while (rs.next()) {
    System.out.println(rs.getString("table_name"));
}
```

5. Output (if any):
```
pg_catalog
stl_alert_event_log
stl_analyze
stl_archive_restore
...
```

6. Close the connection and statement when done:
```java
rs.close();
stmt.close();
conn.close();
```

7. For more information, refer to the [Amazon Redshift JDBC Driver Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html).

onelinerhub: [How do I use the Amazon Redshift JDBC driver?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-jdbc-driver)