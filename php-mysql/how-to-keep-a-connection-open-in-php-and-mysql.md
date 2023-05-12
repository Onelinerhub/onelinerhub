# How to keep a connection open in PHP and MySQL?
// plain

To keep a connection open in PHP and MySQL, you can use the `mysqli_connect()` function. This function takes in the database host, username, password, and database name as parameters and returns a connection object.

```php
$conn = mysqli_connect("localhost", "username", "password", "database_name");
```

The code above will create a connection object `$conn` which can be used to execute queries on the database. To keep the connection open, you can use the `mysqli_ping()` function. This function takes in the connection object as a parameter and returns `true` if the connection is still alive.

```php
if (mysqli_ping($conn)) {
    echo "Connection is still alive";
}
```

The code above will check if the connection is still alive and print out a message if it is.

Parts of the code:

- `mysqli_connect()`: This function takes in the database host, username, password, and database name as parameters and returns a connection object.
- `mysqli_ping()`: This function takes in the connection object as a parameter and returns `true` if the connection is still alive.
- `if` statement: This statement checks if the connection is still alive and prints out a message if it is.

## Helpful links

- [PHP mysqli_connect() Function](https://www.w3schools.com/php/func_mysqli_connect.asp)
- [PHP mysqli_ping() Function](https://www.w3schools.com/php/func_mysqli_ping.asp)

onelinerhub: [How to keep a connection open in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-keep-a-connection-open-in-php-and-mysql)