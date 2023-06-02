# How do I use the PHP Predis command?
// plain

The Predis command is a PHP library that allows you to interact with Redis server from PHP.

Using Predis is fairly simple. First, you must install the Predis library using Composer.

```
composer require predis/predis
```

Once installed, you can start using Predis commands in your PHP scripts. Here is an example of connecting to a Redis server and setting a value:

```php
<?php

require 'vendor/autoload.php';

$client = new Predis\Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1',
    'port'   => 6379,
]);

$client->set('key', 'value');
```

The above code will connect to the Redis server running on `127.0.0.1:6379` and set the key `key` with the value `value`.

You can also use Predis to get values from the Redis server, delete keys, and perform other operations. Here is an example of getting a value from the Redis server:

```php
<?php

require 'vendor/autoload.php';

$client = new Predis\Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1',
    'port'   => 6379,
]);

$value = $client->get('key');
echo $value; // Outputs "value"
```

The above code will get the value of the key `key` from the Redis server and output it.

For more information on using Predis, please refer to the [official documentation](https://github.com/nrk/predis/blob/develop/doc/index.md).

onelinerhub: [How do I use the PHP Predis command?](https://onelinerhub.com/predis/how-do-i-use-the-php-predis-command)