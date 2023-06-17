# How can I use PostgreSQL types to create a database?
// plain

PostgreSQL provides a wide range of data types that can be used to create a database. The following example code creates a table called "users" with three columns:

```
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL
);
```

The `id` column is of type `SERIAL`, which is an auto-incrementing integer. The `name` and `email` columns are of type `VARCHAR`, which is a variable-length character type.

The following query inserts a row into the `users` table:

```
INSERT INTO users (name, email)
VALUES ('John Doe', 'john@example.com');
```

The output of this query is:

```
INSERT 0 1
```

The following query retrieves the newly inserted row:

```
SELECT * FROM users;
```

The output of this query is:

```
 id |  name  |      email
----+--------+---------------------
  1 | John Doe | john@example.com
(1 row)
```

## Code explanation


- `CREATE TABLE` - used to create a table in the database
- `SERIAL` - an auto-incrementing integer type
- `VARCHAR` - a variable-length character type
- `INSERT INTO` - used to insert a row into a table
- `SELECT` - used to retrieve data from a table

## Helpful links

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)

onelinerhub: [How can I use PostgreSQL types to create a database?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-types-to-create-a-database)