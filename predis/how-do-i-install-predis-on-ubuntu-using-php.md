# How do I install Predis on Ubuntu using PHP?
// plain

To install Predis on Ubuntu using PHP, you will need to have [Composer](https://getcomposer.org/) installed.

1. Run the following command in your terminal to install Predis:

```
composer require predis/predis
```

2. After the installation is complete, you will need to add the following line of code to your `php.ini` file:

```
extension=predis.so
```

3. Finally, you will need to restart your web server in order for the changes to take effect.

4. To test if Predis is installed correctly, you can run the following code in your terminal:

```
<?php
$client = new Predis\Client();
$client->set('foo', 'bar');
$value = $client->get('foo');
echo $value;
```

The output of the code should be `bar`.

5. You can also refer to the [Predis documentation](https://github.com/nrk/predis/blob/v1.1/README.md) for more information.

6. You can also refer to the [Predis installation guide](https://github.com/nrk/predis/wiki/Installation) for more detailed instructions.

7. You can also refer to the [PHP manual](https://www.php.net/manual/en/book.predis.php) for more information.

onelinerhub: [How do I install Predis on Ubuntu using PHP?](https://onelinerhub.com/predis/how-do-i-install-predis-on-ubuntu-using-php)