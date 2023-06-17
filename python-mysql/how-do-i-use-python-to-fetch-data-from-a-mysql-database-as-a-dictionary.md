# How do I use Python to fetch data from a MySQL database as a dictionary?
// plain

Using Python to fetch data from a MySQL database as a dictionary is a fairly straightforward process. First, you must import the necessary libraries:

```python
import MySQLdb
import json
```

Next, you must establish a connection to the database:

```python
db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")
```

Once a connection has been established, you can execute your query:

```python
cur = db.cursor()
cur.execute("SELECT * FROM table_name")
```

You can then fetch the results of the query as a dictionary:

```python
rows = cur.fetchall()
data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]
```

Finally, you can convert the dictionary into a JSON string:

```python
json_string = json.dumps(data)
```

The result of this code will be a JSON string containing the results of your query.

**Parts of the code**

1. `import MySQLdb`: This imports the MySQLdb library, which allows us to interact with a MySQL database.
2. `import json`: This imports the json library, which allows us to convert our data into a JSON string.
3. `db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")`: This establishes a connection to the database.
4. `cur = db.cursor()`: This creates a cursor object, which allows us to execute queries.
5. `cur.execute("SELECT * FROM table_name")`: This executes the query.
6. `rows = cur.fetchall()`: This fetches the results of the query.
7. `data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in rows]`: This converts the results of the query into a dictionary.
8. `json_string = json.dumps(data)`: This converts the dictionary into a JSON string.

**Relevant Links**

- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/user_guide.html#module-MySQLdb)
- [JSON Documentation](https://docs.python.org/3/library/json.html)

onelinerhub: [How do I use Python to fetch data from a MySQL database as a dictionary?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-fetch-data-from-a-mysql-database-as-a-dictionary)