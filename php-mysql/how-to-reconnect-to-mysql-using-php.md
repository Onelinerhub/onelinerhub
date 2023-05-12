# How to reconnect to MySQL using PHP?
// plain

To reconnect to MySQL using PHP, you can use the `mysqli_connect()` function. This function takes in four parameters: the hostname, username, password, and database name.

```php
$conn = mysqli_connect("localhost", "username", "password", "database");
```

The code above will establish a connection to the MySQL server. If the connection is successful, it will return a `mysqli` object.

## Code explanation


1. `mysqli_connect()` - This is the function used to establish a connection to the MySQL server.
2. `localhost` - This is the hostname of the MySQL server.
3. `username` - This is the username used to authenticate the connection.
4. `password` - This is the password used to authenticate the connection.
5. `database` - This is the name of the database to connect to.

## Output example


```
mysqli Object
(
    [affected_rows] => 0
    [client_info] => mysqlnd 5.0.12-dev - 20150407 - $Id: b5c5906d452ec590732a93b051f3827e02749b83 $
    [client_version] => 50012
    [connect_errno] => 0
    [connect_error] =>
    [errno] => 0
    [error] =>
    [error_list] => Array
        (
        )

    [field_count] => 0
    [host_info] => Localhost via UNIX socket
    [info] =>
    [insert_id] => 0
    [server_info] => 5.7.25-0ubuntu0.18.04.2
    [server_version] => 50725
    [stat] => Uptime: 845  Threads: 1  Questions: 4  Slow queries: 0  Opens: 103  Flush tables: 1  Open tables: 98  Queries per second avg: 0.005
    [sqlstate] => 00000
    [protocol_version] => 10
    [thread_id] => 8
    [warning_count] => 0
)
```

## Helpful links

- [PHP mysqli_connect() Function](https://www.w3schools.com/php/func_mysqli_connect.asp)

onelinerhub: [How to reconnect to MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-reconnect-to-mysql-using-php)