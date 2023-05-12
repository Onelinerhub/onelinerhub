# How to insert a null value in MySQL using PHP?
// plain

To insert a null value in MySQL using PHP, you can use the `NULL` keyword. For example:

```
$sql = "INSERT INTO table_name (column_name) VALUES (NULL)";
```

This will insert a `NULL` value into the `column_name` column of the `table_name` table.

## Code explanation


- `$sql`: This is a variable that holds the SQL query.
- `INSERT INTO`: This is the SQL command used to insert data into a table.
- `table_name`: This is the name of the table where the data will be inserted.
- `column_name`: This is the name of the column where the data will be inserted.
- `VALUES`: This is the keyword used to specify the values to be inserted.
- `NULL`: This is the keyword used to specify a null value.

## Helpful links

- [MySQL INSERT Statement](https://dev.mysql.com/doc/refman/8.0/en/insert.html)
- [PHP NULL](https://www.php.net/manual/en/language.types.null.php)

onelinerhub: [How to insert a null value in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-insert-a-null-value-in-mysql-using-php)