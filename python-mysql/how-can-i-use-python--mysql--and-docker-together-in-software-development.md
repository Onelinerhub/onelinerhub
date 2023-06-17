# How can I use Python, MySQL, and Docker together in software development?
// plain

Python, MySQL, and Docker can be used together in software development to create a powerful development environment. For example, a web application can be developed using Python, MySQL, and Docker to create a lightweight, isolated, and highly scalable environment.

## Example code

```
# Create a Docker container using MySQL
docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=mydb -p 3306:3306 mysql

# Connect to the MySQL container from Python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mydb"
)

mycursor = mydb.cursor()

# Execute an SQL query
mycursor.execute("SELECT * FROM customers")

# Print the results
for x in mycursor:
  print(x)
```

## Output example

```
('John', 'Doe', 'john@example.com')
('Mary', 'Moe', 'mary@example.com')
('Julie', 'Dooley', 'julie@example.com')
```

The code above creates a Docker container using MySQL, connects to the container from Python, and executes an SQL query. The output shows the results of the query.

## Code explanation

1. `docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=mydb -p 3306:3306 mysql`: This command creates a Docker container using MySQL.
2. `import mysql.connector`: This imports the MySQL Connector Python module.
3. `mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydb")`: This connects to the MySQL container from Python.
4. `mycursor.execute("SELECT * FROM customers")`: This executes an SQL query.
5. `for x in mycursor: print(x)`: This prints the results of the query.

## Helpful links
- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [Docker Documentation](https://docs.docker.com/)

onelinerhub: [How can I use Python, MySQL, and Docker together in software development?](https://onelinerhub.com/python-mysql/how-can-i-use-python--mysql--and-docker-together-in-software-development)