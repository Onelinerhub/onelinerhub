# How do I use the PostgreSQL DISTINCT keyword?
// plain

The PostgreSQL DISTINCT keyword is used to select only distinct (unique) values from a column. It eliminates duplicate values from the result set of a query.

For example, if we have a table of users with the following data:

| ID | Name |
|----|------|
| 1  | John |
| 2  | John |
| 3  | Mary |

We can use the DISTINCT keyword to select only the unique values from the Name column:

```sql
SELECT DISTINCT Name FROM users;
```

This would return the following output:

```
John
Mary
```

The parts of the statement are:

- `SELECT`: The start of the statement, which indicates that we are selecting data from a table.
- `DISTINCT`: This keyword is used to select only unique values from the specified column.
- `Name`: The name of the column that we are selecting from.
- `FROM`: This keyword indicates the table that we are selecting from.
- `users`: The name of the table that we are selecting from.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/9.1/queries-select.html#QUERIES-DISTINCT).

onelinerhub: [How do I use the PostgreSQL DISTINCT keyword?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-distinct-keyword)