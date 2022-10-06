# How to add image to image

```php
<?php

$big = '/var/www/examples/heroine.png';
$small = '/var/www/examples/small.png';

$bg = imagecreatefrompng($big);
$wm = imagecreatefrompng($big);

imagecopy($bg, $wm, 50, 50, 0, 0, 100, 100);

imagePng($im, '/tmp/image.png');
```



