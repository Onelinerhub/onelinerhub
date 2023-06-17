# How can I use Docker Compose to set up a MySQL database in Python?
// plain

Docker Compose can be used to set up a MySQL database in Python. First, create a `docker-compose.yml` file with the following content:

```
version: '3'

services:
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
    ports:
      - "3306:3306"
```

Then, run the `docker-compose up` command to start the MySQL server. You can then connect to the MySQL server using Python's `mysql.connector` library.

```
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootpass"
)

print(mydb)

# Output: <mysql.connector.connection.MySQLConnection object at 0x7f8e856e9d30>
```

The following parts are used to set up a MySQL database in Python with Docker Compose:

1. Create a `docker-compose.yml` file with the configuration for the MySQL server.
2. Run the `docker-compose up` command to start the MySQL server.
3. Connect to the MySQL server using Python's `mysql.connector` library.

## Helpful links

- [Docker Compose](https://docs.docker.com/compose/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)

onelinerhub: [How can I use Docker Compose to set up a MySQL database in Python?](https://onelinerhub.com/python-mysql/how-can-i-use-docker-compose-to-set-up-a-mysql-database-in-python)