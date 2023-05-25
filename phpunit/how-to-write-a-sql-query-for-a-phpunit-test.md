# How to write a SQL query for a PHPUnit test?
// plain

Writing a SQL query for a PHPUnit test is a great way to ensure that your code is working as expected. The following example code block shows a simple SQL query that can be used in a PHPUnit test:
```
$query = "SELECT * FROM users WHERE id = :id";
```
This query will select all the data from the users table where the id matches the value of the :id parameter.

## Code explanation


- `SELECT *`: This part of the query tells the database to select all the columns from the users table.

- `FROM users`: This part of the query tells the database to select the data from the users table.

- `WHERE id = :id`: This part of the query tells the database to only select the data from the users table where the id matches the value of the :id parameter.

## Helpful links

- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

onelinerhub: [How to write a SQL query for a PHPUnit test?](https://onelinerhub.com/phpunit/how-to-write-a-sql-query-for-a-phpunit-test)