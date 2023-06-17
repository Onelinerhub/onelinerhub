# How do I insert data into a PostgreSQL table?
// plain

Inserting data into a PostgreSQL table is a fairly straightforward process. The following example demonstrates how to do this:

```
INSERT INTO my_table (column1, column2, column3)
VALUES (value1, value2, value3);
```

This example inserts a row into the table `my_table` with the values `value1`, `value2`, and `value3` in the columns `column1`, `column2`, and `column3`, respectively.

The parts of the command are as follows:

* `INSERT INTO` - This is the command to insert data into a table.
* `my_table` - This is the name of the table into which the data will be inserted.
* `(column1, column2, column3)` - This is a list of the columns in the table into which the data will be inserted.
* `VALUES` - This is the keyword that indicates the values that will be inserted into the table.
* `(value1, value2, value3)` - This is a list of the values that will be inserted into the corresponding columns.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-insert.html).

onelinerhub: [How do I insert data into a PostgreSQL table?](https://onelinerhub.com/postgresql/how-do-i-insert-data-into-a-postgresql-table)