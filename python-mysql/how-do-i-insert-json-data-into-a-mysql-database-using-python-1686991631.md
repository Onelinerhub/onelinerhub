# How do I insert JSON data into a MySQL database using Python?
// plain

To insert JSON data into a MySQL database using Python, the following steps can be taken:

1. Install the MySQL Connector for Python. This can be done using the command `pip install mysql-connector-python`.
2. Create a connection to the MySQL database using the `connect()` method. An example of this is shown below:
```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)
```
3. Create a cursor object using the `cursor()` method, which will allow us to execute SQL commands.
```
mycursor = mydb.cursor()
```
4. Create a JSON string to be inserted into the database.
```
json_data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
```
5. Convert the JSON string to a Python dictionary using the `json.loads()` method.
```
import json

json_dict = json.loads(json_data)
```
6. Use the `execute()` method to insert the JSON data into the database.
```
sql = "INSERT INTO customers (name, age, city) VALUES (%s, %s, %s)"
val = (json_dict['name'], json_dict['age'], json_dict['city'])

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```
7. Output: `1 record inserted.`

## Helpful links
- https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
- https://www.w3schools.com/python/python_json.asp

onelinerhub: [How do I insert JSON data into a MySQL database using Python?](https://onelinerhub.com/python-mysql/how-do-i-insert-json-data-into-a-mysql-database-using-python-1686991631)