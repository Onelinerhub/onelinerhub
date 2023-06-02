# How can I use the hset command in Redis with PHP?
// plain

The `hset` command can be used in Redis with PHP to set the value of a field in a hash stored at a key.

For example, the following code will set the field `name` to `John` in the hash stored at the key `myhash`:

```php
$redis->hset("myhash", "name", "John");
```

The code returns `1` if the field is a new field in the hash and `0` if the field already exists in the hash.

The `hset` command can also be used to set multiple fields in a hash at once. The following code sets the fields `name` to `John` and `age` to `30` in the hash stored at the key `myhash`:

```php
$redis->hmset("myhash", ["name" => "John", "age" => "30"]);
```

The code returns `true` if the fields were set in the hash.

The command can be used with the following methods in the Redis class of the [phpredis](https://github.com/phpredis/phpredis) library:

* `hset`: Set the string value of a hash field
* `hmset`: Set multiple fields in a hash

## Helpful links

* [Redis hset command](https://redis.io/commands/hset)
* [Redis hmset command](https://redis.io/commands/hmset)
* [phpredis library](https://github.com/phpredis/phpredis)

onelinerhub: [How can I use the hset command in Redis with PHP?](https://onelinerhub.com/predis/how-can-i-use-the-hset-command-in-redis-with-php)