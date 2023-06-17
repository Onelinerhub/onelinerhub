# How can I use the WHERE IN clause in Python to query a MySQL database?
// plain

The WHERE IN clause can be used in Python to query a MySQL database. It is used to filter a result set based on a list of values. The syntax for the WHERE IN clause is as follows:

```
SELECT * FROM table_name WHERE column_name IN (value1, value2, ...);
```

For example, to select all rows from a table named "students" where "name" is "John" or "Mary":

```
SELECT * FROM students WHERE name IN ('John', 'Mary');
```

The output of the query would be all rows from the "students" table where the "name" column contains either "John" or "Mary".

## Code explanation


* `SELECT` - specifies the columns from the table to be returned
* `*` - specifies that all columns should be returned
* `FROM` - specifies the table name
* `WHERE` - specifies the filter condition for the query
* `IN` - specifies the list of values for the filter condition
* `(value1, value2, ...)` - specifies the list of values to be used in the filter condition

## Helpful links

* [MySQL WHERE IN Clause](https://www.w3schools.com/sql/sql_where_in.asp)
* [MySQL SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)

onelinerhub: [How can I use the WHERE IN clause in Python to query a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-the-where-in-clause-in-python-to-query-a-mysql-database)