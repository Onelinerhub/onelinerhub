# How to set image background color

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_green = imageColorAllocate($im, 46,204,64);
imagefill($im, 0, 0, $c_green);

$c_black = imageColorAllocate($im, 0,0,0);
imageellipse($im, 200, 150, 100, 100, $c_black);

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagefill` - fills an entire image with a given color (green in our case)
- `imagePng` - saves image in PNG format to the given path

group: background

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_green = imageColorAllocate($im, 46,204,64);
imagefill($im, 0, 0, $c_green);

$c_black = imageColorAllocate($im, 0,0,0);
imagefilledellipse($im, 200, 150, 100, 100, $c_black);

imagePng($im, '/tmp/image.png');
```

