# How to draw filled rectangle

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledrectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledrectangle` - creates filled rectangle
- `50, 100` - top left rectangle coordinate
- `150, 200` - bottom right rectangle coordinate
- `imagePng` - saves image in PNG format to the given path

group: rectangle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledrectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```

