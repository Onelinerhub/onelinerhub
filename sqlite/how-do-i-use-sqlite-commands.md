# How do I use SQLite commands?
// plain

SQLite is a popular, open-source, lightweight relational database management system (RDBMS). It is used to store data in a structured format and is commonly used with web applications and mobile applications.

To use SQLite commands, you need to open the SQLite command line interface (CLI). You can do this by running the following command:

```
sqlite3 database_name.db
```

Once you are in the CLI, you can start executing SQLite commands. For example, to create a new table, you can use the `CREATE TABLE` command:

```
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);
```

This command will create a table called `users` with three columns: `id`, `name`, and `age`.

To insert data into the table, you can use the `INSERT INTO` command:

```
INSERT INTO users (name, age)
VALUES('John', 30);
```

This command will insert a row into the `users` table with the name `John` and the age `30`.

Other SQLite commands include `SELECT`, `UPDATE`, `DELETE`, `ALTER TABLE`, and `DROP TABLE`. For more information on how to use SQLite commands, you can refer to the [SQLite Documentation](https://www.sqlite.org/docs.html).

onelinerhub: [How do I use SQLite commands?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-commands)