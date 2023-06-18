# clause

How can I use the SQLite HAVING clause to filter query results?
// plain

The SQLite `HAVING` clause is used to filter query results based on aggregate functions. It is used in conjunction with the `GROUP BY` clause to filter the groups of rows returned by the `GROUP BY` clause.

For example, the following code block will return the names of all employees who have a salary greater than $50,000:
```
SELECT name
FROM employees
GROUP BY name
HAVING SUM(salary) > 50000;
```

The code block consists of four parts:

1. `SELECT name` - This clause specifies which columns to return in the query result.
2. `FROM employees` - This clause specifies the table from which the data will be retrieved.
3. `GROUP BY name` - This clause groups the rows of the result set by the specified column or columns.
4. `HAVING SUM(salary) > 50000` - This clause filters the groups of rows returned by the `GROUP BY` clause based on the aggregate function used. In this case, the `SUM` function is used to sum the salaries of each employee and the result is filtered to only include groups with a total salary greater than $50,000.

For more information, see the following links:

- [SQLite Documentation - HAVING Clause](https://www.sqlite.org/lang_select.html#havingclause)
- [W3Schools - SQLite HAVING Clause](https://www.w3schools.com/sql/sql_having.asp)

onelinerhub: [clause

How can I use the SQLite HAVING clause to filter query results?](https://onelinerhub.com/sqlite/clause--how-can-i-use-the-sqlite-having-clause-to-filter-query-results)