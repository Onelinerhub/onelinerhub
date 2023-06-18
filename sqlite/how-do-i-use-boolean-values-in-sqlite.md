# How do I use boolean values in SQLite?
// plain

Boolean values can be used in SQLite to represent true or false values. Boolean values are represented in SQLite using the keywords `TRUE` and `FALSE`.

For example, the following code block can be used to select all records from the `users` table where the `active` column is set to `TRUE`:

```sql
SELECT * FROM users WHERE active = TRUE;
```

This query will return all records from the `users` table where the `active` column is set to `TRUE`.

The following code block can be used to update the `active` column of the `users` table:

```sql
UPDATE users SET active = FALSE WHERE id = 1;
```

This query will set the `active` column of the user with `id` 1 to `FALSE`.

The following code block can be used to insert a new record into the `users` table:

```sql
INSERT INTO users (name, active) VALUES ('John', TRUE);
```

This query will add a new record to the `users` table with a `name` of `John` and an `active` value of `TRUE`.

## Helpful links

- [Boolean Datatype](https://www.sqlite.org/datatype3.html#boolean_datatype)
- [Data Types In SQLite Version 3](https://www.sqlite.org/datatype3.html)

onelinerhub: [How do I use boolean values in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-boolean-values-in-sqlite)