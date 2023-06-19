# How do I download the Amazon Redshift JDBC driver for use in SQL Workbench?
// plain

1. Download the Amazon Redshift JDBC driver from [Amazon Redshift JDBC Driver Download](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver)
2. Extract the downloaded zip file to a local directory.
3. Open SQL Workbench and select `File > Manage Drivers`.
4. In the `Manage Drivers` window, click on `New`.
5. In the `New Driver` window, enter the details as below:
    * Name: `Amazon Redshift JDBC Driver`
    * Library: `Path to the extracted driver jar file`
    * Classname: `com.amazon.redshift.jdbc42.Driver`
6. Click on `OK` to save the driver details.
7. You can now connect to your Amazon Redshift cluster using the `Amazon Redshift JDBC Driver` in SQL Workbench.

```
Example code to connect to Amazon Redshift cluster using SQL Workbench

Connection URL: jdbc:redshift://examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com:5439/dev

Username: mymasteruser

Password: mypassword
```

## Output example

```
Connected
```

onelinerhub: [How do I download the Amazon Redshift JDBC driver for use in SQL Workbench?](https://onelinerhub.com/amazon-redshift/how-do-i-download-the-amazon-redshift-jdbc-driver-for-use-in-sql-workbench)