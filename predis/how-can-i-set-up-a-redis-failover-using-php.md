# How can I set up a Redis failover using PHP?
// plain

Setting up a Redis failover using PHP is relatively straight forward. First, you will need to set up two Redis instances, one as the primary and the other as the failover.

Once the two instances are up and running, you can use the `phpredis` library to connect to the primary instance.

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```

Next, you can use the `addServer` method to add the failover instance.

```php
$redis->addServer('127.0.0.1', 6380);
```

Finally, you can use the `setOption` method to set the `Redis::OPT_SLAVE_FAILOVER` option to `Redis::FAILOVER_DISTRIBUTE` in order to enable the failover feature.

```php
$redis->setOption(Redis::OPT_SLAVE_FAILOVER, Redis::FAILOVER_DISTRIBUTE);
```

Now your Redis failover is set up and ready to use.

**Parts of code explained:**
1. `$redis = new Redis();` - This creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);` - This connects to the primary Redis instance.
3. `$redis->addServer('127.0.0.1', 6380);` - This adds the failover instance.
4. `$redis->setOption(Redis::OPT_SLAVE_FAILOVER, Redis::FAILOVER_DISTRIBUTE);` - This sets the `Redis::OPT_SLAVE_FAILOVER` option to `Redis::FAILOVER_DISTRIBUTE` in order to enable the failover feature.

**## Helpful links**
- [phpredis documentation](https://github.com/phpredis/phpredis#addserver)
- [Redis Slave Failover](https://redis.io/topics/replication#slave-failover)

onelinerhub: [How can I set up a Redis failover using PHP?](https://onelinerhub.com/predis/how-can-i-set-up-a-redis-failover-using-php)