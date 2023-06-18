# How can I use the "not equal" operator in SQLite?
// plain

The "not equal" operator in SQLite is the `!=` operator. This operator is used to compare two values and determine if they are not equal to each other.

For example, the following code block will select all records from the table `people` where the column `age` is not equal to `25`:

```
SELECT * FROM people WHERE age != 25;
```

The output of this code will be all records from the table `people` where the value of the `age` column is not equal to `25`.

The `!=` operator can also be used with other comparison operators, such as `>` and `<`, to create more complex conditions. For example, the following code block will select all records from the table `people` where the column `age` is not greater than `25`:

```
SELECT * FROM people WHERE age != > 25;
```

The output of this code will be all records from the table `people` where the value of the `age` column is not greater than `25`.

The parts of the code are:
- `SELECT *`: This is the command to select all columns from the table.
- `FROM people`: This is the table from which data should be selected.
- `WHERE age != 25`: This is the condition that must be met for a record to be selected.

## Helpful links
- [SQLite Query Language](https://www.sqlite.org/lang.html)
- [SQLite Operators](https://www.tutorialspoint.com/sqlite/sqlite_operators.htm)

onelinerhub: [How can I use the "not equal" operator in SQLite?](https://onelinerhub.com/sqlite/how-can-i-use-the--not-equal--operator-in-sqlite)