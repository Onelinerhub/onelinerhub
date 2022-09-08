# How to add text to image

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


group: text

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);

$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```

