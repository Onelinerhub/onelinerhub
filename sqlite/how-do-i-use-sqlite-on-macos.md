# How do I use SQLite on MacOS?
// plain

SQLite is a lightweight and easy-to-use database system that can be used on MacOS. To use it, you need to install the SQLite3 command line interface, which can be done using Homebrew.

```
brew install sqlite3
```

Once installed, you can access the database from the command line interface. To create a new database, you can use the following command:

```
sqlite3 my_database.db
```

This will create a new database file called `my_database.db`. To create a new table in the database, you can use the `CREATE TABLE` command. For example, to create a table called `users` with two columns `name` and `age`, you can use the following command:

```
CREATE TABLE users (name TEXT, age INTEGER);
```

You can then insert data into the table using the `INSERT INTO` command. For example, to insert a user called `John` with an age of `30`, you can use the following command:

```
INSERT INTO users VALUES ('John', 30);
```

You can then query the table using the `SELECT` command. For example, to get all users with an age of 30, you can use the following command:

```
SELECT * FROM users WHERE age = 30;
```

This will output all users with an age of 30, for example:

```
John|30
```

## Helpful links
- [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-tutorial/)
- [SQLite Commands](https://www.sqlite.org/cli.html)

onelinerhub: [How do I use SQLite on MacOS?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-on-macos)