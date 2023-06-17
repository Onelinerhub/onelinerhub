# How can I ensure a field in PostgreSQL is not null?
// plain

To ensure a field in PostgreSQL is not null, you can add a NOT NULL constraint when creating the table. For example:

```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
```

This will create a table named `users` with two columns, `id` and `username`, where the `username` column is not allowed to be null.

The parts of the code are as follows:
* `CREATE TABLE users` - Creates a table named `users`
* `id SERIAL PRIMARY KEY` - Creates an auto-incrementing `id` column as the primary key
* `username VARCHAR(50) NOT NULL` - Creates a `username` column of type `VARCHAR` with a maximum length of 50 characters, and adds a `NOT NULL` constraint, which ensures the column cannot be null.

## Helpful links
* [PostgreSQL Documentation - CREATE TABLE](https://www.postgresql.org/docs/9.6/sql-createtable.html)
* [PostgreSQL Documentation - NOT NULL Constraint](https://www.postgresql.org/docs/9.6/ddl-constraints.html#DDL-CONSTRAINTS-NOT-NULL)

onelinerhub: [How can I ensure a field in PostgreSQL is not null?](https://onelinerhub.com/postgresql/how-can-i-ensure-a-field-in-postgresql-is-not-null)