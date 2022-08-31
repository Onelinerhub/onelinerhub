# How to scale up an image

### To scale images up, we use the same approach as in [resizing images](https://onelinerhub.com/php-gd/how-to-resize-image).

```php
<?php

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*10,$size[1]*10);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*10,$size[1]*10,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

- `/var/www/examples/small.png` - path to image to scale up
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

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*10,$size[1]*10);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*10,$size[1]*10,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

