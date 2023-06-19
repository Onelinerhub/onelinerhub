# How can I connect Amazon Redshift to Power BI?
// plain

Connecting Amazon Redshift to Power BI is relatively straightforward. To do so, one must first create an ODBC connection to the Amazon Redshift cluster. To do this, one must first install the Amazon Redshift ODBC driver on the machine that will be used to connect to the cluster.

Once the driver is installed, one can create the ODBC connection by using the `odbcad32.exe` program. This will open the ODBC Data Source Administrator window. From there, one can select the Amazon Redshift driver from the list of available drivers. After filling in the connection information for the cluster, one can click the “Test Connection” button to ensure that the connection is successful.

Once the connection is established, one can open Power BI and select the “Get Data” option. From there, one can select the “ODBC” option from the list of available data sources. After selecting the ODBC option, one can select the Amazon Redshift connection that was created earlier. After selecting the connection, one can then select the desired tables from the Amazon Redshift cluster and load them into Power BI.

Once the data is loaded, one can then use Power BI to create visualizations and reports from the Amazon Redshift data.

```
odbcad32.exe
```

No output.

onelinerhub: [How can I connect Amazon Redshift to Power BI?](https://onelinerhub.com/amazon-redshift/how-can-i-connect-amazon-redshift-to-power-bi)