# How do I connect to Amazon Redshift using JDBC?
// plain

1. Download the Amazon Redshift JDBC driver from the [Amazon Redshift JDBC driver download page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)
2. Add the driver to your classpath.
3. Create a JDBC connection URL using the following syntax:
```
jdbc:redshift://<hostname>:<port>/<dbname>
```
where `<hostname>` is the endpoint of your cluster, `<port>` is the port your cluster is using, and `<dbname>` is the name of your database.
4. Establish a connection using the `DriverManager.getConnection()` method, passing in the connection URL, username, and password as parameters.

```
String url = "jdbc:redshift://examplecluster.1234567890.us-west-2.redshift.amazonaws.com:5439/dev";
String user = "awsuser";
String password = "mypassword";

Connection con = DriverManager.getConnection(url, user, password);
```
5. Once the connection is established, you can execute SQL statements using the `Statement` or `PreparedStatement` interfaces.

```
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");
while (rs.next()) {
    System.out.println(rs.getString("column1"));
}
```
6. When you are finished, close the connection using the `Connection.close()` method.

```
con.close();
```
7. For more information, refer to the [Amazon Redshift JDBC Driver Developer Guide](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html).

onelinerhub: [How do I connect to Amazon Redshift using JDBC?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-amazon-redshift-using-jdbc)