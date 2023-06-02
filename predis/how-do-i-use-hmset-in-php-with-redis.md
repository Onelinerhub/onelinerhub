# How do I use hmset in PHP with Redis?
// plain

HMSET is a Redis command used to set multiple fields and values in a hash stored at a key. It can be used in PHP with the Predis library.

Example code and output:
```
<?php

require 'predis/autoload.php';
Predis\Autoloader::register();

$client = new Predis\Client();

$client->hmset('hashkey', [
    'field1' => 'value1',
    'field2' => 'value2',
    'field3' => 'value3',
]);

echo $client->hget('hashkey', 'field1'); // Output: value1
```

The code above uses the Predis library to connect to Redis and then uses the hmset command to set multiple fields and values in a hash stored at a key. The hget command is then used to get the value of one of the fields.

## Code explanation


- `require 'predis/autoload.php';` - Loads the Predis library.
- `Predis\Autoloader::register();` - Registers the Predis autoloader.
- `$client = new Predis\Client();` - Creates a new Predis client.
- `$client->hmset('hashkey', [` - Uses the hmset command to set multiple fields and values in a hash stored at a key.
- `'field1' => 'value1',` - Sets the field1 field to the value1 value.
- `'field2' => 'value2',` - Sets the field2 field to the value2 value.
- `'field3' => 'value3',` - Sets the field3 field to the value3 value.
- `]);` - Closes the array of fields and values.
- `echo $client->hget('hashkey', 'field1');` - Uses the hget command to get the value of the field1 field.

## Helpful links

- Predis library: https://github.com/nrk/predis
- Redis HMSET command: https://redis.io/commands/hmset
- Redis HGET command: https://redis.io/commands/hget

onelinerhub: [How do I use hmset in PHP with Redis?](https://onelinerhub.com/predis/how-do-i-use-hmset-in-php-with-redis)