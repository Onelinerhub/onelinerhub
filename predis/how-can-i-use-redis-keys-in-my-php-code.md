# How can I use Redis keys in my PHP code?
// plain

Using Redis keys in PHP code is quite straightforward.

To start, you'll need to install the Redis PHP extension. This can be done with the command `pecl install redis`.

Once the extension is installed, you can use the following code to connect to Redis and set a key:

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('mykey', 'myvalue');
```

You can then retrieve the key's value by using the `get` method:

```
$value = $redis->get('mykey');
echo $value; // prints 'myvalue'
```

You can also use the `exists` method to check whether a key exists:

```
$exists = $redis->exists('mykey');
echo $exists; // prints '1'
```

You can also use the `del` method to delete a key:

```
$redis->del('mykey');
```

For more information, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How can I use Redis keys in my PHP code?](https://onelinerhub.com/predis/how-can-i-use-redis-keys-in-my-php-code)