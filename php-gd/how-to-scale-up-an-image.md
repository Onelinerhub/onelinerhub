# How to scale up an image

### To scale images up, we use the same approach as in [resizing images](https://onelinerhub.com/php-gd/how-to-resize-image).

```php
<?php

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*5,$size[1]*5);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*5,$size[1]*5,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```


group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/small.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor($size[0]*5,$size[1]*5);
imagecopyresampled($imf, $im, 0,0,0,0, $size[0]*5,$size[1]*5,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

