# How do I format a SQLite database?
// plain

SQLite is a powerful and easy-to-use database engine. To format a SQLite database, you must first define the schema of the database. This is done by creating tables that define the columns and data types of each field.

For example, the following code creates a table named `users` with three columns: `id`, `name`, and `age`:

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
```

Once the table is created, you can insert data into it with the `INSERT` statement. For example, the following code inserts a new user into the `users` table with an `id` of 1, a `name` of "John", and an `age` of 25:

```sql
INSERT INTO users (id, name, age) VALUES (1, 'John', 25);
```

You can also use the `UPDATE` statement to modify existing data in the table. For example, the following code updates the `name` of the user with an `id` of 1 to "Jane":

```sql
UPDATE users SET name = 'Jane' WHERE id = 1;
```

You can also delete data from the table with the `DELETE` statement. For example, the following code deletes the user with an `id` of 1:

```sql
DELETE FROM users WHERE id = 1;
```

Finally, you can query the database with the `SELECT` statement. For example, the following code selects all users from the `users` table:

```sql
SELECT * FROM users;
```

## Code Parts Explanation

* `CREATE TABLE`: Creates a new table in the database with the specified columns and data types.
* `INSERT`: Inserts a new row into the table with the specified values.
* `UPDATE`: Updates an existing row in the table with the specified values.
* `DELETE`: Deletes an existing row in the table.
* `SELECT`: Queries the table and returns the specified data.

## Relevant Links

* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [SQLite Documentation](https://www.sqlite.org/docs.html)

onelinerhub: [How do I format a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-format-a-sqlite-database-1687121062)