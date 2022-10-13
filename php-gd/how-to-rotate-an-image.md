# How to rotate an image

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_black = imageColorAllocate($im, 0,0,0);
$imr = imagerotate( $im, 90, $c_black );

imagePng($imr, '/tmp/image.png');
```

- `$file` - image to rotate
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imageColorAllocate` - creates color object to later use in image
- `imagerotate` - rotates given image and returns new `gd` image object
- `90` - rotate image by `90` degrees
- `$c_black` - color to use for background (if necessary)
- `imagePng` - saves image in PNG format to the given path

group: rotate

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_black = imageColorAllocate($im, 0,0,0);
$imr = imagerotate( $im, 90, $c_black );

imagePng($imr, '/tmp/image.png');
```

