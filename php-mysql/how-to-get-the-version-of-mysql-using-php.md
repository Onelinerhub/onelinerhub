# How to get the version of MySQL using PHP?
// plain

You can get the version of MySQL using PHP by using the `mysqli_get_server_info()` function. This function returns a string containing the version of the MySQL server.

## Example code

```
<?php
$conn = mysqli_connect("localhost", "username", "password", "database");
echo mysqli_get_server_info($conn);
?>
```

## Output example

```
5.7.25
```

## Code explanation

- `mysqli_get_server_info()`: This is the function used to get the version of MySQL.
- `$conn`: This is the connection variable used to connect to the MySQL server.
- `mysqli_connect()`: This is the function used to connect to the MySQL server.

## Helpful links
- [mysqli_get_server_info()](https://www.php.net/manual/en/mysqli.get-server-info.php)
- [mysqli_connect()](https://www.php.net/manual/en/mysqli.connect.php)

onelinerhub: [How to get the version of MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-get-the-version-of-mysql-using-php)