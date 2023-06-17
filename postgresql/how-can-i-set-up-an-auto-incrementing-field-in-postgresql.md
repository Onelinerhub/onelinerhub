# How can I set up an auto-incrementing field in PostgreSQL?
// plain

In PostgreSQL, you can set up an auto-incrementing field by using a sequence object. To do this, you can create a sequence object that generates a unique integer each time it is called.

For example, the following code creates a sequence object called `users_id_seq` that starts at 1 and increments by 1 each time it is called:

```sql
CREATE SEQUENCE users_id_seq
  START WITH 1
  INCREMENT BY 1;
```

Then, you can use the `nextval()` function to assign a unique value to a field in a table. For example, the following code adds a `user_id` field to the `users` table and assigns it a unique value from the `users_id_seq` sequence:

```sql
ALTER TABLE users
  ADD user_id INTEGER NOT NULL DEFAULT nextval('users_id_seq');
```

Finally, you can use the `currval()` function to get the last value assigned by the sequence object. For example, the following code retrieves the last value assigned by the `users_id_seq` sequence:

```sql
SELECT currval('users_id_seq');
```

## Output example


```
currval
--------
      1
(1 row)
```

## Code explanation


- `CREATE SEQUENCE`: creates a sequence object
- `START WITH`: sets the starting value for the sequence
- `INCREMENT BY`: sets the increment step for the sequence
- `nextval()`: assigns a unique value from the sequence to a field in a table
- `currval()`: retrieves the last value assigned by the sequence

## Helpful links

- [PostgreSQL Documentation - Sequences](https://www.postgresql.org/docs/current/sql-createsequence.html)

onelinerhub: [How can I set up an auto-incrementing field in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-set-up-an-auto-incrementing-field-in-postgresql)