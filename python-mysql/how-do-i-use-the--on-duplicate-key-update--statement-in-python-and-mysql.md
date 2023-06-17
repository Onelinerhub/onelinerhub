# How do I use the "on duplicate key update" statement in Python and MySQL?
// plain

The `on duplicate key update` statement in Python and MySQL is used to update existing records in a table when a duplicate key is inserted. It is useful for preventing duplicate records in a database table. The syntax is as follows:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...)
ON DUPLICATE KEY UPDATE column1 = value1, column2 = value2, column3 = value3, ...;
```

For example, if we have a table called `students` with a primary key of `student_id` and we want to update the `name` and `age` columns when a duplicate `student_id` is inserted, we could use the following query:

```
INSERT INTO students (student_id, name, age)
VALUES (2, 'John', 25)
ON DUPLICATE KEY UPDATE name = 'John', age = 25;
```

The parts of this code are:

1. `INSERT INTO students` - This statement is used to insert data into the `students` table.
2. `(student_id, name, age)` - This specifies the columns that the data will be inserted into.
3. `VALUES (2, 'John', 25)` - This specifies the values to be inserted into the specified columns.
4. `ON DUPLICATE KEY UPDATE` - This statement is used to update existing records in the table when a duplicate key is inserted.
5. `name = 'John', age = 25;` - This specifies the columns and values to be updated when a duplicate key is inserted.

## Helpful links

- [MySQL Documentation - INSERT ON DUPLICATE KEY UPDATE](https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html)
- [MySQL Tutorial - INSERT ON DUPLICATE KEY UPDATE](https://www.mysqltutorial.org/mysql-insert-or-update-on-duplicate-key-update/)

onelinerhub: [How do I use the "on duplicate key update" statement in Python and MySQL?](https://onelinerhub.com/python-mysql/how-do-i-use-the--on-duplicate-key-update--statement-in-python-and-mysql)