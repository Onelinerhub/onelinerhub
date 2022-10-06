# How to add border to image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

imagesetthickness($im, 15);
$c_green = imageColorAllocate($im, 46,204,64);
imagerectangle($im, 0, 0, $size[0]-1, $size[1]-1, $c_green);

imagePng($im, '/tmp/image.png');
```

- `$file` - source image file add border to
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagesetthickness` - set line thickness (border width, set to `15` pixels in our case)
- `imageColorAllocate` - creates color object to later use in image
- `imagerectangle` - creates rectangle
- `/tmp/image.png` - path to write generated image to

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

imagesetthickness($im, 15);
$c_green = imageColorAllocate($im, 46,204,64);
imagerectangle($im, 0, 0, $size[0]-1, $size[1]-1, $c_green);

imagePng($im, '/tmp/image.png');
```

