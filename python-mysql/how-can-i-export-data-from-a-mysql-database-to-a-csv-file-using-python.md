# How can I export data from a MySQL database to a CSV file using Python?
// plain

Using Python to export data from a MySQL database to a CSV file is a simple process. The following example code can be used to accomplish this task:

```
import csv
import MySQLdb

# Connect to the database
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")

# Create a Cursor object to execute queries
cur = db.cursor()

# Select data from table using SQL query
cur.execute("SELECT * FROM table_name")

# Create a file and write the data to it
with open('filename.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow([i[0] for i in cur.description]) # write headers
    writer.writerows(cur)

# Close the connection
db.close()
```

This code will create a CSV file called `filename.csv` and write the data from the table `table_name` in the database `database` to it.

The code consists of the following parts:

1. `import csv` and `import MySQLdb` - imports the necessary modules for working with CSV files and MySQL databases.
2. `db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")` - establishes a connection to the MySQL database.
3. `cur = db.cursor()` - creates a cursor object to execute queries.
4. `cur.execute("SELECT * FROM table_name")` - selects data from the table using a SQL query.
5. `with open('filename.csv', 'w') as f:` - creates a file and opens it for writing.
6. `writer = csv.writer(f, delimiter=',')` - creates a CSV writer object.
7. `writer.writerow([i[0] for i in cur.description])` - writes the headers to the file.
8. `writer.writerows(cur)` - writes the data from the cursor object to the file.
9. `db.close()` - closes the connection to the database.

## Helpful links

- [MySQLdb Python API](https://mysqlclient.readthedocs.io/user_guide.html)
- [Python CSV Module](https://docs.python.org/3/library/csv.html)

onelinerhub: [How can I export data from a MySQL database to a CSV file using Python?](https://onelinerhub.com/python-mysql/how-can-i-export-data-from-a-mysql-database-to-a-csv-file-using-python)