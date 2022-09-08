# How to blur image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

imagefilter($image, IMG_FILTER_GAUSSIAN_BLUR);

imagePng($imf, '/tmp/image.png');
```


group: filter


