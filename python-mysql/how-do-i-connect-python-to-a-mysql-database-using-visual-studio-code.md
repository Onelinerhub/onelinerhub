# How do I connect Python to a MySQL database using Visual Studio Code?
// plain

You can connect Python to a MySQL database using Visual Studio Code by following these steps:

1. Install the Python extension for Visual Studio Code.
2. Install the MySQL connector for Python.
3. Open Visual Studio Code and create a new file.
4. Enter the following code in the file:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb)
```
## Output example

```
<mysql.connector.connection.MySQLConnection object at 0x7f5a0f3c1c50>
```
5. Replace the “yourusername” and “yourpassword” with your MySQL credentials.
6. Run the code by pressing the “Ctrl + F5” keys.
7. If the connection is successful, you will get the output as shown above.

## Helpful links
- [Python Extension for Visual Studio Code](https://code.visualstudio.com/docs/languages/python)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How do I connect Python to a MySQL database using Visual Studio Code?](https://onelinerhub.com/python-mysql/how-do-i-connect-python-to-a-mysql-database-using-visual-studio-code)