# How can I use Predis in my PHP project?
// plain

Predis is a PHP client library for the Redis key-value store that can be used in any PHP project. To use Predis in a project, first install it using composer:

```
composer require predis/predis
```

Then, include the autoloader in your project:

```
require 'vendor/autoload.php';
```

You can then create a client instance and start making requests:

```
$client = new Predis\Client();
$client->set('key', 'value');
$value = $client->get('key');
echo $value;
```

## Output example

```
value
```

The code above creates an instance of the Predis\Client class, sets a key-value pair and retrieves the value from Redis.

For more information, see the [Predis documentation](https://github.com/nrk/predis#readme).

onelinerhub: [How can I use Predis in my PHP project?](https://onelinerhub.com/predis/how-can-i-use-predis-in-my-php-project)