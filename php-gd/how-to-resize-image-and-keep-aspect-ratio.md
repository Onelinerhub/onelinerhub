# How to resize an image and keep aspect ratio

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 400;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```


group: resize

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$w = 400;
$h = $w * $size[1] / $size[0];

$imf = imagecreatetruecolor($w, $h);
imagecopyresampled($imf, $im, 0,0,0,0, $w,$h,$size[0],$size[1]);

imagePng($imf, '/tmp/image.png');
```

