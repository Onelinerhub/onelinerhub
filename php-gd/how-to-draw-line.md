# How to draw a line

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageline($im, 50, 50, 350, 250, $c_green);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imageline` - draws line using given coordinates and color
- `$c_green` - color to use as line color
- `50, 50` - starting coordinates for our line
- `350, 250` - end of line coordinates
- `imagePng` - saves image in PNG format to the given path

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageline($im, 50, 50, 350, 250, $c_green);

imagePng($im, '/tmp/image.png');
```

