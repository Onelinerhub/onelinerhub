# How do I create a database using SQLite?
// plain

Creating a database using SQLite is easy and requires only a few steps.

1. Download and install SQLite: The first step is to download and install SQLite. You can find the download page [here](https://www.sqlite.org/download.html).

2. Create a database file: After installation, you can create a database file using the `sqlite3` command. For example:

```
sqlite3 test.db
```

This will create a database file called `test.db`.

3. Create tables: Once the database file is created, you can create tables inside it. For example:

```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```

This will create a table called `users` with three columns: `id`, `name`, and `email`.

4. Insert data into the tables: After creating the tables, you can insert data into them. For example:

```
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
```

This will insert a new row into the `users` table with the name `John Doe` and email `john@example.com`.

5. Query the data: Finally, you can query the data in the database using SQL statements. For example:

```
SELECT * FROM users;
```

This will return all rows in the `users` table.

By following these steps, you can create a database using SQLite.

onelinerhub: [How do I create a database using SQLite?](https://onelinerhub.com/sqlite/how-do-i-create-a-database-using-sqlite)