# How do I use the PHP Predis Client to connect to a Redis server?
// plain

1. First, make sure you have the [Predis PHP client](https://github.com/nrk/predis) installed.
2. Create a `Predis\Client` object with the `host` and `port` of your Redis server.
    ```php
    $redis = new Predis\Client([
        'host' => '127.0.0.1',
        'port' => 6379,
    ]);
    ```
3. To check if the connection is successful, you can call the `ping` method.
    ```php
    $redis->ping(); // Output: 'PONG'
    ```
4. To add a value to the Redis server, use the `set` method.
    ```php
    $redis->set('my_key', 'my_value');
    ```
5. To get the value, use the `get` method.
    ```php
    $redis->get('my_key'); // Output: 'my_value'
    ```
6. For more information, check out the [Predis Documentation](https://github.com/nrk/predis/wiki).
7. You can also find more examples in the [Predis examples repository](https://github.com/nrk/predis-examples).

onelinerhub: [How do I use the PHP Predis Client to connect to a Redis server?](https://onelinerhub.com/predis/how-do-i-use-the-php-predis-client-to-connect-to-a-redis-server)