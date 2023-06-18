# How do I use the SQLite SELECT statement?
// plain

The SQLite SELECT statement is used to query the database and retrieve specific data from one or more tables. It is the most commonly used SQL statement.

The basic syntax of the SELECT statement is as follows:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Where `column1`, `column2`, etc. are the columns to be selected from the table `table_name` and `condition` is the condition which must be met for a row to be included in the result set.

For example, to select all the records from the table `employees` where the `salary` is greater than 50000:

```
SELECT *
FROM employees
WHERE salary > 50000;
```

This statement will return all columns from the `employees` table where the `salary` is greater than 50000.

The following list explains the parts of the SELECT statement:

- `SELECT`: This keyword is used to indicate that the statement is a SELECT statement.
- `column1, column2, ...`: These are the names of the columns to be selected from the table.
- `FROM`: This keyword is used to indicate the table from which data should be selected.
- `table_name`: This is the name of the table from which data should be selected.
- `WHERE`: This keyword is used to indicate the condition which must be met for a row to be included in the result set.
- `condition`: This is the condition which must be met for a row to be included in the result set.

For more information on the SQLite SELECT statement, see the [SQLite documentation](https://www.sqlite.org/lang_select.html).

onelinerhub: [How do I use the SQLite SELECT statement?](https://onelinerhub.com/sqlite/how-do-i-use-the-sqlite-select-statement)