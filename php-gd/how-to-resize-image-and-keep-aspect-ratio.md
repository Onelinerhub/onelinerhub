# How to resize an image and keep aspect ratio

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 400;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to resize
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `$w = 400` - resize image to `400` pixels wide
- `$w * $size[1] / $size[0]` - calculates resized image height based on source image proportions
- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagecopyresampled` - resizes source image and writes result to destination image
- `imagePng` - saves image in PNG format to the given path

group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 400;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

