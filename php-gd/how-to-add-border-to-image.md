# How to add border to image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$c_green = imageColorAllocate($im, 46,204,64);
imagerectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```



