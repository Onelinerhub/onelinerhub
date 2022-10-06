# How to add watermark to image

```php
<?php

$big = '/var/www/examples/heroine.png';
$small = '/var/www/examples/small.png';

$bg = imagecreatefrompng($big);
$wm = imagecreatefrompng($small);

$size = getimagesize($small);

imagecopy($bg, $wm, 100, 100, 0, 0, $size[0], $size[1]);

imagePng($bg, '/tmp/image.png');
```

- `$bg` - image to add watermark to
- `$wm` - watermark
- `getimagesize` - returns image size from given path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagecopy` - adds `$wm` watermark image to `$bg` image
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

imagecopy($bg, $wm, 100, 100, 0, 0, $size[0], $size[1]);

imagePng($bg, '/tmp/image.png');
```

