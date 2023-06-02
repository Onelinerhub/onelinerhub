# How do I use PHP to set a key in Redis?
// plain

1. First, make sure you have the [PHP Redis extension](https://github.com/phpredis/phpredis) installed.

2. Establish a connection to the Redis server in your PHP code:
```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```

3. Set the key in Redis using the `set` method:
```
$redis->set('mykey', 'myvalue');
```

4. Check that the key has been set by retrieving its value:
```
$value = $redis->get('mykey');
echo $value; // Outputs 'myvalue'
```

5. If you want to set an expiry for the key, you can use the `setex` method instead:
```
$redis->setex('mykey', 60, 'myvalue');
```
This will set the key to expire after 60 seconds.

6. You can also set multiple keys at once using the `mset` method:
```
$redis->mset(array('key1' => 'value1', 'key2' => 'value2'));
```

7. To retrieve multiple keys at once, use the `mget` method:
```
$values = $redis->mget(array('key1', 'key2'));
print_r($values); // Outputs Array ( [0] => value1 [1] => value2 )
```

onelinerhub: [How do I use PHP to set a key in Redis?](https://onelinerhub.com/predis/how-do-i-use-php-to-set-a-key-in-redis)