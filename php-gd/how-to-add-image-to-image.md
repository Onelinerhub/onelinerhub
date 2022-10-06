# How to add image to image

```php
<?php

$big = '/var/www/examples/heroine.png';
$small = '/var/www/examples/small.png';

$bg = imagecreatefrompng($big);
$wm = imagecreatefrompng($small);

$size = getimagesize($small);

imagecopy($bg, $wm, 50, 50, 0, 0, $size[0], $size[1]);

imagePng($bg, '/tmp/image.png');
```

- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `$bg` - larger image to add other image to
- `$wm` - smaller image to add to larger image
- `getimagesize` - returns image size from given path
- `imagecopy` - adds `$wm` image to `$bg` image using given coordinates and size
- `50, 50` - places smaller image at 50 pixels `Y` and 50 pixels `X` coordinates
- `imagePng` - saves image in PNG format to the given path

group: water

## Example: 
```php
<?php

$big = '/var/www/examples/heroine.png';
$small = '/var/www/examples/small.png';

$bg = imagecreatefrompng($big);
$wm = imagecreatefrompng($small);

$size = getimagesize($small);

imagecopy($bg, $wm, 25, 25, 0, 0, $size[0], $size[1]);

imagePng($bg, '/tmp/image.png');
```

