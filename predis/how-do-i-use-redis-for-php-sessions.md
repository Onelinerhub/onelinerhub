# How do I use Redis for PHP sessions?
// plain

The following steps explain how to use Redis for PHP sessions:

1. Install the Redis PHP extension:
```
$ sudo pecl install redis
```

2. Enable the extension in php.ini:
```
extension=redis.so
```

3. Configure the session handler in php.ini:
```
session.save_handler = redis
session.save_path = "tcp://host1:6379?weight=1, tcp://host2:6379?weight=2&timeout=2.5"
```

4. Update your code to use the session handler:
```php
<?php
session_set_save_handler(
    array('RedisSessionHandler', 'open'),
    array('RedisSessionHandler', 'close'),
    array('RedisSessionHandler', 'read'),
    array('RedisSessionHandler', 'write'),
    array('RedisSessionHandler', 'destroy'),
    array('RedisSessionHandler', 'gc')
);

session_start();
```

5. Start working with your session data:
```php
<?php
$_SESSION['name'] = 'John Doe';
$name = $_SESSION['name'];
echo $name; // Outputs: John Doe
```

6. Finally, don't forget to close the session:
```php
<?php
session_write_close();
```

For more information, check out the official [PHP documentation](https://www.php.net/manual/en/session.configuration.php#ini.session.save-handler) and [Redis documentation](https://redis.io/topics/session-handler).

onelinerhub: [How do I use Redis for PHP sessions?](https://onelinerhub.com/predis/how-do-i-use-redis-for-php-sessions)