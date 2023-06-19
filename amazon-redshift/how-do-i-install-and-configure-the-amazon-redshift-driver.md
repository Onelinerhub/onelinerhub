# How do I install and configure the Amazon Redshift driver?
// plain

1. Download the Amazon Redshift JDBC driver from the [Amazon Redshift JDBC Driver Download Page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html).
2. Extract the driver to a local directory, for example:
```
$ tar -xzf AmazonRedshiftJDBC42-1.2.1.1001.jar
```
3. Set the Java classpath to the driver directory:
```
$ export CLASSPATH=.:/path/to/driver/AmazonRedshiftJDBC42-1.2.1.1001.jar
```
4. Create a database connection URL. For example:
```
$ jdbc:redshift://examplecluster.1234567890.us-west-2.redshift.amazonaws.com:5439/dev
```
5. Establish a connection to the database using the URL and credentials:
```
$ Connection con = DriverManager.getConnection(url, "username", "password");
```
6. Test the connection by running a query:
```
$ Statement stmt = con.createStatement();
$ ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");
```
7. Close the connection when you are finished:
```
$ con.close();
```

onelinerhub: [How do I install and configure the Amazon Redshift driver?](https://onelinerhub.com/amazon-redshift/how-do-i-install-and-configure-the-amazon-redshift-driver)