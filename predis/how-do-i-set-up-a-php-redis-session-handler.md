# How do I set up a PHP Redis session handler?
// plain

1. Install the Redis PHP extension: `pecl install redis`
2. Create a PHP script to configure the Redis session handler:
```php
<?php
// Connect to Redis server
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Set session handler to Redis
$handler = new RedisSessionHandler($redis);
session_set_save_handler($handler, true);

// Start session
session_start();

// Show that the session is active
echo session_status() === PHP_SESSION_ACTIVE ? 'Session active' : 'Session not active';
```
## Output example
 `Session active`
3. Set session name and save path:
```php
<?php
session_name('my_session');
session_save_path('tcp://127.0.0.1:6379');
```
4. Set session cookie parameters:
```php
<?php
session_set_cookie_params(
    [
        'lifetime' => 86400,
        'path' => '/',
        'domain' => 'example.com',
        'secure' => false,
        'httponly' => true
    ]
);
```
5. Set session ID:
```php
<?php
session_id('my_session_id');
```
6. Set session save handler:
```php
<?php
$handler = new RedisSessionHandler($redis);
session_set_save_handler($handler, true);
```
7. Set session timeout:
```php
<?php
ini_set('session.gc_maxlifetime', 86400);
```

## Helpful links
- [Redis PHP extension](https://pecl.php.net/package/redis)
- [RedisSessionHandler](https://github.com/colinmollenhour/Cm_RedisSession)

onelinerhub: [How do I set up a PHP Redis session handler?](https://onelinerhub.com/predis/how-do-i-set-up-a-php-redis-session-handler)