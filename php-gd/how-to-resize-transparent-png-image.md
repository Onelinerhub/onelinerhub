# How to resize transparent PNG image

```php
<?php

$file = '/var/www/examples/clouds.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 300;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

- `/var/www/examples/clouds.png` - path to image to resize (has transparent background)
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagealphablending` - we're disabling alpha blending to prevent transparent background being converted to black color
- `imagesavealpha` - we're enabling alpha channel (controls transparency) for resulting image
- `imagecopyresampled` - resizes source image and writes result to destination image
- `imagePng` - saves image in PNG format to the given path

group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/clouds.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 300;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

