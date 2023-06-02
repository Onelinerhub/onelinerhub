# How do I use PHP Predis with TLS encryption?
// plain

Using PHP Predis with TLS encryption requires a few steps:

1. Install the Predis library via [Composer](https://getcomposer.org/):
```
composer require predis/predis
```

2. Create a new client object, and configure it to use TLS encryption:
```
$client = new Predis\Client([
    'scheme' => 'tls',
    'host'   => '127.0.0.1',
    'port'   => 6379
]);
```

3. Use the client object to connect to the Redis server:
```
$client->connect();
```

4. Execute commands on the server:
```
$client->set('foo', 'bar');
```

5. Retrieve the result of the command:
```
$value = $client->get('foo');
echo $value;
// Output: "bar"
```

6. Close the connection when you are done:
```
$client->disconnect();
```

For more information about using TLS encryption with Predis, please refer to the official [Predis documentation](https://github.com/nrk/predis/wiki/Connection-Overview#using-tls).

onelinerhub: [How do I use PHP Predis with TLS encryption?](https://onelinerhub.com/predis/how-do-i-use-php-predis-with-tls-encryption)