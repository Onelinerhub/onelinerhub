# How can I get the column names of a MySQL table using Python?
// plain

Using Python to get column names of a MySQL table is relatively simple. First, you will need to import the `mysql.connector` module.

```python
import mysql.connector
```

Then, establish a connection to your MySQL server, and create a cursor object.

```python
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = mydb.cursor()
```

Next, you need to execute a `DESCRIBE` query on the table you want to get the column names from.

```python
mycursor.execute("DESCRIBE customers")
```

Finally, you can loop through the results of the query and print out the column names.

```python
for x in mycursor:
  print(x[0])

# Output
# id
# name
# address
```

List of Code Parts

1. Import mysql.connector module - `import mysql.connector`
2. Connect to MySQL server and create a cursor object - `mydb = mysql.connector.connect(host="localhost", user="yourusername", passwd="yourpassword"); mycursor = mydb.cursor()`
3. Execute DESCRIBE query - `mycursor.execute("DESCRIBE customers")`
4. Loop through query results and print column names - `for x in mycursor: print(x[0])`

Relevant Links

- [mysql.connector](https://dev.mysql.com/doc/connector-python/en/)
- [DESCRIBE statement](https://dev.mysql.com/doc/refman/8.0/en/describe.html)

onelinerhub: [How can I get the column names of a MySQL table using Python?](https://onelinerhub.com/python-mysql/how-can-i-get-the-column-names-of-a-mysql-table-using-python)