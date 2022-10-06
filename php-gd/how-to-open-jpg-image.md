# How to open JPG image

```php
$file = 'test.jpg';
$im = imagecreatefromjpeg($file);

# ...
```

- `$file` - image path to open
- `$im` - image resource to manipulate using [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) lib
- `imagecreatefromjpeg` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image

group: open


