# Drawing with GD - usage example 

```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```

- `imageCreate` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `400, 300` - we create image of `400` pixels in width and `300` in height
- `imageColorAllocate` - creates color object to later use in image
- `0,0,0` - RGB codes for black color
- `46,204,64` - RGB codes for nice green color from [clrs.cc](https://clrs.cc/)
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `imagePng` - saves image in PNG format to the given path
- `/tmp/image.png` - path to write generated image to

group: install

## Example: 
```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 100, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```

