# clause

How do I use a WHERE clause in SQLite?
// plain

A WHERE clause is used in SQLite to filter the results of a query. It is used to specify a condition that must be met for the results to be returned.

For example, the following query will return all rows from the table 'users' where the 'status' column is equal to 'active':

```
SELECT * FROM users WHERE status = 'active';
```

The output of this query will be all the rows from the table 'users' where the 'status' column has the value 'active'.

The syntax of a WHERE clause is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

## Code explanation


- `SELECT`: This is used to specify the columns to be returned by the query.
- `FROM`: This is used to specify the table from which the data should be retrieved.
- `WHERE`: This is used to specify the condition that must be met for the results to be returned.
- `condition`: This is the condition that must be met for the results to be returned. It can be a comparison operator, such as `=`, `<`, or `>`, or a logical operator, such as `AND` or `OR`.

For more information, please refer to the [SQLite documentation](https://www.sqlite.org/lang_select.html).

onelinerhub: [clause

How do I use a WHERE clause in SQLite?](https://onelinerhub.com/sqlite/clause--how-do-i-use-a-where-clause-in-sqlite)