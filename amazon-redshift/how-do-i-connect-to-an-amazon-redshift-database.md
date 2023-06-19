# How do I connect to an Amazon Redshift database?
// plain

1. **Step 1:** Install the Amazon Redshift JDBC Driver.
   - Download the driver from [Amazon Redshift JDBC Driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)
   - Unzip the driver and add it to your classpath

2. **Step 2:** Create a JDBC Connection.
   - Create a new connection with the following code:
   ```
   Connection conn = DriverManager.getConnection(
       "jdbc:redshift://<hostname>:<port>/<database>",
       "<username>",
       "<password>");
   ```

3. **Step 3:** Run a SQL Query.
   - Once the connection is established, you can run a SQL query with the following code:
   ```
   Statement stmt = conn.createStatement();
   ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");
   ```

4. **Step 4:** Process the Results.
   - After the query is executed, you can process the results with the following code:
   ```
   while (rs.next()) {
       String col1 = rs.getString("column1");
       String col2 = rs.getString("column2");
       ...
   }
   ```

5. **Step 5:** Close the Connection.
   - Finally, you can close the connection with the following code:
   ```
   conn.close();
   ```

6. **Optional Step 6:** Use a Database Management Tool.
   - You can also use a database management tool like [SQL Workbench](https://www.sql-workbench.eu/) to connect to your Amazon Redshift database.

7. **Optional Step 7:** Use the Amazon Redshift CLI.
   - You can also use the Amazon Redshift CLI to connect to your database. See the [Amazon Redshift CLI Documentation](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html) for more information.

onelinerhub: [How do I connect to an Amazon Redshift database?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-an-amazon-redshift-database)