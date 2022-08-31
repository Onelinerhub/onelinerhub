# Using antialias in GD

### **Note**, that PHP GD lib has limited antialiasing capabilities. Alternative approach is to create [larger image and resize it to apply smarter antialiasing](https://onelinerhub.com/php-gd/better-antialias-with-gd).

```php
<?php

$im = imagecreatetruecolor(400, 300);
imageantialias($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');=
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageantialias` - enable antialiasing for the given image
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `imagePng` - saves image in PNG format to the given path

group: antialias

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);
imageantialias($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 80, 80, $c_green);

imagePng($im, '/tmp/image.png');
```

