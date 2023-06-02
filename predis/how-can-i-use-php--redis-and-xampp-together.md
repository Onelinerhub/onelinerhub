# How can I use PHP, Redis and XAMPP together?
// plain

The combination of PHP, Redis and XAMPP can be used to create powerful web applications. To use them together, you will need to install and configure each component.

1. Install XAMPP:
XAMPP is a web development stack that includes Apache, MySQL, PHP, and other tools. It can be downloaded from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html).

2. Install Redis:
Redis is an in-memory data structure store that can be used as a database, cache, and message broker. It can be downloaded from [https://redis.io/download](https://redis.io/download).

3. Install the Redis PHP extension:
The Redis PHP extension is a PHP module that allows PHP to communicate with Redis. It can be downloaded from [https://github.com/phpredis/phpredis](https://github.com/phpredis/phpredis).

4. Configure XAMPP:
Once all components are installed, you will need to configure XAMPP to use Redis. This can be done by editing the `php.ini` file and adding the following line:

```
extension=redis.so
```

5. Test the setup:
You can now test the setup by creating a PHP script that connects to Redis.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo "Connected to Redis";
?>
```

## Output example


```
Connected to Redis
```

Once the script is executed, you should see the output `Connected to Redis`. This confirms that the setup is working correctly.

onelinerhub: [How can I use PHP, Redis and XAMPP together?](https://onelinerhub.com/predis/how-can-i-use-php--redis-and-xampp-together)