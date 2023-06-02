# How do I use the PHP Redis rawcommand?
// plain

Using the `rawcommand` method of the `Redis` class in `PHP` is a great way to execute arbitrary commands on a `Redis` server. Here is an example of how to use it:

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$reply = $redis->rawcommand('SET', 'mykey', 'myvalue');
echo $reply;
```

## Output example

```
OK
```

In the example, we connected to a `Redis` server running on `127.0.0.1` on port `6379`, and used the `rawcommand` method to execute the `SET` command with the arguments `mykey` and `myvalue`. The output of the command is `OK`, which indicates that the command was successful.

## Code explanation


1. `$redis = new Redis();` - create a new `Redis` object.
2. `$redis->connect('127.0.0.1', 6379);` - connect to a `Redis` server running on `127.0.0.1` on port `6379`.
3. `$reply = $redis->rawcommand('SET', 'mykey', 'myvalue');` - execute the `SET` command with the arguments `mykey` and `myvalue` using the `rawcommand` method.
4. `echo $reply;` - print the output of the command.

For more information about using the `rawcommand` method, see the [PHP Redis documentation](https://www.php.net/manual/en/redis.rawcommand.php).

onelinerhub: [How do I use the PHP Redis rawcommand?](https://onelinerhub.com/predis/how-do-i-use-the-php-redis-rawcommand)