# How do I format an SQLite database with version 3?
// plain

SQLite version 3 is a popular open source relational database system. Formatting an SQLite database with version 3 can be done using the SQL commands CREATE TABLE and INSERT INTO. The following example code block creates a database called 'mydb' and a table called 'mytable' with columns 'name' and 'age':

```
sqlite3 mydb.db
CREATE TABLE mytable (name TEXT, age INT);
INSERT INTO mytable (name, age) VALUES ('John', 25);
INSERT INTO mytable (name, age) VALUES ('Jane', 30);
```

The output of the above code should be:

```
sqlite> CREATE TABLE mytable (name TEXT, age INT);
sqlite> INSERT INTO mytable (name, age) VALUES ('John', 25);
sqlite> INSERT INTO mytable (name, age) VALUES ('Jane', 30);
```

## Code explanation


- `sqlite3 mydb.db`: This command creates the database file 'mydb.db'.
- `CREATE TABLE mytable (name TEXT, age INT)`: This command creates a table called 'mytable' with two columns, 'name' and 'age'.
- `INSERT INTO mytable (name, age) VALUES ('John', 25)`: This command inserts a row into the table with the values 'John' and 25 for the 'name' and 'age' columns, respectively.
- `INSERT INTO mytable (name, age) VALUES ('Jane', 30)`: This command inserts a row into the table with the values 'Jane' and 30 for the 'name' and 'age' columns, respectively.

## Helpful links

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/index.htm)

onelinerhub: [How do I format an SQLite database with version 3?](https://onelinerhub.com/sqlite/how-do-i-format-an-sqlite-database-with-version--)