# How do I use Predis to connect to a database in PHP?
// plain

Using Predis to connect to a database in PHP is easy and straightforward. The following is an example of how to connect to a Redis database using Predis:

```php
<?php
    require 'predis/autoload.php';
    Predis\Autoloader::register();

    $client = new Predis\Client([
        'scheme' => 'tcp',
        'host'   => '127.0.0.1',
        'port'   => 6379,
    ]);

    echo $client->ping();
?>
```

## Output example
 `PONG`

The code above does the following:

1. Require the Predis autoloader.
2. Register the Predis autoloader.
3. Create a new client instance, passing in a configuration array that contains the scheme, host, and port of the Redis server.
4. Ping the Redis server to check the connection.

For more information on using Predis to connect to a database in PHP, please refer to the [Predis documentation](https://github.com/nrk/predis).

onelinerhub: [How do I use Predis to connect to a database in PHP?](https://onelinerhub.com/predis/how-do-i-use-predis-to-connect-to-a-database-in-php)