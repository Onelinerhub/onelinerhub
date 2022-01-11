# How to delete all keys

### Warning! This will delete *ALL* data from your Redis server:

```php
$redis->flushAll();
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `flushAll` - deletes all keys from Redis server

group: delete


