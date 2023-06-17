# How can I quickly get started with PostgreSQL?
// plain

1. First, you need to install PostgreSQL on your computer. You can download it from [the official website](https://www.postgresql.org/download/).
2. Once installed, you can start the PostgreSQL server by running the command `pg_ctl -D /usr/local/var/postgres start` in the terminal.
3. Next, you can create a new database with the command `createdb mydb` to create a database called `mydb`.
4. To access the database, you can use the command `psql mydb` to open the PostgreSQL interactive terminal.
5. From here, you can start writing SQL statements to create tables, insert data, and query the database.
6. For example, you can create a table with the command `CREATE TABLE users (id INTEGER PRIMARY KEY, name VARCHAR(255));`.
7. To check if the table was created, you can run the command `\d` which will list all the tables in the database.

```
$ createdb mydb
$ psql mydb
psql (12.3)
Type "help" for help.

mydb=# CREATE TABLE users (id INTEGER PRIMARY KEY, name VARCHAR(255));
CREATE TABLE
mydb=# \d
              List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | users           | table | postgres
(1 row)
```

onelinerhub: [How can I quickly get started with PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-quickly-get-started-with-postgresql)