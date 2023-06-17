# How do I download MySQL-Python 1.2.5 zip file?
// plain

1. Visit the [MySQL-Python 1.2.5 download page](https://pypi.org/project/MySQL-python/#files) on PyPI.
2. Select the **MySQL-python-1.2.5.zip** file from the list of available downloads.
3. Click the **Download** button to begin the download.
4. Once the download is complete, open the zip file.
5. Extract the contents of the zip file to a local directory.
6. To verify that the download was successful, use the following Python code to connect to a MySQL database:
```python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database")
```
7. If the connection is successful, you should see the following output:
```
<_mysql.connection open to 'localhost' at 7f8f7c2f5a90>
```

## Helpful links
- [MySQL-Python 1.2.5 download page](https://pypi.org/project/MySQL-python/#files)
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/user_guide.html)

onelinerhub: [How do I download MySQL-Python 1.2.5 zip file?](https://onelinerhub.com/python-mysql/how-do-i-download-mysql-python-------zip-file)