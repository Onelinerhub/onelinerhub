# Better antialias with GD

### This is rather a hack, than systematic solution, so mind using other libs like [Imagemagick for PHP](https://www.php.net/manual/ru/book.imagick.php) to get native antialiasing support.

```php
<?php

$im = imagecreatetruecolor(4000, 3000);
imageantialias($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 2000, 1500, 800, 800, $c_green);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,4000,3000);

imagePng($imf, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageantialias` - enable antialiasing for the given image
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `4000, 3000` - we have created initial image of large size (10x what we need in result)
- `imagecopyresampled` - now we resize source large image (`4000x3000`) to resulting image (`400x300`) to apply better antialiasing
- `imagePng` - saves image in PNG format to the given path

group: antialias

## Example: 
```php
<?php

$im = imagecreatetruecolor(4000, 3000);
imageantialias($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 2000, 1500, 800, 800, $c_green);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,4000,3000);

imagePng($imf, '/tmp/image.png');
```

