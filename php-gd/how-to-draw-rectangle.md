# How to draw rectangle with border

### Approach is to first [draw filled rectangle](https://onelinerhub.com/php-gd/how-to-draw-filled-rectangle) and then [draw rectangle border](https://onelinerhub.com/php-gd/how-to-draw-rectangle-copy) to finally get rectangle with border.

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_fill = imageColorAllocate($im, 46,204,64);
$c_border = imageColorAllocate($im, 1,255,112);

imagefilledrectangle($im, 50, 100, 150, 200, $c_fill);
imagerectangle($im, 50, 100, 150, 200, $c_border);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagerectangle` - creates rectangle
- `imagefilledrectangle` - creates filled rectangle
- `imagePng` - saves image in PNG format to the given path

group: rectangle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_fill = imageColorAllocate($im, 46,204,64);
$c_border = imageColorAllocate($im, 1,255,112);

imagefilledrectangle($im, 50, 100, 150, 200, $c_fill);
imagerectangle($im, 50, 100, 150, 200, $c_border);

imagePng($im, '/tmp/image.png');
```

