# How to crop image

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecrop($im, ['x' => 0, 'y' => 0, 'width' => 200, 'height' => 200]);

imagePng($imf, '/tmp/image.png');
```


## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$imf = imagecrop($im, ['x' => 0, 'y' => 0, 'width' => 200, 'height' => 200]);

imagePng($imf, '/tmp/image.png');
```

