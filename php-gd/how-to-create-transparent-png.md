# How to create transparent PNG

### This code creates and saves PNG image with black circle on a transparent background:

```php
<?php

$im = imagecreatetruecolor(400, 300);

imagealphablending($im, false);
$tr = imagecolorallocatealpha($im, 0, 0, 0, 255);
imagefill($im, 0, 0, $tr);
imagesavealpha($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
imagefilledellipse($im, 200, 150, 100, 100, $c_black);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagealphablending` - we're disabling alpha blending to prevent transparent background being converted to black color
- `imagecolorallocatealpha` - creates color with transparency (in our case, we just create fully transparent color)
- `imagefill(` - fills an entire image with a given color (green in our case)
- `imagesavealpha` - we're enabling alpha channel (controls transparency) for resulting image
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `imagePng` - saves image in PNG format to the given path

group: background


