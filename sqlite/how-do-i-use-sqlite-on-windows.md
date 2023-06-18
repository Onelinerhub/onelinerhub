# How do I use SQLite on Windows?
// plain

SQLite is a lightweight database system that can be used on Windows. It is a self-contained, serverless, zero-configuration, transactional SQL database engine. The following steps explain how to use SQLite on Windows:

1. Download and install the [SQLite command-line shell](https://www.sqlite.org/download.html) for your platform.

2. Create a new database file with the `sqlite3` command:

```
sqlite3 test.db
```

This will create a new database file called `test.db` in the current directory.

3. Create a table with the `CREATE TABLE` command:

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
```

4. Insert some data with the `INSERT INTO` command:

```
INSERT INTO users (name, age) VALUES ('John', 25);
INSERT INTO users (name, age) VALUES ('Jane', 32);
```

5. Query the data with the `SELECT` command:

```
SELECT * FROM users;
```

This will output the following:

```
id          name        age
----------  ----------  ----------
1           John        25
2           Jane        32
```

6. Finally, close the database with the `.exit` command:

```
.exit
```

This will save the changes and close the database.

onelinerhub: [How do I use SQLite on Windows?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-on-windows)