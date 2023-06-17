# How can I use Python and MySQL JDBC to connect to a database?
// plain

Connecting to a database with Python and MySQL JDBC is an easy process. To do so, you'll need to install the MySQL JDBC driver and set up the connection.

1. Install the MySQL JDBC driver:
    * Download the driver from the MySQL website: [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/).
    * Unzip the driver and add the `mysql-connector-java-<version>-bin.jar` file to your classpath.

2. Set up the connection:
    ```
    import java.sql.DriverManager
    conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/<database>", "<user>", "<password>")
    ```

3. Execute queries:
    ```
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM <table>")
    print(cursor.fetchall())
    ```

4. Close the connection:
    ```
    cursor.close()
    conn.close()
    ```

For more information, please refer to the [MySQL Connector/J documentation](https://dev.mysql.com/doc/connector-j/8.0/en/).

onelinerhub: [How can I use Python and MySQL JDBC to connect to a database?](https://onelinerhub.com/python-mysql/how-can-i-use-python-and-mysql-jdbc-to-connect-to-a-database)