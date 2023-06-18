# How do I install and use SQLite on Ubuntu?
// plain

1. Install SQLite on Ubuntu by running the command `sudo apt-get install sqlite3` in a terminal window.
2. Create a new database by running the command `sqlite3 <database_name>` in the same terminal window.
3. Create a table in the database by running the command `CREATE TABLE <table_name> (<column_name> <data_type>)`.
4. Add records to the table using the command `INSERT INTO <table_name> VALUES (<value1>, <value2>, ...)`.
5. Retrieve records from the table using the command `SELECT * FROM <table_name>`.
6. Update existing records using the command `UPDATE <table_name> SET <column_name> = <new_value> WHERE <column_name> = <value>`.
7. Delete records from the table using the command `DELETE FROM <table_name> WHERE <column_name> = <value>`.

Example code block:
```
sqlite> CREATE TABLE users (name TEXT, age INTEGER);
sqlite> INSERT INTO users VALUES ('John', 25);
sqlite> SELECT * FROM users;

name        age
----------  ----------
John        25
```

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/)

onelinerhub: [How do I install and use SQLite on Ubuntu?](https://onelinerhub.com/sqlite/how-do-i-install-and-use-sqlite-on-ubuntu)