# How can I use PHP and Redis to parse JSON data?
// plain

PHP and Redis can be used together to parse JSON data. To do this, the [PHP Redis extension](https://github.com/phpredis/phpredis) must be installed. Once installed, the `json_decode` function can be used to convert a JSON string into a PHP array.

For example, given the following JSON string:

```json
{
    "name": "John Doe",
    "age": 30
}
```

The following code can be used to parse the data:

```php
$jsonString = '{"name": "John Doe", "age": 30}';
$data = json_decode($jsonString, true);
```

This will create an associative array that looks like this:

```
Array
(
    [name] => John Doe
    [age] => 30
)
```

The data can then be stored in Redis using the `set` command. For example, to store the data in a key called `user_data`:

```php
$redis->set('user_data', $data);
```

The data can then be retrieved from Redis using the `get` command:

```php
$data = $redis->get('user_data');
```

This will return the data as a PHP array.

onelinerhub: [How can I use PHP and Redis to parse JSON data?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-parse-json-data)