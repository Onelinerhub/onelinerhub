# How can I use the "order by" statement in Python to sort data in a MySQL database?
// plain

The `ORDER BY` statement in Python can be used to sort data in a MySQL database. The syntax for using `ORDER BY` is as follows: `SELECT * FROM table_name ORDER BY column_name [ASC|DESC];`.

The `ORDER BY` statement is used to sort the results of a `SELECT` statement in either ascending or descending order. The `ASC` keyword is used to sort the results in ascending order, while the `DESC` keyword is used to sort the results in descending order.

For example, the following code block can be used to sort a table of student grades in descending order:

```
SELECT * FROM student_grades ORDER BY grade DESC;
```

The output of the above code would be a list of student grades sorted in descending order.

## Code explanation


- `SELECT * FROM`: This part of the code tells the database to select all data from the table.
- `table_name`: This is the name of the table from which the data is to be selected.
- `ORDER BY`: This part of the code tells the database to sort the results of the `SELECT` statement.
- `column_name`: This is the name of the column by which the data is to be sorted.
- `[ASC|DESC]`: This part of the code tells the database to sort the results in either ascending or descending order.

## Helpful links
- [MySQL ORDER BY Clause](https://www.w3schools.com/sql/sql_orderby.asp)
- [MySQL SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)

onelinerhub: [How can I use the "order by" statement in Python to sort data in a MySQL database?](https://onelinerhub.com/python-mysql/how-can-i-use-the--order-by--statement-in-python-to-sort-data-in-a-mysql-database)