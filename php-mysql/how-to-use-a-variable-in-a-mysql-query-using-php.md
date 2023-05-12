# How to use a variable in a MySQL query using PHP?
// plain

Using a variable in a MySQL query using PHP is a common task. The following example code block shows how to use a variable in a MySQL query using PHP:

```
$variable = "example";
$query = "SELECT * FROM table WHERE column = '$variable'";
$result = mysqli_query($connection, $query);
```

The output of the example code is a MySQL query that looks like this:

```
SELECT * FROM table WHERE column = 'example'
```

## Code explanation


1. `$variable = "example";` - This line of code declares a variable called `$variable` and assigns it the value of "example".
2. `$query = "SELECT * FROM table WHERE column = '$variable'";` - This line of code declares a variable called `$query` and assigns it a MySQL query that uses the `$variable` variable.
3. `$result = mysqli_query($connection, $query);` - This line of code executes the MySQL query and stores the result in the `$result` variable.

## Helpful links

- [PHP MySQLi Introduction](https://www.w3schools.com/php/php_mysqli_intro.asp)
- [PHP MySQLi Query](https://www.w3schools.com/php/php_mysqli_query.asp)

onelinerhub: [How to use a variable in a MySQL query using PHP?](https://onelinerhub.com/php-mysql/how-to-use-a-variable-in-a-mysql-query-using-php)