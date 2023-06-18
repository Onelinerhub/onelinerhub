# How can I install and use SQLite on a Linux system?
// plain

To install and use SQLite on a Linux system, you can use the following steps:

1. Install the SQLite package using the package manager for your Linux distribution. For example, for Ubuntu, you can use the following command:

```
sudo apt-get install sqlite3
```

2. Create a new database file using the `sqlite3` command. For example, to create a database file named `mydatabase.db` in the current directory, you can use the following command:

```
sqlite3 mydatabase.db
```

3. Create tables and insert data into the database using SQL commands. For example, to create a table named `users` with two columns, `name` and `age`, you can use the following command:

```
CREATE TABLE users (name TEXT, age INTEGER);
```

4. To insert data into the table, you can use the `INSERT` command. For example, to insert a user named `John` with an age of `25`, you can use the following command:

```
INSERT INTO users VALUES('John', 25);
```

5. To query the database, you can use the `SELECT` command. For example, to select all users from the `users` table, you can use the following command:

```
SELECT * FROM users;
```

This should return the following output:

```
name        age
----------  ----------
John        25
```

For more information, you can refer to the [SQLite documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How can I install and use SQLite on a Linux system?](https://onelinerhub.com/sqlite/how-can-i-install-and-use-sqlite-on-a-linux-system)