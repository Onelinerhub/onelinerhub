# How do I format a SQLite database?
// plain

To format a SQLite database, you can use the SQLite command line shell. The command line shell provides a way to interact with the database and execute SQL commands.

For example, to create a table called 'users' with columns 'id', 'name', and 'email', you can use the following command:

```
sqlite> CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT);
```

This command will create a table called 'users' with the specified columns.

To insert data into the table, you can use the INSERT statement. For example, to insert a new user into the 'users' table, you can use the following command:

```
sqlite> INSERT INTO users (name, email) VALUES ('John', 'john@example.com');
```

This command will insert a new row into the 'users' table with the specified values.

To view the data in the table, you can use the SELECT statement. For example, to view all the users in the 'users' table, you can use the following command:

```
sqlite> SELECT * FROM users;
```

This command will return the following output:

```
id  name    email
1   John    john@example.com
```

To delete data from the table, you can use the DELETE statement. For example, to delete the user with the id of 1, you can use the following command:

```
sqlite> DELETE FROM users WHERE id = 1;
```

This command will delete the user with the id of 1 from the 'users' table.

## Helpful links
- [SQLite Command Line Shell](https://www.sqlite.org/cli.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I format a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-format-a-sqlite-database)