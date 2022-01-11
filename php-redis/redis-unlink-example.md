# Redis unlink example

### Unlink will remove specified keys asynchronously in contrast to [delete method](/php-redis/how-to-delete-key-from-redis):

```php
$redis->unlink('key');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `unlink` - removes key asynchronously
- `key` - name of the key to remove

group: delete


