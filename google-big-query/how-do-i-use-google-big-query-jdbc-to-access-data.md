# How do I use Google Big Query JDBC to access data?
// plain

Google BigQuery provides a JDBC driver for connecting to BigQuery from Java applications. This driver is available as a part of the Google Cloud SDK.

To use the driver, add the following code to your application:

```
Class.forName("com.google.cloud.sql.Driver");
Connection connection = DriverManager.getConnection(
    "jdbc:google:bigquery://<project-id>:<dataset-id>");
```

The code above creates a connection to a BigQuery project and dataset.

You can then use the connection to execute queries and retrieve the results. For example, the following code will retrieve the number of rows in a table:

```
String query = "SELECT COUNT(*) FROM <table-name>";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
while (resultSet.next()) {
  System.out.println(resultSet.getLong(1));
}
```

The output of the code above would be a single number representing the number of rows in the table.

## Helpful links
- [Google BigQuery JDBC Driver](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-java)
- [BigQuery Java API Documentation](https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-java)

onelinerhub: [How do I use Google Big Query JDBC to access data?](https://onelinerhub.com/google-big-query/how-do-i-use-google-big-query-jdbc-to-access-data)