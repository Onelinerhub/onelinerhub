# How to flip an image

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

imageflip( $im, IMG_FLIP_VERTICAL );
imagePng($im, '/tmp/image.png');
```

- `$file` - image to rotate
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imageflip` - flips given image in a specified direction
- `IMG_FLIP_VERTICAL` - flips image vertically, explore [other options](https://www.php.net/manual/en/function.imageflip.php)
- `imagePng` - saves image in PNG format to the given path

group: rotate

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

imageflip( $im, IMG_FLIP_VERTICAL );
imagePng($im, '/tmp/image.png');
```

