# How to make image grayscale

```php
<?php
 
$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

for ( $i = 0; $i < 20; $i++ ) {
  imagefilter($im, IMG_FILTER_GRAYSCALE);
}

imagePng($im, '/tmp/image.png');
```

- `/var/www/examples/heroine.png` - path to image to blur
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagefilter` - applies filter to image
- `$i < 20` - we apply Gaussian filter 20 times for better blurring effect
- `imagePng` - saves image in PNG format to the given path

group: filter

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

imagefilter($im, IMG_FILTER_GRAYSCALE);

imagepng($im, '/tmp/image.png');
```

