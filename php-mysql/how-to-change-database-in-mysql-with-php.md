# How to change database in MySQL with PHP?
// plain

To change the database in MySQL with PHP, you can use the `mysqli_select_db()` function. This function takes two parameters, the first being the MySQLi connection object and the second being the name of the database you want to select.

```php
$conn = mysqli_connect("localhost", "username", "password");
$db_selected = mysqli_select_db($conn, "database_name");
```

The code above will connect to the MySQL server and select the database with the name `database_name`.

The parts of the code are:

1. `$conn`: This is the MySQLi connection object.
2. `mysqli_connect()`: This is the function used to connect to the MySQL server. It takes three parameters, the first being the hostname, the second being the username and the third being the password.
3. `mysqli_select_db()`: This is the function used to select the database. It takes two parameters, the first being the MySQLi connection object and the second being the name of the database you want to select.

## Helpful links

- [MySQLi: Selecting a Database](https://www.w3schools.com/php/func_mysqli_select_db.asp)

onelinerhub: [How to change database in MySQL with PHP?](https://onelinerhub.com/php-mysql/how-to-change-database-in-mysql-with-php)