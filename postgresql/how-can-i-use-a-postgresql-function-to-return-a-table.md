# How can I use a PostgreSQL function to return a table?
// plain

You can use the `RETURNS TABLE` syntax in PostgreSQL to return a table. This syntax is used to define a function that returns a set of rows, which can be used as a table.

For example:
```sql
CREATE FUNCTION get_employees()
  RETURNS TABLE(id INTEGER, name TEXT)
AS $$
  SELECT id, name FROM employees;
$$ LANGUAGE SQL;
```

This function will return a table with two columns `id` and `name`, which can be used as a table.

To use the table, you can call the function in a `SELECT` statement:
```sql
SELECT * FROM get_employees();
```

This will return the following output:
```
 id |  name
----+---------
  1 | John
  2 | Jane
  3 | Bob
(3 rows)
```

The `RETURNS TABLE` syntax in PostgreSQL can be used to define a function that returns a set of rows, which can be used as a table. The table can then be used in a `SELECT` statement to return the data.

#### List of code parts with detailed explanation
- `CREATE FUNCTION get_employees()` - This statement creates a function named `get_employees`.
- `RETURNS TABLE(id INTEGER, name TEXT)` - This statement defines the function to return a table with two columns `id` and `name`.
- `SELECT id, name FROM employees;` - This statement is used to retrieve the data from the `employees` table.
- `SELECT * FROM get_employees();` - This statement is used to call the function and return the data.

#### List of relevant links
- [PostgreSQL Documentation - RETURNS TABLE](https://www.postgresql.org/docs/current/sql-createrule.html#SQL-CREATEFUNCTION-RETURNING-TABLE)

onelinerhub: [How can I use a PostgreSQL function to return a table?](https://onelinerhub.com/postgresql/how-can-i-use-a-postgresql-function-to-return-a-table)