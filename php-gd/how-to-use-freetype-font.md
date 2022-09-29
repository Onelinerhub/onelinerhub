# How to use freetype font

```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/var/www/sumkin.otf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


group: font


