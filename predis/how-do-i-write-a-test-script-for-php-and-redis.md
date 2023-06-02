# How do I write a test script for PHP and Redis?
// plain

Writing a test script for PHP and Redis is a straightforward process.

First, we need to install the Redis PHP extension. This can be done by running the following command:
```
$ sudo apt-get install php-redis
```

Once the extension is installed, we can start writing our test script.

We'll start by connecting to the Redis server:
```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```

Next, we'll add some data to Redis:
```
$redis->set('key', 'value');
```

Finally, we'll retrieve the data from Redis and print it to the screen:
```
$value = $redis->get('key');
echo $value;
```

The output should be:
```
value
```

This is a basic example of how to write a test script for PHP and Redis.

## Helpful links
- [Redis PHP Documentation](https://redis.io/clients/php)
- [Redis PHP GitHub Repository](https://github.com/phpredis/phpredis)

onelinerhub: [How do I write a test script for PHP and Redis?](https://onelinerhub.com/predis/how-do-i-write-a-test-script-for-php-and-redis)