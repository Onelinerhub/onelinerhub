# How to crop image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecrop($im, ['x' => 50, 'y' => 50, 'width' => 600, 'height' => 300]);

imagePng($imf, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to crop
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagecrop` - crops given image
- `'x' => 50, 'y' => 50` - top left point to start crop on
- `'width' => 600, 'height' => 300` - size of cropping rectangle
- `imagePng` - saves image in PNG format to the given path

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecrop($im, ['x' => 50, 'y' => 50, 'width' => 600, 'height' => 300]);

imagePng($imf, '/tmp/image.png');
```

