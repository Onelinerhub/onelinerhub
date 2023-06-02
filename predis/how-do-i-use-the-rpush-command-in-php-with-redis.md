# How do I use the rpush command in PHP with Redis?
// plain

The `rpush` command in PHP with Redis can be used to add one or more values to the end of a list.

For example, to add a single value to the end of a list, we can use the following code:
```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->rpush('list_name', 'value_to_add');
```

This command will return the length of the list after the value has been added.

If we want to add multiple values to the end of the list, we can use the following code:
```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->rpush('list_name', ['value1', 'value2', 'value3']);
```

This command will return the length of the list after the values have been added.

## Code explanation


* `$redis = new Redis();` - Connects to a Redis server.
* `$redis->connect('127.0.0.1', 6379);` - Connects to a Redis server at the specified host and port.
* `$redis->rpush('list_name', 'value_to_add');` - Adds a single value to the end of a list.
* `$redis->rpush('list_name', ['value1', 'value2', 'value3']);` - Adds multiple values to the end of a list.

For more information, please see the [Redis documentation](https://redis.io/commands/rpush).

onelinerhub: [How do I use the rpush command in PHP with Redis?](https://onelinerhub.com/predis/how-do-i-use-the-rpush-command-in-php-with-redis)