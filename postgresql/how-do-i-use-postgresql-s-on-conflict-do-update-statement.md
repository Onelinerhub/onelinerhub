# How do I use PostgreSQL's ON CONFLICT DO UPDATE statement?
// plain

PostgreSQL's `ON CONFLICT DO UPDATE` statement allows you to specify an action to take when a conflict arises within a unique index or primary key. It is used to update existing records in the table when a conflict occurs.

## Example

```sql
INSERT INTO users (id, name, age)
VALUES (1, 'John', 20)
ON CONFLICT (id) DO UPDATE
SET name = 'John', age = 21;
```
This statement will insert the record (1, 'John', 20) into the users table, unless a record with id 1 already exists. In that case, the existing record will be updated with name 'John' and age 21.

The syntax of the `ON CONFLICT DO UPDATE` statement is as follows:
```sql
INSERT INTO table_name (column_list)
VALUES (value_list)
ON CONFLICT (conflict_target) DO UPDATE
SET set_clause
[ WHERE condition ]
```

- `table_name`: The name of the table to insert data into.
- `column_list`: A list of column names for the columns to be inserted.
- `value_list`: A list of values to be inserted into the specified columns.
- `conflict_target`: A list of columns that are used to determine whether a conflict exists.
- `set_clause`: A list of columns and values to be set when a conflict is detected.
- `WHERE condition`: An optional condition to filter which rows should be updated.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-insert.html).

onelinerhub: [How do I use PostgreSQL's ON CONFLICT DO UPDATE statement?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-on-conflict-do-update-statement)