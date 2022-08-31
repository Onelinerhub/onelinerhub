# How to resize image

### To keep proportions width/height automatically, take a look at [resizing with aspect ratio keep](https://onelinerhub.com/php-gd/how-to-resize-image-and-keep-aspect-ratio).

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```


group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

