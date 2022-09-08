# How to draw rectangle COPY

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagerectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagerectangle` - creates rectangle
- `50, 100` - top left rectangle coordinates
- `150, 200` - bottom right rectangle coordinates
- `$c_green` - rectangle border color
- `imagePng` - saves image in PNG format to the given path

group: rectangle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagerectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```

