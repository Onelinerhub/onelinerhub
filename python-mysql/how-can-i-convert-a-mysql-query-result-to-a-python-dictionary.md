# How can I convert a MySQL query result to a Python dictionary?
// plain

The easiest way to convert a MySQL query result to a Python dictionary is to use the **fetchall()** method of the MySQL cursor object. This method returns a list of tuples, each tuple containing the data for a single row in the query result. The **dict()** constructor can then be used to convert the list of tuples into a dictionary where the first element of each tuple is used as the key and the second element as the value.

## Example code

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="passwd",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

customer_dict = dict(myresult)

print(customer_dict)
```
## Output example

```
{1: 'John', 2: 'Peter', 3: 'Amy', 4: 'Hannah'}
```

The example code above:
* imports the mysql.connector module (line 1)
* creates a connection to the MySQL database (lines 3-6)
* executes a query to select all rows from the customers table (line 8)
* stores the query result in the myresult variable (line 9)
* uses the dict() constructor to convert the list of tuples into a dictionary (line 11)
* prints the resulting dictionary (line 12)

## Helpful links
* [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
* [Python dict()](https://docs.python.org/3/library/functions.html#func-dict)

onelinerhub: [How can I convert a MySQL query result to a Python dictionary?](https://onelinerhub.com/python-mysql/how-can-i-convert-a-mysql-query-result-to-a-python-dictionary)