# How can I use the Google Big Query JDBC driver to access data?
// plain

Google BigQuery JDBC Driver is a powerful tool that enables Java programs to access data stored in BigQuery. To use the driver, you need to first download and install the driver from the [Google Cloud Platform Console](https://console.cloud.google.com/marketplace/details/google-cloud-platform/bigquery-jdbc-driver).

Once the driver is installed, you can use the following code snippet to connect to BigQuery:

```java
// Create a new BigQuery JDBC connection
String url = "jdbc:bigquery://https://www.googleapis.com/bigquery/v2:443";
String projectId = "<your-project-id>";
String datasetId = "<your-dataset-id>";
String tableId = "<your-table-id>";
String user = "<your-username>";
String password = "<your-password>";

Connection connection = DriverManager.getConnection(url, user, password);
```

Once the connection is established, you can use the following code snippet to execute a query and retrieve the results from BigQuery:

```java
// Execute a query
String query = "SELECT * FROM " + projectId + "." + datasetId + "." + tableId;
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);

// Retrieve the results
while (resultSet.next()) {
  // Process the results
  System.out.println(resultSet.getString(1));
  System.out.println(resultSet.getString(2));
  // ...
}
```

Finally, you can close the connection when you are done:

```java
connection.close();
```

This is how you can use the Google BigQuery JDBC driver to access data stored in BigQuery.

onelinerhub: [How can I use the Google Big Query JDBC driver to access data?](https://onelinerhub.com/google-big-query/how-can-i-use-the-google-big-query-jdbc-driver-to-access-data)