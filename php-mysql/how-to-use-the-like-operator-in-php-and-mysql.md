# How to use the LIKE operator in PHP and MySQL?
// plain

The `LIKE` operator is used in PHP and MySQL to match a pattern in a string. It is used in `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

## Example code

```
SELECT * FROM table_name WHERE column_name LIKE '%pattern%';
```

## Output example

```
+----+------------+
| id | column_name|
+----+------------+
|  1 | abc        |
|  2 | abcd       |
|  3 | abcde      |
+----+------------+
```

## Code explanation

- `SELECT`: used to select data from a database
- `*`: used to select all columns from a table
- `FROM`: used to specify the table from which to select data
- `WHERE`: used to specify a condition
- `LIKE`: used to match a pattern in a string
- `'%pattern%'`: used to specify the pattern to match

## Helpful links
- [MySQL LIKE Clause](https://www.w3schools.com/sql/sql_like.asp)
- [MySQL SELECT Statement](https://www.w3schools.com/sql/sql_select.asp)

onelinerhub: [How to use the LIKE operator in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-use-the-like-operator-in-php-and-mysql)