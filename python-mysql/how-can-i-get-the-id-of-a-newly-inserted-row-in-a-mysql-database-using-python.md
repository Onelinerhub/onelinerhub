# How can I get the ID of a newly inserted row in a MySQL database using Python?
// plain

To get the ID of a newly inserted row in a MySQL database using Python, the following steps should be taken:

1. Connect to the MySQL database using the `mysql.connector` library:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()
```

2. Execute an `INSERT` query to add a row to the database:
```
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)
```

3. Use the `lastrowid` attribute of the cursor object to get the ID of the newly inserted row:
```
print(mycursor.lastrowid)
```
## Output example
 `1`

4. Finally, commit the changes to the database using the `commit()` method:
```
mydb.commit()
```

For more information, see the [MySQL Connector Python documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html).

onelinerhub: [How can I get the ID of a newly inserted row in a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-id-of-a-newly-inserted-row-in-a-mysql-database-using-python)