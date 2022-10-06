# How to compress GD image

```php
<?php

$im = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($im);
imagejpeg($im, '/tmp/image.jpg', 88);
```

- `$im` - image resource of original image to compress
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagejpeg` - saves `$im` gd object to the specified 'jpeg' file with a given level of compression
- `88` - quality (or compression) level, use lower values for better compression, up to `100` (best quality, worst compression)

group: quality


