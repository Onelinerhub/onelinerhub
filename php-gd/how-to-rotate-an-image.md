# How to rotate an image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$c_black = imageColorAllocate($im, 0,0,0);
$imr = imagerotate( $im, 90, $c_black )

imagePng($imr, '/tmp/image.png');
```


group: rotate


