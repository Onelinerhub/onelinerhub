# How can I use PHP, Redis, and MySQL together in an example?
// plain

An example of using PHP, Redis, and MySQL together would be to store data in Redis and MySQL and then use PHP to query the data from both databases.

```php
<?php

// Connect to MySQL
$conn = new mysqli("localhost", "username", "password", "database");

// Connect to Redis
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Query data from MySQL
$sql = "SELECT * FROM users";
$result = $conn->query($sql);

// Query data from Redis
$user_data = $redis->get('user_data');

// Output
echo $result;
echo $user_data;

?>
```

This example code connects to both MySQL and Redis, queries data from each, and then outputs the result.

## Code explanation


1. Connect to MySQL: Establishes a connection to MySQL using the `mysqli` class.
2. Connect to Redis: Establishes a connection to Redis using the `Redis` class.
3. Query data from MySQL: Uses the `query` method to query data from MySQL.
4. Query data from Redis: Uses the `get` method to query data from Redis.
5. Output: Outputs the result of the MySQL and Redis queries.

## Helpful links
- [MySQL PHP Manual](https://www.php.net/manual/en/book.mysqli.php)
- [Redis PHP Manual](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How can I use PHP, Redis, and MySQL together in an example?](https://onelinerhub.com/predis/how-can-i-use-php--redis--and-mysql-together-in-an-example)