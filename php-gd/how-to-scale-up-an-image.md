# How to scale up an image

### To scale images up, we use the same approach as in [resizing images](https://onelinerhub.com/php-gd/how-to-resize-image).

```php
<?php

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*10,$size[1]*10);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*10,$size[1]*10,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```


group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*10,$size[1]*10);
imagealphablending($imf, false);
imagesavealpha($imf, true);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*10,$size[1]*10,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

