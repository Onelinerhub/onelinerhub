# statement

How do I use the SQLite BETWEEN statement to compare values?
// plain

The SQLite BETWEEN statement is used to compare values within a range. It is used to filter a result set based on a specified range of values. The syntax for the BETWEEN statement is as follows:

```
SELECT * FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

The BETWEEN statement will return all rows where the column_name is between value1 and value2. The values can be strings, numbers, dates, or even subqueries.

For example, the following query will return all rows from the table "Employees" where the salary is between $50,000 and $60,000:

```
SELECT * FROM Employees
WHERE salary BETWEEN 50000 AND 60000;
```

The output of this query would be all rows from the table "Employees" where the salary is between $50,000 and $60,000.

The parts of the BETWEEN statement are:

* SELECT - specifies which columns to return
* FROM - specifies the table to query
* WHERE - specifies the conditions for the query
* BETWEEN - compares values within a range
* value1 and value2 - the range of values to compare

## Helpful links

* [SQLite Documentation](https://www.sqlite.org/lang_expr.html#between)
* [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-between/)

onelinerhub: [statement

How do I use the SQLite BETWEEN statement to compare values?](https://onelinerhub.com/sqlite/statement--how-do-i-use-the-sqlite-between-statement-to-compare-values)