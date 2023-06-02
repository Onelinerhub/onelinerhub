# How can I use PHP to increment values in Redis using ZINCRBY?
// plain

To increment values in Redis using ZINCRBY, you can use the PHP function `redis()->zincrby()`. This function takes three parameters: the key name, the increment amount, and the member. The syntax looks like this:

```php
$redis->zincrby('key', 5, 'member');
```

This command will increment the value of 'member' in the 'key' key by 5. The output of this command will be the new value of 'member' in 'key'. For example:

```
$redis->zincrby('key', 5, 'member');
// Output: 10
```

## Code explanation


* `$redis` - This is the Redis instance.
* `zincrby()` - This is the command to increment values in Redis.
* `'key'` - This is the key name.
* `5` - This is the increment amount.
* `'member'` - This is the member.

For more information on this command, please see the [Redis documentation](https://redis.io/commands/zincrby).

onelinerhub: [How can I use PHP to increment values in Redis using ZINCRBY?](https://onelinerhub.com/predis/how-can-i-use-php-to-increment-values-in-redis-using-zincrby)