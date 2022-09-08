# How to draw circle

### Check [antialiasing strategies](https://onelinerhub.com/php-gd/better-antialias-with-gd) to get smooth drawing.

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `200, 150` - coordinates of center of circle
- `100, 100` - horizontal and vertical radius should be equal to get circle
- `$c_green` - fill color
- `imagePng` - saves image in PNG format to the given path

group: circle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```

