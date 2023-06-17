# How do I install the Python MySQL driver?
// plain

1. Install the Python MySQL driver using the pip package manager.
   ```
   pip install mysql-connector-python
   ```
2. To connect to a MySQL database, you need to use the Connect() method of the mysql.connector module.
   ```
   import mysql.connector
   conn = mysql.connector.connect(host="localhost",user="yourusername",password="yourpassword")
   ```
3. Once you have connected to the database, you can execute queries using the execute() method.
   ```
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM employees")
   ```
4. To fetch the results of the query, you can use the fetchall() method.
   ```
   rows = cursor.fetchall()
   ```
5. Don't forget to close the connection to the database when you're done.
   ```
   conn.close()
   ```
6. For more information on how to use the Python MySQL driver, see the [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/).
7. For more information on the Connect() method, see the [MySQL Connector/Python API Reference](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnector-connect.html).

onelinerhub: [How do I install the Python MySQL driver?](https://onelinerhub.com/python-mysql/how-do-i-install-the-python-mysql-driver)