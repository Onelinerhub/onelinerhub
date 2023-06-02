# How do I install Predis with PHP?
// plain

1. Installing Predis with PHP is easy and straightforward.
2. First, you need to download the latest version of Predis from [GitHub](https://github.com/nrk/predis).
3. Then, unzip the downloaded file and include the library in your project.
```
<?php
require 'path/to/Predis/Autoloader.php';
Predis\Autoloader::register();
```
4. After that, you can create a new instance of the client.
```
<?php
$client = new Predis\Client();
```
5. You can then use the client to connect to the Redis server.
```
<?php
$client->connect('127.0.0.1', 6379);
```
6. Finally, you can use the client to execute commands.
```
<?php
$client->set('key', 'value');
$value = $client->get('key');
echo $value; // Outputs: value
```
7. For more information, please refer to the [Predis documentation](https://github.com/nrk/predis/wiki).

onelinerhub: [How do I install Predis with PHP?](https://onelinerhub.com/predis/how-do-i-install-predis-with-php)