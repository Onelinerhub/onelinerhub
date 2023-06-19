# How can I connect Amazon Redshift to Tableau?
// plain

To connect Amazon Redshift to Tableau, you first need to set up an ODBC connection. This can be done by following these steps:

1. Install the Amazon Redshift ODBC driver on the computer running Tableau Desktop.

2. Configure an ODBC data source on the computer running Tableau Desktop.

3. Connect Tableau Desktop to the ODBC data source.

Here is an example of how to configure an ODBC data source on Windows:

```
1. Open the ODBC Data Source Administrator.

2. Select the System DSN tab.

3. Click Add.

4. Select the Amazon Redshift ODBC driver.

5. Enter a Data Source Name.

6. Enter the server name or IP address of the Amazon Redshift cluster.

7. Enter the port number of the Amazon Redshift cluster.

8. Select the database name.

9. Enter the database user name and password.

10. Click Test Connection to verify the connection.

11. Click OK.
```

Once the ODBC connection has been set up, you can connect Tableau Desktop to the ODBC data source by following these steps:

1. Open Tableau Desktop.

2. Select Connect to Data.

3. Select Other Databases (ODBC).

4. Select the ODBC data source you configured.

5. Enter the database user name and password.

6. Select Sign In.

7. Select the tables and views you want to connect to.

For more information, see [Connect Tableau to Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-tableau.html).

onelinerhub: [How can I connect Amazon Redshift to Tableau?](https://onelinerhub.com/amazon-redshift/how-can-i-connect-amazon-redshift-to-tableau)