# How can I use Redis with the Yii PHP framework?
// plain

Redis can be used with the Yii PHP framework by using the [Redis extension](https://github.com/yiisoft/yii2-redis) for Yii2. This extension provides a full set of Redis commands implemented as methods of the yii\redis\Connection class.

For example, to set a key-value pair, you can use the `set()` method:

```
$redis = Yii::$app->redis;
$redis->set('my-key', 'my-value');
```

To get a value by key, use the `get()` method:

```
$value = $redis->get('my-key');
echo $value; // prints "my-value"
```

Other Redis commands can be used in a similar way. The full list of available commands can be found in the [documentation](https://github.com/yiisoft/yii2-redis/blob/master/docs/guide/usage.md).

onelinerhub: [How can I use Redis with the Yii PHP framework?](https://onelinerhub.com/predis/how-can-i-use-redis-with-the-yii-php-framework)