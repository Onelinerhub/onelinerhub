# How to join tables with PHP and MySQL?
// plain

Joining tables in PHP and MySQL is a common task when working with databases. It can be done using the `JOIN` keyword in an SQL query.

```
SELECT * FROM table1
JOIN table2
ON table1.id = table2.id
```

This example query will join the two tables `table1` and `table2` on the `id` column. The output of this query will be all the columns from both tables.

- `SELECT *`: This part of the query specifies which columns to select from the tables. In this case, `*` is used to select all columns.
- `FROM table1`: This part of the query specifies which table to select from. In this case, `table1` is used.
- `JOIN table2`: This part of the query specifies which table to join with. In this case, `table2` is used.
- `ON table1.id = table2.id`: This part of the query specifies which columns to join on. In this case, the `id` column from both tables is used.

## Helpful links
- [MySQL JOIN Syntax](https://dev.mysql.com/doc/refman/8.0/en/join.html)
- [PHP MySQLi Prepared Statements](https://www.w3schools.com/php/php_mysql_prepared_statements.asp)

onelinerhub: [How to join tables with PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-join-tables-with-php-and-mysql)