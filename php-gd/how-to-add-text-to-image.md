# How to add text to image

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 50, 0, 100, 1000, $c_green, $font, 'wonder woman');

imagePng($im, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to add text to
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imageColorAllocate` - creates color object to later use in image
- `$font` - path to `ttf` font to use
- `imagettftext` - draw text with given `ttf` font
- `imagePng` - saves image in PNG format to the given path

group: text

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 50, 0, 100, 1000, $c_green, $font, 'wonder woman');

imagePng($im, '/tmp/image.png');
```

