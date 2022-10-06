# How to open PNG image

```php
$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

# ...
```

- `$file` - path of an image to open
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `$im` - image resource to manipulate using [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) lib

group: open


