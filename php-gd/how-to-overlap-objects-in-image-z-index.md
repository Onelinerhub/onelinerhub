# How to control objects overlapping order (z-index)

### There's nothing like `z-index` in `gd`, but you can control what's being on top. Objects that are drawn later will be on top of previously drawn. Red ellipse will be on top of green one since it was drawn later:

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$c_red = imageColorAllocate($im, 255, 64, 64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);
imagefilledellipse($im, 250, 200, 100, 100, $c_red);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `imagePng` - saves image in PNG format to the given path

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$c_red = imageColorAllocate($im, 255, 64, 64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);
imagefilledellipse($im, 250, 200, 100, 100, $c_red);

imagePng($im, '/tmp/image.png');
```

