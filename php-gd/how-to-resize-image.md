# How to resize an image

### To keep proportions width/height automatically, take a look at [resizing with aspect ratio keep](https://onelinerhub.com/php-gd/how-to-resize-image-and-keep-aspect-ratio).

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to resize
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagecopyresampled` - resizes source image and writes result to destination image
- `$imf` - destination image (will save resized image)
- `0,0,0,0` - `X` and `Y` coordinates of left point in source (first 2 numbers) and destination (last 2 numbers) images
- `400,300` - we're resizing image to `400x300` pixels
- `imagePng` - saves image in PNG format to the given path

group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

