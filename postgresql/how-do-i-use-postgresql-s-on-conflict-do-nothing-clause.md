# How do I use PostgreSQL's ON CONFLICT DO NOTHING clause?
// plain

The ON CONFLICT DO NOTHING clause is a PostgreSQL extension to the SQL standard that allows you to specify an alternative action to take when a conflict arises in a unique index or primary key constraint. To use it, you must specify the target index or constraint and the action to take when a conflict occurs.

For example, consider a table `users` with a unique index on `email`:

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE
);
```

Now if you attempt to insert a duplicate email address, PostgreSQL will raise an error:

```sql
INSERT INTO users(email) VALUES('user@example.com');
INSERT INTO users(email) VALUES('user@example.com');
ERROR:  duplicate key value violates unique constraint "users_email_key"
```

To avoid this error, you can use the ON CONFLICT DO NOTHING clause:

```sql
INSERT INTO users(email) VALUES('user@example.com')
ON CONFLICT DO NOTHING;
```

This will cause PostgreSQL to ignore the conflicting row and not raise an error.

The ON CONFLICT DO NOTHING clause can also be used with a DO UPDATE clause to specify an alternative action to take when a conflict arises.

## Helpful links
- [PostgreSQL Documentation - ON CONFLICT Clause](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT)

onelinerhub: [How do I use PostgreSQL's ON CONFLICT DO NOTHING clause?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-on-conflict-do-nothing-clause)