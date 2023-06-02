# How do I use a Redis message queue with PHP?
// plain

Using Redis message queue with PHP is quite easy.

1. First, install the [Predis](https://github.com/nrk/predis) library:

```
composer require predis/predis
```

2. Then, create an instance of the client:

```php
$redis = new Predis\Client();
```

3. To add an item to the queue:

```php
$redis->rpush('messages', 'Hello, world!');
```

4. To retrieve an item from the queue:

```php
$message = $redis->lpop('messages');
// Output: Hello, world!
```

5. To check the length of the queue:

```php
$queue_length = $redis->llen('messages');
```

6. To delete the queue:

```php
$redis->del('messages');
```

7. To close the connection:

```php
$redis->quit();
```

onelinerhub: [How do I use a Redis message queue with PHP?](https://onelinerhub.com/predis/how-do-i-use-a-redis-message-queue-with-php)