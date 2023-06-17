# How can I join two tables in MySQL using Python?
// plain

Joining two tables in MySQL using Python can be done using the `JOIN` command in a `SELECT` statement. The syntax for joining two tables is as follows:

```
SELECT table1.column1, table2.column2
FROM table1
JOIN table2
ON table1.column1 = table2.column2;
```

This statement will return all rows from both tables where the `column1` of `table1` matches the `column2` of `table2`.

For example, if `table1` is a table of student IDs and `table2` is a table of student grades, the following statement can be used to join the two tables:

```
SELECT table1.student_id, table2.grade
FROM table1
JOIN table2
ON table1.student_id = table2.student_id;

## Output example

student_id	grade
1	A
2	B
3	C
4	D
```

## Code explanation

- `SELECT table1.column1, table2.column2`: This part of the statement is used to specify which columns should be returned by the statement. In this example, `column1` from `table1` and `column2` from `table2` are specified.
- `FROM table1`: This part of the statement is used to specify which table should be used as the primary source of data. In this example, `table1` is specified.
- `JOIN table2`: This part of the statement is used to specify which table should be joined to the primary table. In this example, `table2` is specified.
- `ON table1.column1 = table2.column2`: This part of the statement is used to specify the condition that should be used to join the two tables. In this example, `column1` of `table1` is compared to `column2` of `table2`.

## Helpful links
- [MySQL JOIN](https://dev.mysql.com/doc/refman/8.0/en/join.html)
- [MySQL SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html)

onelinerhub: [How can I join two tables in MySQL using Python?](https://onelinerhub.com/python-mysql/how-can-i-join-two-tables-in-mysql-using-python)