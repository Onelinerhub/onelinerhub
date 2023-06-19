# How do I install the Amazon Redshift (x64) driver?
// plain

1. Download the Amazon Redshift (x64) driver from the [Amazon Redshift Connector page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html).
2. Install the driver on your computer.
3. Create a DSN (Data Source Name) for the Amazon Redshift driver.
  ```
  # Windows
  C:\> odbcad32.exe

  # Mac OSX
  $ odbcad32
  ```
4. Configure the DSN with the Amazon Redshift connection details.
5. Test the connection.
  ```
  $ isql <dsn> <username> <password>
  +---------------------------------------+
  | Connected!                            |
  |                                       |
  | sql-statement                         |
  | help [tablename]                      |
  | quit                                  |
  |                                       |
  +---------------------------------------+
  SQL>
  ```
6. Once the connection is established, you can use the DSN to connect to Amazon Redshift from any application that supports ODBC.
7. For more information, see the [Amazon Redshift Connector page](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html).

onelinerhub: [How do I install the Amazon Redshift (x64) driver?](https://onelinerhub.com/amazon-redshift/how-do-i-install-the-amazon-redshift--x----driver)