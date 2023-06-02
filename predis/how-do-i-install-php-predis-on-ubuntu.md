# How do I install PHP Predis on Ubuntu?
// plain

1. Download the latest version of Predis from [GitHub](https://github.com/nrk/predis/releases):

```
$ wget https://github.com/nrk/predis/archive/v1.1.1.zip
```

2. Unzip the archive:

```
$ unzip v1.1.1.zip
```

3. Change directory into the unzipped folder:

```
$ cd predis-1.1.1
```

4. Install the dependencies using [Composer](https://getcomposer.org/):

```
$ php composer.phar install
```

5. Copy the `Predis` folder into your project:

```
$ cp -r vendor/predis/predis/src/Predis /path/to/your/project/
```

6. Include the `Autoloader` in your project:

```php
<?php
require '/path/to/your/project/Predis/Autoloader.php';
Predis\Autoloader::register();
```

7. You can now use Predis in your project:

```php
<?php
$client = new Predis\Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1',
    'port'   => 6379,
]);

$client->set('foo', 'bar');
$value = $client->get('foo');

echo $value; // Outputs: 'bar'
```

onelinerhub: [How do I install PHP Predis on Ubuntu?](https://onelinerhub.com/predis/how-do-i-install-php-predis-on-ubuntu)