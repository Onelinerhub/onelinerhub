# How to change font size

```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 60, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


group: font


