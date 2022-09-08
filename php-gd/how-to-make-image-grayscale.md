# How to make image grayscale

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

imagefilter($im, IMG_FILTER_GRAYSCALE);

imagepng($im, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to grayscale
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagefilter` - applies filter to image
- `IMG_FILTER_GRAYSCALE` - converts colors for our image to grayscale

group: filter

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

imagefilter($im, IMG_FILTER_GRAYSCALE);

imagepng($im, '/tmp/image.png');
```

